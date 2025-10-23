# -*- coding: utf-8 -*-
"""
🎬 JellyNamer - Smart Episode & Folder Renamer for Jellyfin, Plex & Emby
Author: c13p70
License: MIT (2025)

Features:
 - Automatic rename of TV episodes (Jellyfin/Plex style)
 - Season folder detection (SxxExxx)
 - Interactive setup (no config editing)
 - Optional dry-run preview
 - JSON backup (with timestamp)
 - Restore from backup
 - File cleanup (.nfo, .jpg, .trickplay)
 - Intelligent filename cleaning (removes duplicates, extensions, resolutions)
 - UTF-8 support for special characters (ä, ö, ü, ß, etc.)
"""

import os
import re
import json
import shutil
import sys
from datetime import datetime

# Enable UTF-8 output on Windows console
if sys.platform.startswith("win"):
    os.system("")

# === Regex patterns ===
FOLDER_PATTERN = re.compile(r"S(?P<season>\d+)[ ._-]*E(?P<start>\d+)-E(?P<end>\d+)", re.IGNORECASE)
EPISODE_PATTERN = re.compile(r"(\d{3,4})|E(\d{2,3})", re.IGNORECASE)


def clean_title(name: str, show_name: str) -> str:
    """Cleans messy file titles before renaming."""
    pattern_show = re.escape(show_name)
    name = re.sub(pattern_show, "", name, flags=re.IGNORECASE)
    name = re.sub(r"S\d{1,3}", "", name)
    name = re.sub(r"E\d{1,4}", "", name)
    name = re.sub(
        r"\b(720p|1080p|2160p|x264|x265|hdr|webrip|bluray|hd|sd|4k|hdtv|dvdrip)\b",
        "",
        name,
        flags=re.IGNORECASE,
    )
    name = re.sub(r"\.(mp4|mkv|avi|mov|wmv|flv|mpg)+", "", name, flags=re.IGNORECASE)
    name = re.sub(r"[._]+", " ", name)
    name = re.sub(r"-{2,}", "-", name)
    name = re.sub(r"\s{2,}", " ", name)
    name = re.sub(r"\b(sample|copy|part\d+|episode|ep)\b", "", name, flags=re.IGNORECASE)
    name = re.sub(r"\bmp4\b", "", name, flags=re.IGNORECASE)
    return name.strip(" -_.")


def create_backup(backup_dir, data):
    ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_file = os.path.join(backup_dir, f"JellyNamer_backup_{ts}.json")
    with open(backup_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"💾 Backup saved: {backup_file}")
    return backup_file


def ask_bool(prompt, default):
    default_str = "1" if default else "0"
    val = input(f"{prompt} (1=True, 0=False, Enter={default_str}): ").strip()
    if val not in ["0", "1", ""]:
        print("[WARN] Invalid input, using default.")
        return default
    return default if val == "" else val == "1"


def unlock_folder(path):
    """Removes read-only / hidden attributes from a folder recursively (Windows safe)."""
    try:
        if sys.platform.startswith("win"):
            os.system(f'attrib -r -s -h "{path}" /S /D')
        else:
            for root, dirs, files in os.walk(path):
                for p in [*dirs, *files]:
                    full_path = os.path.join(root, p)
                    try:
                        os.chmod(full_path, 0o777)
                    except Exception:
                        pass
        return True
    except Exception as e:
        print(f"[WARN] Could not unlock folder {path}: {e}")
        return False


def delete_file(path, dry_run, backup_data):
    """Delete a file or directory (records in backup)."""
    if dry_run:
        print(f"[TEST] Would delete: {path}")
        return
    try:
        if os.path.isdir(path):
            unlock_folder(path)
            shutil.rmtree(path, ignore_errors=True)
        else:
            os.remove(path)
        backup_data["deleted"].append(path)
        print(f"[OK] Deleted: {path}")
    except Exception as e:
        print(f"[WARN] Failed to delete {path}: {e}")


def rename_folders(root_dir, dry_run, backup_data):
    for root, dirs, _ in os.walk(root_dir):
        for d in dirs:
            match = FOLDER_PATTERN.search(d)
            if not match:
                continue
            season = int(match.group("season"))
            start_ep = match.group("start")
            end_ep = match.group("end")
            new_name = f"Season {season:02d} (E{start_ep}-{end_ep})"
            old_path = os.path.join(root, d)
            new_path = os.path.join(root, new_name)
            backup_data["folders"].append({"old": old_path, "new": new_path})
            if dry_run:
                print(f"[TEST] Folder: {d} → {new_name}")
            else:
                try:
                    os.rename(old_path, new_path)
                    print(f"[OK] Folder renamed: {d} → {new_name}")
                except Exception as e:
                    print(f"[WARN] Error renaming folder {d}: {e}")


def rename_files(root_dir, show_name, dry_run, delete_trickplay, show_trickplay, backup_data):
    for root, _, files in os.walk(root_dir):
        folder_match = FOLDER_PATTERN.search(root)
        if not folder_match:
            continue
        season = int(folder_match.group("season"))
        start_ep = int(folder_match.group("start"))
        end_ep = int(folder_match.group("end"))
        header_printed = False
        for file in files:
            try:
                file = file.encode("latin-1").decode("utf-8")
            except (UnicodeEncodeError, UnicodeDecodeError):
                file = file.encode("latin-1", errors="replace").decode("utf-8", errors="replace")
            if "trickplay" in file.lower():
                if show_trickplay:
                    print(f"[INFO] Ignored trickplay: {file}")
                if delete_trickplay and not dry_run:
                    try:
                        os.remove(os.path.join(root, file))
                        backup_data["deleted"].append(os.path.join(root, file))
                    except Exception as e:
                        print(f"[WARN] Could not delete trickplay: {e}")
                continue
            if not file.lower().endswith((".mp4", ".mkv", ".avi", ".mov", ".wmv")):
                continue
            ep_match = EPISODE_PATTERN.search(file)
            if not ep_match:
                continue
            ep_num = int(ep_match.group(1) or ep_match.group(2))
            if not (start_ep <= ep_num <= end_ep):
                continue
            if not header_printed:
                print(f"\n📂 {root} → Season {season} (Episodes {start_ep}-{end_ep})")
                header_printed = True
            title = clean_title(file, show_name)
            title = re.sub(r"\.(mp4|mkv|avi|mov|wmv|flv|mpg)+$", "", title, flags=re.IGNORECASE)
            title = title.strip(" -_.")
            new_filename = f"{show_name}-S{season:02d}E{ep_num:03d}-{title}.mp4"
            old_path = os.path.join(root, file)
            new_path = os.path.join(root, new_filename)
            backup_data["files"].append({"old": old_path, "new": new_path})
            if dry_run:
                print(f"[TEST] {file} → {new_filename}")
            else:
                try:
                    os.rename(old_path, new_path)
                    print(f"[OK] {file} → {new_filename}")
                except Exception as e:
                    print(f"[WARN] Error renaming {file}: {e}")


def cleanup_files(root_dir, opts, dry_run, backup_data):
    trickplay_dirs = []
    for root, dirs, files in os.walk(root_dir, topdown=False):
        if opts.get("DELETE_TRICKPLAY_FOLDERS", False):
            for d in dirs:
                if d.lower().endswith(".trickplay"):
                    trickplay_dirs.append(os.path.join(root, d))
        for f in files:
            fpath = os.path.join(root, f)
            if opts.get("DELETE_NFO", False) and f.lower().endswith(".nfo"):
                delete_file(fpath, dry_run, backup_data)
            elif opts.get("DELETE_JPG", False) and (f.lower().endswith(".jpg") or "-thumb.jpg" in f.lower()):
                delete_file(fpath, dry_run, backup_data)
    if trickplay_dirs:
        print(f"\n🧹 Deleting {len(trickplay_dirs)} trickplay folders...")
        for d in trickplay_dirs:
            if os.path.exists(d):
                unlock_folder(d)
                delete_file(d, dry_run, backup_data)


def restore_from_backup(json_path):
    if not os.path.exists(json_path):
        print("❌ Backup file not found.")
        return
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"🔄 Restoring from backup created on {data.get('created')}...")
    restored = 0
    for item in data.get("files", []):
        if os.path.exists(item["new"]):
            try:
                os.rename(item["new"], item["old"])
                restored += 1
            except Exception as e:
                print(f"[WARN] File restore failed: {e}")
    for item in data.get("folders", []):
        if os.path.exists(item["new"]):
            try:
                os.rename(item["new"], item["old"])
                restored += 1
            except Exception as e:
                print(f"[WARN] Folder restore failed: {e}")
    print(f"✅ Restored {restored} items.")


def main():
    print("🚀 JellyNamer - Smart Episode & Folder Renamer\n")
    print("Select mode:")
    print("1 = Rename / Modify files and folders")
    print("2 = Restore from a backup JSON")
    mode = input("> ").strip()
    if mode == "2":
        json_path = input("💾 Enter path to backup JSON file: ").strip()
        restore_from_backup(json_path)
        return
    elif mode != "1":
        print("⚠️ Invalid selection. Exiting.")
        return
    show_name = input("📺 Enter the show name (e.g., OnePiece, Naruto, etc.): ").strip()
    if not show_name:
        print("⚠️ No show name entered. Aborting.")
        return
    root_dir = input("📁 Enter your media folder path: ").strip()
    if not os.path.exists(root_dir):
        print("❌ Folder not found. Aborting.")
        return
    backup_dir = input("💾 Enter backup folder path (Enter for same as media folder): ").strip() or root_dir
    os.makedirs(backup_dir, exist_ok=True)
    backup_in_dryrun = ask_bool("💾 Create backup file before changes (also in dry-run)?", True)
    dry_run = ask_bool("🔧 Enable DRY_RUN (Preview only)?", True)
    delete_trickplay = ask_bool("🧹 Delete trickplay files?", False)
    show_trickplay = ask_bool("👁️  Show trickplay files in console?", False)
    rename_folders_flag = ask_bool("🗂️  Rename season folders?", False)
    opts = {
        "DELETE_NFO": ask_bool("🗑️  Delete .nfo files?", False),
        "DELETE_JPG": ask_bool("🖼️  Delete .jpg or -thumb.jpg files?", False),
        "DELETE_TRICKPLAY_FOLDERS": ask_bool("🧹  Delete .trickplay folders?", False)
    }
    print("\n⚙️  Configuration Summary:")
    print(f"  Show Name: {show_name}")
    print(f"  Root Folder: {root_dir}")
    print(f"  Backup Folder: {backup_dir}")
    print(f"  DRY_RUN: {dry_run}")
    print(f"  DELETE_TRICKPLAY: {delete_trickplay}")
    print(f"  SHOW_TRICKPLAY: {show_trickplay}")
    print(f"  RENAME_FOLDERS: {rename_folders_flag}")
    for k, v in opts.items():
        print(f"  {k}: {v}")
    print(f"  BACKUP_IN_DRYRUN: {backup_in_dryrun}\n")
    backup_data = {
        "created": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        "root": root_dir,
        "files": [],
        "folders": [],
        "deleted": []
    }
    cleanup_files(root_dir, opts, dry_run, backup_data)
    rename_files(root_dir, show_name, dry_run, delete_trickplay, show_trickplay, backup_data)
    if rename_folders_flag:
        rename_folders(root_dir, dry_run, backup_data)
    if backup_in_dryrun or not dry_run:
        create_backup(backup_dir, backup_data)
    print("\n✅ Done!")


if __name__ == "__main__":
    main()
2