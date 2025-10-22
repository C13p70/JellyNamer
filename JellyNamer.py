# -*- coding: utf-8 -*-
import os
import re

# === Patterns for folder and episode detection ===
folder_pattern = re.compile(r"S(?P<season>\d+)[ ._-]*E(?P<start>\d+)-E(?P<end>\d+)", re.IGNORECASE)
file_episode_pattern = re.compile(r"(\d{3,4})|E(\d{2,3})", re.IGNORECASE)


def clean_title(name: str) -> str:
    """Cleans the file title by removing numbers, dots, underscores, and redundant info."""
    name = re.sub(r"(^\d+\.?|E\d+\.*)", "", name)
    name = re.sub(r"(?i)one[ ._-]*piece", "", name)
    name = re.sub(r"[._]+", " ", name)
    name = re.sub(r"\s{2,}", " ", name)
    return name.strip(" -_.")


def rename_folders(root_dir: str, show_name: str, dry_run: bool):
    """Renames season folders to 'Season XX (E001-E061)' format."""
    for root, dirs, _ in os.walk(root_dir):
        for d in dirs:
            match = folder_pattern.search(d)
            if not match:
                continue

            season = int(match.group("season"))
            start_ep = match.group("start")
            end_ep = match.group("end")

            new_name = f"Season {season:02d} (E{start_ep}-{end_ep})"
            old_path = os.path.join(root, d)
            new_path = os.path.join(root, new_name)

            if dry_run:
                print(f"📁 (Test) {d} → {new_name}")
            else:
                try:
                    os.rename(old_path, new_path)
                    print(f"✅ Folder renamed: {d} → {new_name}")
                except Exception as e:
                    print(f"⚠️ Error renaming {d}: {e}")


def rename_files(root_dir: str, show_name: str, dry_run: bool,
                 delete_trickplay: bool, show_trickplay: bool):
    """Renames episode files into Jellyfin/Plex/Emby-compatible names."""
    for root, dirs, files in os.walk(root_dir):
        folder_match = folder_pattern.search(root)
        if not folder_match:
            continue

        # Skip trickplay-only folders
        if all("trickplay" in f.lower() for f in files):
            if delete_trickplay:
                for f in files:
                    if "trickplay" in f.lower() and not dry_run:
                        try:
                            os.remove(os.path.join(root, f))
                        except Exception as e:
                            print(f"⚠️ Error deleting {f}: {e}")
            continue

        season = int(folder_match.group("season"))
        start_ep = int(folder_match.group("start"))
        end_ep = int(folder_match.group("end"))
        header_printed = False

        for file in files:
            if "trickplay" in file.lower():
                if show_trickplay:
                    print(f"  ⏭️ Ignored trickplay: {file}")
                if delete_trickplay and not dry_run:
                    try:
                        os.remove(os.path.join(root, file))
                    except Exception as e:
                        print(f"⚠️ Error deleting {file}: {e}")
                continue

            if not file.lower().endswith((".mp4", ".mkv", ".avi")):
                continue

            ep_match = file_episode_pattern.search(file)
            if not ep_match:
                continue

            ep_num = int(ep_match.group(1) or ep_match.group(2))
            if not (start_ep <= ep_num <= end_ep):
                continue

            if not header_printed:
                print(f"\n📂 {root} → Season {season} (Episodes {start_ep}-{end_ep})")
                header_printed = True

            title = clean_title(file)
            new_filename = f"{show_name}-S{season:02d}E{ep_num:03d}-{title}.mp4"
            old_path = os.path.join(root, file)
            new_path = os.path.join(root, new_filename)

            if dry_run:
                print(f"  ➤ {file} → {new_filename}")
            else:
                try:
                    os.rename(old_path, new_path)
                    print(f"  ✅ Renamed: {file} → {new_filename}")
                except Exception as e:
                    print(f"⚠️ Error renaming {file}: {e}")


def ask_bool(prompt: str, default: bool) -> bool:
    """Asks a yes/no question with default fallback (Enter = default)."""
    default_str = "1" if default else "0"
    val = input(f"{prompt} (1=True, 0=False, Enter={default_str}): ").strip()
    if val not in ["0", "1", ""]:
        print("⚠️ Invalid input, using default.")
        return default
    return default if val == "" else val == "1"


def main():
    print("🚀 Starting JellyNamer...\n")

    # === Interactive setup ===
    show_name = input("📺 Enter the show name (e.g., OnePiece, Naruto, etc.): ").strip()
    if not show_name:
        print("⚠️ No show name entered. Aborting.")
        return

    root_dir = input("📁 Enter your media folder path: ").strip()
    if not os.path.exists(root_dir):
        print("❌ Folder not found. Aborting.")
        return

    # Interactive flags (with default fallback)
    dry_run = ask_bool("🔧 Enable DRY_RUN (Preview only)?", True)
    delete_trickplay = ask_bool("🧹 Delete trickplay files?", False)
    show_trickplay = ask_bool("👁️  Show trickplay files in console?", False)
    rename_folders_flag = ask_bool("🗂️  Rename season folders?", False)

    print("\n⚙️  Configuration Summary:")
    print(f"  Show Name:           {show_name}")
    print(f"  Root Folder:         {root_dir}")
    print(f"  DRY_RUN:             {dry_run}")
    print(f"  DELETE_TRICKPLAY:    {delete_trickplay}")
    print(f"  SHOW_TRICKPLAY:      {show_trickplay}")
    print(f"  RENAME_FOLDERS:      {rename_folders_flag}\n")

    rename_files(root_dir, show_name, dry_run, delete_trickplay, show_trickplay)
    if rename_folders_flag:
        print("\n📁 Checking and renaming season folders...")
        rename_folders(root_dir, show_name, dry_run)

    print("\n✅ Done!")


if __name__ == "__main__":
    main()
