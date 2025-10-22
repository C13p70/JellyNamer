import os
import re

# === CONFIGURATION ===
ROOT_DIR = r"C:\path\to\your\media"  # Main media folder (adjust as needed)

DRY_RUN = True             # True = preview only, False = apply changes
DELETE_TRICKPLAY = False   # True = delete trickplay files silently
SHOW_TRICKPLAY = False     # True = display trickplay files in console output
RENAME_FOLDERS = False     # True = rename season folders
# ======================

# Folder pattern: e.g., "S09.E264-E336"
folder_pattern = re.compile(r"S(?P<season>\d+)\.E(?P<start>\d+)-E(?P<end>\d+)", re.IGNORECASE)
# File pattern: matches "E336" or "336"
file_episode_pattern = re.compile(r"(\d{3,4})|E(\d{2,3})", re.IGNORECASE)

def clean_title(name: str) -> str:
    """Cleans the file title by removing numbers, dots, underscores, and redundant info."""
    name = re.sub(r"(^\d+\.?|E\d+\.*)", "", name)
    name = re.sub(r"(?i)one[ ._-]*piece", "", name)
    name = re.sub(r"[._]+", " ", name)
    name = re.sub(r"\s{2,}", " ", name)
    return name.strip(" -_.")

def rename_folders():
    """Renames season folders to 'Season XX (E001-E061)' format."""
    for root, dirs, _ in os.walk(ROOT_DIR):
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

            if DRY_RUN:
                print(f"📁 (Test) {d} → {new_name}")
            else:
                try:
                    os.rename(old_path, new_path)
                    print(f"✅ Folder renamed: {d} → {new_name}")
                except Exception as e:
                    print(f"⚠️ Error renaming {d}: {e}")

def rename_files():
    """Renames episode files into Jellyfin/Plex/Emby-compatible names."""
    for root, dirs, files in os.walk(ROOT_DIR):
        folder_match = folder_pattern.search(root)
        if not folder_match:
            continue

        # Skip trickplay-only folders
        if all("trickplay" in f.lower() for f in files):
            if DELETE_TRICKPLAY:
                for f in files:
                    if "trickplay" in f.lower() and not DRY_RUN:
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
                if SHOW_TRICKPLAY:
                    print(f"  ⏭️ Ignored trickplay: {file}")
                if DELETE_TRICKPLAY and not DRY_RUN:
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
            new_filename = f"ShowName-S{season:02d}E{ep_num:03d}-{title}.mp4"
            old_path = os.path.join(root, file)
            new_path = os.path.join(root, new_filename)

            if DRY_RUN:
                print(f"  ➤ {file} → {new_filename}")
            else:
                try:
                    os.rename(old_path, new_path)
                    print(f"  ✅ Renamed: {file} → {new_filename}")
                except Exception as e:
                    print(f"  ⚠️ Error renaming {file}: {e}")

def main():
    print("🚀 Starting JellyNamer...
")
    rename_files()
    if RENAME_FOLDERS:
        print("\n📁 Checking and renaming season folders...")
        rename_folders()
    print("\n✅ Done!")

if __name__ == "__main__":
    main()
