# 🎬 JellyNamer  
### Smart Episode & Folder Renamer for Jellyfin, Plex & Emby  
*(English + Deutsch)*

---

## 🇬🇧 English

### 📖 Description
**JellyNamer** is a flexible Python script for automatically renaming and organizing TV show episodes for **Jellyfin**, **Plex**, or **Emby**.  

It can also safely back up and restore all file and folder name changes using timestamped JSON backups.  
Originally created to solve the messy and inconsistent season structures of large shows, it now works for **any** series following a similar folder pattern.

---

### ⚙️ Features
- 🧠 Automatically detects season and episode numbers from folder and file names  
- 💾 Backup & restore system (JSON, timestamped)  
- 🧪 Option to create backups even during dry-run  
- 🧩 Interactive setup — no need to edit the code  
- 🧹 Optionally delete “trickplay” files or rename season folders  
- 💬 Displays a full configuration summary before execution  
- 🌍 UTF-8 compatible and works on Windows, macOS, and Linux  

---

### 🔄 Restore Example
```bash
python JellyNamer.py
```
→ Select option **2 (Restore)**  
Then enter the path to your backup file:
```
💾 Enter path to backup JSON file: D:\Media\ShowName\JellyNamer_backup_2025-10-22_23-14-05.json
```
✅ JellyNamer will automatically restore all files and folders to their original names.

Example backup file (`.json`):
```json
{
  "created": "2025-10-22T23:14:05",
  "root": "D:\\Media\\ShowName",
  "files": [
    {
      "old": "E336.Some.Episode.Name.mp4",
      "new": "ShowName-S09E336-Some Episode Name.mp4"
    }
  ],
  "folders": [
    {
      "old": "Show.S09.E264-E336",
      "new": "Season 09 (E264-E336)"
    }
  ]
}
```

---

### 🧰 Installation
1. Install [Python 3.9+](https://www.python.org/downloads/)  
2. Clone or download this repository  
3. Run the script:
   ```bash
   python JellyNamer.py
   ```
4. Follow the prompts — press **Enter** to use default values.

---

### 🧩 Options
| Option | Description | Default |
|---------|--------------|----------|
| `DRY_RUN` | Preview only (no changes) | `True` |
| `DELETE_TRICKPLAY` | Silently delete trickplay files | `False` |
| `SHOW_TRICKPLAY` | Display trickplay files in console | `False` |
| `RENAME_FOLDERS` | Rename season folders | `False` |
| `BACKUP_IN_DRYRUN` | Create backups even during dry-run | `True` |

---

### 🧠 Technical Details
- Uses regular expressions to detect season/episode ranges  
- Cleans filenames (dots, underscores, numbering, etc.)  
- Creates Jellyfin/Plex/Emby compatible file naming  
- Stores backups as JSON files with timestamped names like:  
  `JellyNamer_backup_2025-10-22_23-14-05.json`

---

### 📄 License
MIT License © 2025  
Created by [Your GitHub Name]  
Originally inspired by complex metadata structures of long-running shows.  
Free to use, modify, and share.

---

## 🇩🇪 Deutsch

### 📖 Beschreibung
**JellyNamer** ist ein flexibles Python-Skript zum automatischen **Umbenennen und Strukturieren von Serienepisoden** für **Jellyfin**, **Plex** oder **Emby**.  

Es kann außerdem alle Änderungen in einem **zeitgestempelten JSON-Backup** sichern und bei Bedarf vollständig wiederherstellen.  
Ursprünglich entwickelt, um unregelmäßige Staffelstrukturen großer Serien zu korrigieren,  
funktioniert es nun für **jede Serie**, die einem ähnlichen Ordneraufbau folgt.

---

### ⚙️ Funktionen
- 🧠 Erkennt automatisch Staffel- und Episodennummern aus Namen  
- 💾 Backup- & Wiederherstellungssystem (JSON mit Zeitstempel)  
- 🧪 Optionales Backup auch im Testmodus (Dry-Run)  
- 🧩 Interaktive Benutzerführung – keine Codeänderungen nötig  
- 🧹 Optionales Löschen von Trickplay-Dateien oder Umbenennen von Ordnern  
- 💬 Übersichtliche Konfigurationsausgabe vor dem Start  
- 🌍 UTF-8-kompatibel und plattformübergreifend

---

### 🔄 Restore Beispiel
```bash
python JellyNamer.py
```
→ Option **2 (Restore)** wählen  
Dann den Pfad zur Backup-Datei eingeben:
```
💾 Pfad zur Backup-Datei: D:\Media\ShowName\JellyNamer_backup_2025-10-22_23-14-05.json
```
✅ JellyNamer stellt automatisch alle ursprünglichen Datei- und Ordnernamen wieder her.

Beispiel-Backup (`.json`):
```json
{
  "created": "2025-10-22T23:14:05",
  "root": "D:\\Media\\ShowName",
  "files": [
    {
      "old": "E336.Some.Episode.Name.mp4",
      "new": "ShowName-S09E336-Some Episode Name.mp4"
    }
  ],
  "folders": [
    {
      "old": "Show.S09.E264-E336",
      "new": "Season 09 (E264-E336)"
    }
  ]
}
```

---

### 📄 Lizenz
MIT License © 2025  
Erstellt von c13p70  
Ursprünglich inspiriert durch das unübersichtliche Metadaten-Chaos langer Serien.  
Frei verwendbar, anpassbar und erweiterbar.
