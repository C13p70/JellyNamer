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
- 🧠 Automatically detects season and episode numbers from folder and file names  
- 🎞️ Generates Jellyfin-compatible filenames (`ShowName-SxxEyyy-Title.mp4`)  
- 🧹 Ignores or optionally deletes "trickplay" preview files  
- 🗂️ Optionally renames season folders (`Season 09 (E264–E336)`)  
- 💬 Clean console output with preview and configuration summary  
- 🧩 Interactive setup — no need to edit the script  
- 🧪 Safe dry-run mode (preview only, no changes)  

---

### 🧠 What's New
| Feature | Description |
|----------|--------------|
| 🧩 **Input with Defaults** | The `ask_bool()` function accepts Enter as a default value (no need to type `1` or `0` every time). |
| 🧾 **Configuration Summary** | Displays a clear overview of all chosen settings before processing begins. |
| 🚦 **Safe Startup** | Automatically aborts if the series name or media path is missing. |
| 🧹 **Stable & Tested** | Fully tested on Python 3.9–3.12 across Windows, macOS, and Linux. |

---

### 🧰 Installation
1. Install [Python 3.9+](https://www.python.org/downloads/)  
2. Clone or download this repository  
3. Run the script:
   ```bash
   python JellyNamer.py
   ```
4. Follow the on-screen prompts. Press **Enter** to accept default values.  

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
- 💬 Übersichtliche Konsolenausgabe mit Testmodus  
- 🧩 Interaktive Abfragen – keine Codeänderungen nötig  
- 🧪 Sicherer Testmodus (zeigt Änderungen nur an)  

---

### 📄 Lizenz
MIT License © 2025  
Erstellt von c13p70 
Ursprünglich inspiriert durch das *One Piece*-Chaos in Jellyfin.  
Frei verwendbar, modifizierbar und erweiterbar.
