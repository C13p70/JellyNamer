# 🎬 JellyNamer  
### Smart Episode & Folder Renamer for Jellyfin, Plex & Emby  
*(English + Deutsch)*

---

## 🇬🇧 English

### 📖 Description
**JellyNamer** is a Python script for automatically renaming and organizing TV show episodes for **Jellyfin**, **Plex**, or **Emby**.  

It can also safely back up and restore all file and folder name changes using timestamped JSON backups.

It was originally created to fix the chaotic and irregular season structure of *One Piece*, which Jellyfin couldn’t recognize correctly.  
Manually fixing everything through the metadata manager was f**$!!..... — so this tool was born.  

---

### ⚙️ Features
- 🧠 Auto-detects seasons and episodes from folder and file names  
- 💾 Backup & restore system (JSON, timestamped)  
- 🧪 Option to back up even in dry-run mode  
- 🧩 Interactive setup (no need to edit code)  
- 🧹 Optional trickplay deletion and folder renaming  
- 💬 Clear configuration summary before execution  
- 🧠 UTF-8 safe and cross-platform compatible  

---

### 🔄 Restore Example
```bash
python JellyNamer.py
```
→ Select option **2 (Restore)**  
Then enter the path to your backup file:
```
💾 Enter path to backup JSON file: W:\jellyfin\anime\One-Piece-Anime\JellyNamer_backup_2025-10-22_23-14-05.json
```
✅ JellyNamer will automatically restore all files and folders to their original names.

Example backup file (`.json`):
```json
{
  "created": "2025-10-22T23:14:05",
  "root": "W:\\jellyfin\\anime\\One-Piece-Anime",
  "files": [
    {
      "old": "336.Chopperman.in.Aktion.HD.720P.x264.by.M3lloW.mp4",
      "new": "OnePiece-S09E336-Chopperman in Aktion HD 720P x264 by M3lloW.mp4"
    }
  ],
  "folders": [
    {
      "old": "One.Piece.S09.E264-E336",
      "new": "Season 09 (E264-E336)"
    }
  ]
}
```

---

## 🇩🇪 Deutsch

### 📖 Beschreibung
**JellyNamer** ist ein flexibles Python-Skript zum automatischen **Umbenennen und Strukturieren von Serienepisoden** für **Jellyfin**, **Plex** oder **Emby**.  

Zusätzlich kann es alle Änderungen mit einem **zeitgestempelten JSON-Backup** sichern und bei Bedarf vollständig wiederherstellen.

Es wurde ursprünglich entwickelt, um die chaotische und unregelmäßige Staffelstruktur von *One Piece* zu korrigieren, die Jellyfin nicht richtig erkennen konnte.  
Alles manuell über den Metadaten-Manager zu korrigieren war f**$!! ... – also wurde dieses Tool entwickelt.  
---

### ⚙️ Funktionen
- 🧠 Erkennt automatisch Staffeln und Episoden aus Ordner- und Dateinamen  
- 💾 Backup- & Wiederherstellungssystem (JSON, mit Zeitstempel)  
- 🧪 Optionales Backup auch im Testmodus (Dry-Run)  
- 🧩 Interaktive Abfragen – keine Codeänderungen nötig  
- 🧹 Optionales Löschen von Trickplay-Dateien und Umbenennen von Staffelordnern  
- 💬 Übersichtliche Konfigurationszusammenfassung vor der Ausführung  
- 🧠 UTF-8-kompatibel und plattformübergreifend  

---

### 🔄 Restore Beispiel
```bash
python JellyNamer.py
```
→ Option **2 (Restore)** wählen  
Dann den Pfad zur Backup-Datei eingeben:
```
💾 Pfad zur Backup-Datei: W:\jellyfin\anime\One-Piece-Anime\JellyNamer_backup_2025-10-22_23-14-05.json
```
✅ JellyNamer stellt automatisch alle ursprünglichen Datei- und Ordnernamen wieder her.

Beispiel-Backupdatei (`.json`):
```json
{
  "created": "2025-10-22T23:14:05",
  "root": "W:\\jellyfin\\anime\\One-Piece-Anime",
  "files": [
    {
      "old": "336.Chopperman.in.Aktion.HD.720P.x264.by.M3lloW.mp4",
      "new": "OnePiece-S09E336-Chopperman in Aktion HD 720P x264 by M3lloW.mp4"
    }
  ],
  "folders": [
    {
      "old": "One.Piece.S09.E264-E336",
      "new": "Season 09 (E264-E336)"
    }
  ]
}
```

---

### 📄 License
MIT License © 2025  
Created by c13P70 
Originally inspired by the *One Piece* metadata chaos.
