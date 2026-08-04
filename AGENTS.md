# Elektroniker Ausbildung – Projektstruktur für AI Agents

## Überblick

Dieses Projekt erstellt eine **Sphinx-Webdokumentation** für die Elektroniker-Ausbildung. Die Quellen sind **Markdown-Dateien** im Ordner `content/`, die mit dem **MyST-Parser** (Markdown für Sphinx) verarbeitet werden. Das Theme ist `pydata_sphinx_theme`.

## Verzeichnisstruktur

```
├── content/                        # 📝 Sämtliche Dokumentationsquellen
│   ├── index.md                    # Root-Toctree (Startseite)
│   ├── glossar.md                  # Glossar (orphan, per Link erreichbar)
│   ├── fertigung/
│   │   ├── index.md                # → Theorie, Praktika
│   │   ├── theorie/
│   │   │   └── index.md            # Löten, PCB, Bestückung, Testen, Montage
│   │   └── praktika/
│   │       ├── index.md            # → smd-bestuecken, tht-bestuecken, prueffeld, mechanik
│   │       ├── smd-bestuecken.md   # ⬜ tbd
│   │       ├── tht-bestuecken.md   # ⬜ tbd
│   │       ├── prueffeld.md        # ⬜ tbd
│   │       └── mechanik.md         # ⬜ tbd
│   ├── hardware/
│   │   ├── index.md                # → Theorie, Aufgaben
│   │   ├── theorie/
│   │   │   └── index.md            # Grundlagen, Bauteile, Messen, Schaltungen, Digitaltechnik
│   │   └── aufgaben/
│   │       ├── index.md            # → 11 Hardware-Aufgaben (Toctree)
│   │       ├── 7-segment.md        # ✅ 7-Segment-Würfelanzeige
│   │       ├── akku-laden.md       # ✅ Akku laden
│   │       ├── diode.md            # ✅ Messübung Diode
│   │       ├── led-ansteuerung.md  # ✅ LED-Ansteuerung
│   │       ├── linearregler.md     # ✅ Linearregler
│   │       ├── mosfet-schalter.md  # ✅ Mosfet als Schalter
│   │       ├── opamp.md            # ✅ OpAmp Stromquelle/Phototransistor
│   │       ├── Photodiode.md       # ✅ Photodioden
│   │       ├── rc-oszillator.md    # ✅ RC-Oszillator
│   │       ├── solarzelle.md       # ✅ Solarzelle
│   │       └── temperatursensor.md # ✅ Temperatursensor
│   ├── konzepte/
│   │   ├── index.md                # → Theorie, Aufgaben
│   │   ├── theorie/
│   │   │   └── index.md            # Pflichtenheft, Anleitung, Messbericht, Git, Simulation
│   │   └── aufgaben/
│   │       ├── index.md            # → git, ltspice, eval
│   │       ├── git.md              # ✅ Git Branching Tutorial
│   │       ├── ltspice.md          # ✅ OpAmp-Simulation mit LTSpice
│   │       └── eval.md             # ⬜ tbd
│   └── software/
│       ├── index.md                # → Theorie, Aufgaben
│       ├── theorie/
│       │   └── index.md            # C, Toolchain, CPU, Peripherie, Code-Struktur
│       └── aufgaben/
│           ├── index.md            # → toolchain, uart, assembler, i2c, repetition-syntax, stm32, netzwerk-praktikum
│           ├── toolchain.md        # ✅ Toolchain recherchieren
│           ├── uart.md             # ✅ UART-Signal mit LA analysieren
│           ├── assembler.md        # ✅ PIC-Assembler Lauflicht
│           ├── i2c.md              # ✅ STM32 + SHT31 I2C-Sensor
│           ├── repetition-syntax.md # ✅ C Repetition Syntax
│           ├── stm32.md            # ✅ Einstieg STM32 DevKit
│           └── netzwerk-praktikum.md # ✅ Netzwerk-Praktikum
├── sphinx/                         # 🏗️ Sphinx-Build-Umgebung
│   ├── conf.py                     # Sphinx-Konfiguration
│   ├── pyproject.toml              # Python-Projekt + UV-Dependencies
│   ├── uv.lock                     # Lockfile
│   └── build/                      # Generierte HTML-Ausgabe (gitignored)
└── .vscode/tasks.json              # VS Code Build-Tasks
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

### Clean-Build (Cache zurücksetzen)
```sh
uv run --directory sphinx sphinx-build -b html -c . ../content build -E
```

Bei Änderungen an `conf.py` reicht ein normaler Build – Sphinx erkennt Config-Änderungen automatisch. Bei seltsamen Seitendarstellungen empfiehlt sich der `-E`-Flag.

### Live-Reload (Entwicklung)
```sh
uv run --directory sphinx sphinx-autobuild -b html -c . ../content build --open-browser
```
In VS Code: `Ctrl+Shift+B` (Default-Task).

## Navigationsstruktur

Die Sidebar wird über Toctrees in den `index.md`-Dateien aufgebaut. Jedes Hauptkapitel (Hardware, Software, Fertigung, Konzepte) enthält Unterkapitel für Theorie und Aufgaben/Praktika.

| Datei | Toctree-Inhalt | `:maxdepth:` |
|---|---|---|
| `content/index.md` (root) | hardware, software, fertigung, konzepte | 1 |
| `content/hardware/index.md` | theorie, aufgaben | 2 |
| `content/software/index.md` | theorie, aufgaben | 2 |
| `content/fertigung/index.md` | theorie, praktika | 2 |
| `content/konzepte/index.md` | theorie, aufgaben | 2 |
| `content/hardware/aufgaben/index.md` | 7-segment, akku-laden, diode, led-ansteuerung, linearregler, mosfet-schalter, opamp, Photodiode, rc-oszillator, solarzelle, temperatursensor | 1 |
| `content/software/aufgaben/index.md` | toolchain, uart, assembler, i2c, repetition-syntax, stm32, netzwerk-praktikum | 1 |
| `content/konzepte/aufgaben/index.md` | git, ltspice, eval | 2 |
| `content/fertigung/praktika/index.md` | smd-bestuecken, tht-bestuecken, prueffeld, mechanik | 2 |

Sphinx-Konfiguration für die Sidebar (`sphinx/conf.py`):
- `navigation_depth: 3` – wie viele Ebenen die Sidebar maximal anzeigt
- `show_nav_level: 2` – wie viele Ebenen standardmäßig aufgeklappt sind

`:maxdepth:` auf einem Toctree begrenzt die Einträge im Sphinx-Toctree-Objekt. Ist der Wert zu niedrig (< 2), werden Unterseiten der Sidebar nicht korrekt angezeigt.

## Wichtige Konventionen

1. **MyST Markdown**: Alle Quelldateien sind `.md` mit MyST-Syntax. Toctrees werden als ```` ```{toctree} ````-Blöcke definiert.

2. **Toctree-Pfade sind relativ zum `content/`-Verzeichnis**:
   ```markdown
   ```{toctree}
   :caption: Hardware
   :maxdepth: 2

   Theorie <theorie/index.md>
   Aufgaben <aufgaben/index.md>
   ```
   ```
   Verweist ein Toctree auf eine nicht-existente Datei, wirft Sphinx nur eine Warning und ignoriert den Eintrag stillschweigend.

3. **`:maxdepth:` richtig setzen**: Für Kapitel mit Unterkapiteln `:maxdepth: 2` verwenden (sonst erscheinen Kindseiten nicht in der Sidebar).

4. **Sprache**: Sämtlicher Content ist Deutsch (Zielgruppe: deutschsprachige Elektronik-Azubis).

5. **Glossar**: `content/glossar.md` ist ein `orphan`-Dokument (nicht im Toctree). Es wird per Link von der Startseite aus erreicht. Neue Abkürzungen in der `{glossary}`-Liste ergänzen.

6. **Jedes Kapitel hat `theorie/` und `aufgaben/`** (bzw. `praktika/` bei Fertigung). Theorie-Seiten enthalten Gliederungen/Inhalte, Aufgaben-Seiten enthalten praktische Übungen.

## Sphinx-Konfiguration (conf.py)

- Extensions: `myst_parser` (für Markdown)
- Theme: `pydata_sphinx_theme`
- Suffixe: `.rst` und `.md`
- `navigation_depth: 3`, `show_nav_level: 2`
- Excluded: `_build`, `Thumbs.db`, `.DS_Store`

## Zielgruppe: Elektroniker/in EFZ (FutureMEM)

Die Dokumentation richtet sich an **Lernende der 4-jährigen Grundbildung Elektroniker/in EFZ** nach der MEM-Berufsreform FutureMEM. Die Ausbildung erfolgt an drei **Lernorten**:

| Lernort | Kürzel | Beitrag |
|---|---|---|
| Lehrbetrieb | BE | Praktische Fertigkeiten im Berufsalltag |
| Berufsfachschule | BFS | Theoretische Grundbildung (Unterricht in Berufskenntnissen, Allgemeinbildung, Sport) |
| Überbetrieblicher Kurs | ÜK | Grundlegende Fertigkeiten, ergänzend zu Betrieb und Schule |

Die Lernenden absolvieren **8 Semester** und schliessen mit dem **eidgenössischen Fähigkeitszeugnis (EFZ)** ab.

### Arbeitsgebiet

Elektroniker/innen EFZ sind Spezialisten für elektronische Schaltungen mit den entsprechenden Softwarelösungen. Sie sind in Hightech-Unternehmen tätig und entwickeln/realisieren elektronische Hard- und Softwarelösungen. Ihre speziellen Kompetenzen liegen in:

- Schaltungsentwicklung
- Mikrocontroller-Technik und Programmierung
- Mess- und Prüftechnik
- Herstellung von Elektronikprodukten (Bestückung, Montage, Prototypen)

### Handlungskompetenzbereiche (HKB a–d)

Der Beruf ET (Elektroniker/in) gliedert sich in 4 Handlungskompetenzbereiche:

| HKB | Bezeichnung | Kapitel |
|---|---|---|
| a | Entwickeln von Ideen und Konzepten | Konzepte |
| b | Entwickeln und Fertigen von elektronischer Hardware | Hardware + Fertigung |
| c | Entwickeln von Software | Software |
| d | Übernehmen von technischer und betrieblicher Verantwortung | Konzepte |

### Kognitive Anforderungsstufen (Lernziele K1–K6)

Jedes Lernziel ist einer kognitiven Stufe zugeordnet:

| Stufe | Name | Beschreibung |
|---|---|---|
| K1 | Wissen | Gelerntes Wissen wiedergeben |
| K2 | Verstehen | Wissen in eigenen Worten erklären |
| K3 | Anwenden | Technologien/Fertigkeiten in verschiedenen Situationen anwenden |
| K4 | Analyse | Komplexe Situationen analysieren und Strukturmerkmale erkennen |
| K5 | Synthese | Einzelne Elemente zu einem Ganzen zusammenfügen |
| K6 | Beurteilen | Sachverhalte aufgrund von Kriterien beurteilen |

### Leistungsniveaus (LN 1–6)

Leistungskriterien werden in 6 Leistungsniveaus eingeteilt:

| LN | Beschreibung |
|---|---|
| 1 | Anwenden von Technologien, Instrumenten, Prozeduren nach Anleitung |
| 2 | Anpassen der Anwendung bei Abweichungen (adaptives Verhalten) |
| 3 | Aufträge selbstständig ausführen |
| 4 | Planen, berechnen – neue Vorhaben mit Unbekannten |
| 5 | Entwerfen, konzipieren, entwickeln oder optimieren von Lösungen |
| 6 | Innovationen und kreative Lösungen gestalten, erfinden |

### Hierarchie des Bildungsplans

```
HKB (Handlungskompetenzbereich, a–d, 4 Stück)
  └─ HK (Handlungskompetenz, z. B. "Mikrocontroller-Programme entwickeln", NQR 2–5)
       └─ LK (Leistungskriterien, pro Lernort, LN 1–6, z. B. "ET c1 05")
            └─ LZ (Lernziele, K1–K6)
```

Die **Lernfelder (LFE)** ordnen die Leistungskriterien den Semestern zu. Beispielsweise ist die Handlungskompetenz **9999 c.01** (Mikrocontroller-Programme entwickeln, NQR 4) mit 378 Lektionen an der BFS und 14.5 Tagen in ÜK verortet, verteilt über die Semester 3–8.

## Richtlinien zum Erstellen von Inhalten

### Allgemein

- **Sprache**: Schweizer Hochdeutsch (Zielgruppe: deutschsprachige Elektronik-Azubis). Kein Dialekt.
- **Niveau**: Die Inhalte richten sich an Lernende im 1.–4. Lehrjahr. Einsteigerthemen (K1–K2) in den unteren Semestern, anspruchsvolle Themen (K4–K6) in den oberen Semestern. Alle Inhalte sollten mit wenig Vorwissen verständlich sein.
- **Praxisbezug**: Jedes Thema sollte auf eine konkrete berufliche Handlungssituation bezogen sein. Die Lernenden sollen verstehen, **warum** sie etwas lernen und **wo** sie es im Berufsalltag anwenden.
- **Datenblattarbeit**: Elektroniker/innen arbeiten regelmässig mit technischen Datenblättern (active and passive components, Mikrocontroller, Sensoren etc.). Datenblattbezüge in Aufgaben und Theorie einbauen.
- **Normen**: EN-, IEC- und ISO-Normen sowie branchenspezifische Standards der MEM-Industrie beachten. Schemata normgerecht zeichnen (IEC 60617, EN 61082).

### Theorie-Seiten (`content/<kapitel>/theorie/index.md`)

- Mit `#`-Überschrift beginnen (wird als Seitentitel verwendet).
- Unterüberschriften mit `##`, `###` etc. gliedern.
- Pro Abschnitt: **warum relevant → grundlegendes Prinzip → Beispiel aus der Praxis**.
- Abstrakte Konzepte mit konkreten Elektronik-Beispielen untermauern (z. B. Zustandsautomaten anhand einer Ampelschaltung erklären).
- Falls sinnvoll: `{note}`, `{warning}` oder `{tip}`-Admonitions von MyST verwenden.
- Nicht-physikalische Einheiten vermeiden, SI-Einheiten konsequent verwenden.
- Codeblöcke mit Spracheannotation (`c`, `python`, `bash`) versehen.

### Aufgaben-Seiten (`content/<kapitel>/aufgaben/*.md`)

- Aufbau:
  - Beginnen mit `# <Titel>` (wird als Aufgabenname angezeigt).
  - Es folgt eine Kurze Beschreibung der Aufgabe und Ausgangslage.
  - Es folgt eine Liste mit folgenden Punkten:
    - Schwierigkeit: Leicht / Mittel / Scher
    - Semester: 1-8
    - Material: Liste Kommasepariert
    - Abgabe: Dokument (PDF oder Markdown), ev Quiz-Antworten, Messprotokoll, Schaltung, PCB, Code oder ähnliches
- Aufgaben sind **selbstständig von den Lernenden zu bearbeiten** – der Agent beschreibt nur, was zu tun ist, nicht die Lösung.
- **Typische Aufgabentypen** für Elektroniker/innen:
  - Recherche- und Berichtsaufgaben (z. B. Toolchain recherchieren)
  - Messaufgaben mit Oszilloskop/Logic Analyzer/Multimeter (z. B. UART-Signal analysieren)
  - Programmieraufgaben für Mikrocontroller (C/Assembler, z. B. PIC-Assembler Lauflicht)
  - Simulationsaufgaben (LTSpice, z. B. OpAmp-Schaltungen simulieren)
  - Aufbau- und Inbetriebnahme-Aufgaben (z. B. STM32 + SHT31 I2C-Sensor)
  - Fehlersuche in bestehenden Schaltungen oder Code
  - Emebedded C Mikrokontroller Code Aufgaben
- Aufgaben sollten sich auf die **Leistungskriterien (LK)** des Bildungsplans beziehen – möglichst unter Angabe der HK-Nummer (z. B. `9999 c.01` für Mikrocontroller-Programmierung).
- **Geräte/Materialien** präzise benennen (z. B. "PIC Board 7 aus dem ÜK", "STM32 Devkit", "USB-Serial Wandler").
- Optional mit nummerierten Schritten (`1)`, `2)`, …) strukturieren.
- Optional: verlangen, dass Ergebnisse in einem kurzen Bericht dokumentiert werden.

## Content-Struktur im Detail

| Pfad | Inhalt | Status |
|---|---|---|
| `index.md` | Root-Toctree + FutureMEM-Erklärung | ✅ Fertig |
| `glossar.md` | Abkürzungsverzeichnis | ✅ Fertig |
| `fertigung/index.md` | Fertigung Toctree | ✅ Fertig |
| `fertigung/theorie/index.md` | Löten, PCB, Bestückung, Testen, Montage | ⬜ Nur Gliederung |
| `fertigung/praktika/index.md` | Praktika Toctree | ✅ Fertig |
| `fertigung/praktika/*.md` | Praktikumsbeschreibungen | ⬜ tbd |
| `hardware/index.md` | Hardware Toctree | ✅ Fertig |
| `hardware/theorie/index.md` | Grundlagen, Bauteile, Messen, Schaltungen, Digitaltechnik | ⬜ Nur Gliederung |
| `hardware/aufgaben/index.md` | Hardware-Aufgaben Toctree | ✅ 11 Aufgaben |
| `hardware/aufgaben/*.md` | Hardware-Aufgabenbeschreibungen | ✅ Ausformuliert |
| `konzepte/index.md` | Konzepte Toctree | ✅ Fertig |
| `konzepte/theorie/index.md` | Pflichtenheft, Anleitung, Messbericht, Git, Simulation | ⬜ Nur Gliederung |
| `konzepte/aufgaben/index.md` | Konzept-Aufgaben Toctree | ✅ Fertig |
| `konzepte/aufgaben/git.md` | Git Branching Tutorial | ✅ Ausformuliert |
| `konzepte/aufgaben/ltspice.md` | OpAmp-Simulation | ✅ Ausformuliert |
| `konzepte/aufgaben/eval.md` | Evaluieren | ⬜ tbd |
| `software/index.md` | Software Toctree | ✅ Fertig |
| `software/theorie/index.md` | C, Toolchain, CPU, Peripherie, Code-Struktur | ⬜ Nur Gliederung |
| `software/aufgaben/index.md` | Aufgaben Toctree | ✅ Fertig |
| `software/aufgaben/*.md` | Aufgabenbeschreibungen | ✅ Ausformuliert |

## Typische Aufgaben für AI Agents

- **Neue Inhalte schreiben**: `.md`-Dateien in `content/<kapitel>/theorie/` mit MyST-Markdown erstellen oder erweitern. Bestehende Gliederungen (Überschriften) mit Inhalt füllen. Konkrete Elektronik-Beispiele aus dem Berufsalltag verwenden, Bezug zu FutureMEM-Leistungskriterien herstellen.
- **Aufgaben hinzufügen**: Neue `.md` in `content/<kapitel>/aufgaben/` anlegen und im zugehörigen `index.md`-Toctree eintragen. Aufgaben müssen praxisnah, selbstständig lösbar und auf die Lernorte (BE/BFS/ÜK) abgestimmt sein.
- **Toctree pflegen**: Kapitel-Hierarchie in den `index.md`-Dateien anpassen. `:maxdepth:` beachten – für Kapitel mit Unterkapiteln `:maxdepth: 2` setzen.
- **Glossar erweitern**: Neue Abkürzungen in `content/glossar.md` in der `{glossary}`-Liste ergänzen (siehe Zielgruppe oben für alle relevanten Kürzel).
- **Build testen**: `uv run --directory sphinx sphinx-build -b html -c . ../content build` ausführen und auf Warnings/Fehler prüfen. Bei Verdacht auf Stale-Cache `-E` verwenden (`uv run --directory sphinx sphinx-build -b html -c . ../content build -E`).
