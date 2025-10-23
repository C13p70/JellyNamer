# 🎬 JellyNamer  
### Smart Episode & Folder Renamer for Jellyfin, Plex & Emby  
*(English + Deutsch)*

---

## 🇬🇧 English

### 📖 Description
**JellyNamer** is a flexible Python script for automatically renaming and organizing TV show episodes for **Jellyfin**, **Plex**, or **Emby**.  

It can also safely back up and restore all file and folder name changes using timestamped JSON backups.  
Additionally, JellyNamer can clean up `.nfo`, `.jpg`, and `.trickplay` files that are no longer needed.

It was originally created to fix the chaotic and irregular season structure of *One Piece*, which Jellyfin couldn’t recognize correctly.  
Manually fixing everything through the metadata manager was so f**$!... — so this tool was born.  

---

### ⚙️ Features
- 🧠 Automatically detects season and episode numbers from folder and file names  
- 💾 Backup & restore system (JSON, timestamped, includes deletions)  
- 🧹 File cleanup for `.nfo`, `.jpg`, and `.trickplay` files  
- 🔓 **Automatically unlocks write-protected `.trickplay` folders before deletion**  
- 🧪 Dry-run mode (preview only)  
- 🧩 Interactive setup (no code editing)  
- 💬 Clear configuration summary before execution  
- 🌍 UTF-8 compatible and cross-platform  
- 💻 Works on Windows, Linux, and macOS  

---

### ⚙️ File Cleanup Options
JellyNamer can optionally remove temporary or redundant media files before or during renaming.  
These deletions are **recorded in the backup JSON** under the `"deleted"` key.

| Option | Description | Default |
|---------|--------------|----------|
| `DELETE_NFO` | Delete `.nfo` metadata files | `False` |
| `DELETE_JPG` | Delete `.jpg` / `-thumb.jpg` thumbnail files | `False` |
| `DELETE_TRICKPLAY_FOLDERS` | Delete `.trickplay` folders (preview cache) | `False` |

🧪 In **DRY_RUN** mode, all deletions are displayed but not performed.

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

### 🛠️ Error Handling Improvements
- More specific exception handling (`PermissionError`, `OSError`)  
- Automatically unlocks read-only `.trickplay` folders before deletion  
- Graceful continuation even when access is denied  
- No more broad “catch-all” exceptions — cleaner, safer, more stable  

---

### 🧾 Backup System
Each rename or deletion is logged inside a timestamped JSON backup:
```json
{
  "created": "2025-10-23T06:22:41",
  "root": "W:/jellyfin/anime/One-Piece-Anime",
  "files": [
    {"old": "...", "new": "..."}
  ],
  "folders": [
    {"old": "...", "new": "..."}
  ],
  "deleted": [
    "W:/.../file_or_folder_removed"
  ]
}
```
You can restore all renames or deletions anytime using **mode 2** in the program menu.

---

### 🧠 Example Use
```bash
python JellyNamer.py
```
Then follow the interactive setup — no config file editing required.

---

### 📄 License
MIT License © 2025  
Created by **c13p70**  
Free to use, modify, and share.

---

## 🇩🇪 Deutsch

### 📖 Beschreibung
**JellyNamer** ist ein flexibles Python-Skript zum automatischen **Umbenennen und Strukturieren von Serienepisoden** für **Jellyfin**, **Plex** oder **Emby**.  

Es kann zudem alle Änderungen mit einem **zeitgestempelten JSON-Backup** sichern und bei Bedarf vollständig wiederherstellen.  
Zusätzlich kann JellyNamer überflüssige `.nfo`, `.jpg` und `.trickplay`-Dateien automatisch bereinigen.

Es entstand ursprünglich, um die völlig unregelmäßigen Staffel- und Episodennamen von *One Piece* zu bereinigen.  
Da Jellyfin diese Strukturen nicht korrekt erkennen konnte und die manuelle Anpassung im Metadaten-Manager extrem f**$!..., wurde dieses Skript entwickelt.  

---

### ⚙️ Funktionen
- 🧠 Automatische Erkennung von Staffel- und Episodennummern  
- 💾 Backup & Restore-System (JSON, mit Zeitstempel, inklusive Löschungen)  
- 🧹 Bereinigung von `.nfo`, `.jpg` und `.trickplay`-Dateien  
- 🔓 **Automatische Entfernung des Schreibschutzes bei `.trickplay`-Ordnern**  
- 🧪 Vorschau-Modus (Dry-Run)  
- 🧩 Interaktive Einrichtung, kein Code-Editieren nötig  
- 💬 Übersichtliche Zusammenfassung vor der Ausführung  
- 🌍 UTF-8-kompatibel und plattformübergreifend  
- 💻 Funktioniert unter Windows, Linux und macOS  

---

### ⚙️ Dateibereinigungs-Optionen
JellyNamer kann optional temporäre oder überflüssige Mediendateien löschen.  
Diese Löschungen werden im Backup-JSON unter `"deleted"` gespeichert.

| Option | Beschreibung | Standard |
|---------|---------------|-----------|
| `DELETE_NFO` | Löscht `.nfo`-Metadaten-Dateien | `False` |
| `DELETE_JPG` | Löscht `.jpg` / `-thumb.jpg` Vorschaubilder | `False` |
| `DELETE_TRICKPLAY_FOLDERS` | Löscht `.trickplay`-Ordner (Vorschaudaten) | `False` |

🧪 Im **Dry-Run-Modus** werden alle Löschungen nur angezeigt, aber nicht ausgeführt.

---

### 🧠 Verbesserte Fehlerbehandlung
- Gezieltes Abfangen von Dateisystemfehlern (`PermissionError`, `OSError`)  
- Automatische Aufhebung des Schreibschutzes vor dem Löschen von `.trickplay`-Ordnern  
- Fortsetzung auch bei fehlenden Berechtigungen  
- Kein Abbruch durch allgemeine Ausnahmen  

---

### 📄 Lizenz
MIT License © 2025  
Erstellt von **c13p70**  
Frei verwendbar, anpassbar und erweiterbar.

---
