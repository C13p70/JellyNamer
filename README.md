# 🎬 JellyNamer  
### Smart Episode & Folder Renamer for Jellyfin, Plex & Emby  
*(English + Deutsch)*

---

## 🇬🇧 English

### 📖 Description
**JellyNamer** is a powerful and flexible Python script for automatically renaming and organizing TV show episodes for **Jellyfin**, **Plex**, or **Emby**.  

It was originally created to fix the chaotic and irregular season structure of *One Piece*, which Jellyfin couldn’t recognize correctly.  
Manually fixing everything through the metadata manager was too time-consuming — so this tool was born.  

Now it can be used for **any series** that follows a similar folder pattern like:  
`S09.E264-E336` → meaning *Season 9, Episodes 264–336.*

---

### ⚙️ Features
- 🧠 Auto-detects season and episode numbers from folders and filenames  
- 🎞️ Creates Jellyfin-compatible filenames (`ShowName-SxxEyyy-Title.mp4`)  
- 🧹 Ignores or deletes "trickplay" preview files  
- 🗂️ Optionally renames season folders (`Season 09 (E264–E336)`)  
- 🧪 Dry-run mode (safe preview without changing files)  
- 💬 Clean console output with optional trickplay visibility  

---

### 📁 Example Output
```
🚀 Starting JellyNamer...

📂 D:\media\anime\S09.E264-E336 → Season 9 (Episodes 264–336)
  ➤ 336.Chopperman.in.Action.mp4 → ShowName-S09E336-Chopperman in Action.mp4

📁 Checking and renaming season folders...
📁 (Test) S09.E264-E336 → Season 09 (E264-E336)

✅ Done!
```

---

### 🧩 Options
| Variable | Description | Default |
|-----------|--------------|----------|
| `DRY_RUN` | Preview only (no changes) | `True` |
| `DELETE_TRICKPLAY` | Silently delete trickplay files | `False` |
| `SHOW_TRICKPLAY` | Display trickplay files in console | `False` |
| `RENAME_FOLDERS` | Rename season folders | `False` |

---

### 🧰 Installation
1. Install [Python 3.9+](https://www.python.org/downloads/)  
2. Clone or download this repository  
3. Adjust your root directory in the script:  
   ```python
   ROOT_DIR = r"C:\path\to\your\media"
   ```
4. Run the script in dry-run mode (default):  
   ```bash
   python JellyNamer.py
   ```

---

## 🇩🇪 Deutsch

### 📖 Beschreibung
**JellyNamer** ist ein flexibles Python-Skript zum automatischen **Umbenennen und Strukturieren von Serienepisoden** für **Jellyfin**, **Plex** oder **Emby**.  

Es entstand ursprünglich, um die völlig unregelmäßigen Staffel- und Episodennamen von *One Piece* zu bereinigen.  
Da Jellyfin diese Strukturen nicht korrekt erkennen konnte und die manuelle Anpassung im Metadaten-Manager extrem mühsam war, wurde dieses Skript entwickelt.  

Es funktioniert aber auch für **jede andere Serie**, deren Ordner z. B. so aussehen:  
`S09.E264-E336` → Staffel 9, Episoden 264–336.

---

### ⚙️ Funktionen
- 🧠 Automatische Staffel- und Episodenerkennung aus Ordner- und Dateinamen  
- 🎞️ Erstellt Jellyfin-kompatible Namen (`ShowName-SxxEyyy-Titel.mp4`)  
- 🧹 Ignoriert oder löscht Trickplay-Dateien  
- 🗂️ Optionales Umbenennen von Staffelordnern (`Season 09 (E264–E336)`)  
- 🧪 Testmodus (zeigt Änderungen nur an)  
- 💬 Klare Konsolenausgabe ohne unnötige Informationen  

---

### 🧰 Verwendung
1. [Python 3.9+](https://www.python.org/downloads/) installieren  
2. Repository klonen oder herunterladen  
3. Im Skript den Medienpfad anpassen:  
   ```python
   ROOT_DIR = r"C:\path\to\your\media"
   ```
4. Ausführen (Standard ist Testmodus):  
   ```bash
   python JellyNamer.py
   ```

---

### 📄 Lizenz
MIT License © 2025  
Created by C13p70  
Originally inspired by the *One Piece* metadata chaos.  
Free to use, modify, and share.
