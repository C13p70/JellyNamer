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
- 🧪 Dry-run mode (preview only)  
- 🧩 Interactive setup (no code editing)  
- 💬 Clear configuration summary before execution  
- 🌍 UTF-8 compatible and cross-platform  

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

### 📄 License
MIT License © 2025  
Created by c13p70  
Free to use, modify, and share.

---

## 🇩🇪 Deutsch

### 📖 Beschreibung
**JellyNamer** ist ein flexibles Python-Skript zum automatischen **Umbenennen und Strukturieren von Serienepisoden** für **Jellyfin**, **Plex** oder **Emby**.  

Es kann zudem alle Änderungen mit einem **zeitgestempelten JSON-Backup** sichern und bei Bedarf vollständig wiederherstellen.  
Zusätzlich kann JellyNamer überflüssige `.nfo`, `.jpg` und `.trickplay`-Dateien automatisch bereinigen.

s entstand ursprünglich, um die völlig unregelmäßigen Staffel- und Episodennamen von *One Piece* zu bereinigen.  
Da Jellyfin diese Strukturen nicht korrekt erkennen konnte und die manuelle Anpassung im Metadaten-Manager extrem f**$!..., wurde dieses Skript entwickelt.  

---

### ⚙️ Dateibereinigungs-Optionen
JellyNamer kann optional temporäre oder überflüssige Mediendateien löschen.  
Diese Löschungen werden im Backup-JSON unter `"deleted"` gespeichert.

| Option | Beschreibung | Standard |
|---------|---------------|-----------|
| `DELETE_NFO` | Löscht `.nfo`-Metadaten-Dateien | `False` |
| `DELETE_JPG` | Löscht `.jpg` / `-thumb.jpg` Vorschaubilder | `False` |
| `DELETE_TRICKPLAY_FOLDERS` | Löscht `.trickplay`-Ordner (Vorschaubilder) | `False` |

🧪 Im **Dry-Run-Modus** werden alle Löschungen nur angezeigt, aber nicht ausgeführt.

---

### 📄 Lizenz
MIT License © 2025  
Erstellt von c13p70 
Frei verwendbar,anpassbar und erweiterbar.
