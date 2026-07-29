# Elektroniker Ausbildung – Projektstruktur für AI Agents

## Überblick

Dieses Projekt erstellt eine **Sphinx-Webdokumentation** für die Elektroniker-Ausbildung. Die Quellen sind **Markdown-Dateien** im Ordner `content/`, die mit dem **MyST-Parser** (Markdown für Sphinx) verarbeitet werden. Das Theme ist `pydata_sphinx_theme`.

## Verzeichnisstruktur

```
├── content/                  # 📝 Sämtliche Dokumentationsquellen
│   ├── index.md              # Root-Toctree (Startseite)
│   ├── fertigung/
│   │   └── index.md          # Fertigung (PCB, Bestückung, Testing, Montage)
│   ├── hardware/
│   │   └── index.md          # Hardwareentwicklung (Grundlagen, Bauteile, Messen, etc.)
│   ├── konzepte/
│   │   └── konzpete.md       # Konzepte (Pflichtenheft, Git, etc.)
│   └── software/
│       ├── index.md          # Software (C, Toolchain, CPU, Peripherie, Code-Struktur)
│       └── aufgaben/
│           ├── index.md      # leer – Platzhalter
│           ├── toolchain.md  # Aufgabe: Toolchain recherchieren
│           ├── uart.md       # Aufgabe: UART-Signal mit LA analysieren
│           ├── assembler.md  # Aufgabe: PIC-Assembler Lauflicht
│           └── i2c.md        # 
├── sphinx/                   # 🏗️ Sphinx-Build-Umgebung
│   ├── conf.py               # Sphinx-Konfiguration
│   ├── pyproject.toml        # Python-Projekt + UV-Dependencies
│   ├── uv.lock               # Lockfile
│   └── build/                # Generierte HTML-Ausgabe (gitignored)
└── .vscode/tasks.json        # VS Code Build-Tasks
```

## Build-System

### Dependencies installieren

```sh
uv sync --directory sphinx --group docs
```

### Dokumentation bauen

```sh
uv run --directory sphinx sphinx-build -b html -c . ../content build
```

Ergebnis liegt in `sphinx/build/index.html`.

### Live-Reload (Entwicklung)

```sh
uv run --directory sphinx sphinx-autobuild -b html -c . ../content build --open-browser
```

In VS Code: `Ctrl+Shift+B` (Default-Task).

## Wichtige Konventionen

1. **MyST Markdown**: Alle Quelldateien sind `.md` mit MyST-Syntax. Toctrees werden als ```` ```{toctree} ````-Blöcke definiert (siehe `content/index.md`).

2. **Toctree-Pfade sind relativ zum `content/`-Verzeichnis**:

   ```markdown
   ```{toctree}
   :caption: Fachbereiche
   :maxdepth: 1

   Fertigung <fertigung/index.md>
   Hardwareentwicklung <hardware/index.md>
   ```

   ```
   
   Verweist ein Toctree auf eine nicht-existente Datei, wirft Sphinx nur eine Warning und **ignoriert den Eintrag** stillschweigend.

3. **Sprache**: Sämtlicher Content ist **Deutsch** (Zielgruppe: deutschsprachige Elektronik-Azubis).

4. **Aufgaben**: Praxisübungen liegen in `content/software/aufgaben/`. Jede Datei beschreibt eine Aufgabe, die der Azubi selbstständig bearbeiten soll.

5. **`.c`-Datei als Dok**: `software/aufgaben/i2c.c` ist kein C-Code, sondern Markdown – die Dateiendung ist irreführend.

## Content-Struktur im Detail

| Datei | Thema | Status |
| --- | --- | --- |
| `content/index.md` | Root-Toctree (Startseite) | ✅ Fertig |
| `fertigung/index.md` | Fertigung (PCB, Bestückung, etc.) | ⬜ Nur Gliederung |
| `hardware/index.md` | Hardwareentwicklung (Bauteile, Messen, Schaltungen, Digitaltechnik) | ⬜ Nur Gliederung |
| `software/index.md` | Software (C, Peripherie, Code-Struktur) | ⬜ Nur Gliederung |
| `konzepte/konzpete.md` | Konzepte (Pflichtenheft, Git, etc.) | ⬜ Nur Gliederung |
| `software/aufgaben/*.md` | Aufgabenblätter | ✅ Ausformuliert |
| `software/aufgaben/index.md` | Aufgaben-Übersicht | ⬜ Leer |

Die meisten Kapitel existieren bisher nur als **Gliederung** (Überschriften ohne Inhalt). Aufgaben sind vollständig beschrieben.

## Sphinx-Konfiguration (conf.py)

- Extensions: `myst_parser` (für Markdown)
- Theme: `pydata_sphinx_theme`
- Suffixe: `.rst` und `.md`
- Excluded: `_build`, `Thumbs.db`, `.DS_Store`

## Typische Aufgaben für AI Agents

- **Neue Inhalte schreiben**: `.md`-Dateien in `content/` mit MyST-Markdown erstellen oder erweitern. Bestehende Gliederungen (Überschriften) mit Inhalt füllen.
- **Toctree pflegen**: Neue Kapitel in `content/index.md` eintragen.
- **Aufgaben hinzufügen**: Neue `.md`-Datei in `content/software/aufgaben/` anlegen und in dessen `index.md`-Toctree aufnehmen.
- **Build testen**: `uv run --directory sphinx sphinx-build -b html -c . ../content build` ausführen und auf Warnings/Fehler prüfen.
