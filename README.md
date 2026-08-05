# Elektroniker Ausbildung

Dokumentation und Übungsaufgaben für die Ausbildung zur **Elektronikerin / zum Elektroniker EFZ** nach der Berufsreform [FutureMEM](https://skills.futuremem.swiss/de/).

- **Hardware** – Entwickeln und Fertigen von elektronischer Hardware
- **Software** – Entwickeln von Software
- **Fertigung** – Fertigen und Montieren
- **Konzepte** – Entwickeln von Ideen und Konzepten

## Was ist dieses Projekt?

Dieses Projekt enthält die **Quellen** (Texte, Aufgaben, Bilder) für eine Webseite. Die fertige Webseite ist hier erreichbar:

👉 **https://elektronik-ausbildung.github.io/**

Der Inhalt ist auf Deutsch und wird laufend ergänzt. Ein Glossar mit allen Abkürzungen ist [als Teil der Webseite](https://elektronik-ausbildung.github.io/glossar.html) verfügbar.

## Für Leser:innen – nur lesen

Ihr braucht **nichts zu installieren**. Öffnet einfach die Webseite:

- [Startseite](https://elektronik-ausbildung.github.io/)
- Dort findet ihr über die Seitenleiste die Kapitel **Hardware**, **Software**, **Fertigung** und **Konzepte**.

Das Projekt ist [auf GitHub](https://github.com/elektronik-ausbildung/elektronik-ausbildung.github.io) Open Source veröffentlicht und steht unter der [Creative-Commons-Lizenz](LICENSE.MD).

## Für Autor:innen – Inhalt beitragen

Möchtet ihr Fehler melden, Inhalte verbessern oder neue Aufgaben beitragen, gibt es mehrere Wege:

1. **Ohne Installation (empfohlen für Einsteiger):** Erstellt auf GitHub ein [Issue](https://github.com/elektronik-ausbildung/elektronik-ausbildung.github.io/issues) oder einen Pull Request direkt im Browser (Stift-Symbol oben rechts in jeder Datei auf GitHub).
2. **Lokal mit VSCode:** Klont das Repository und bearbeitet die Markdown-Dateien (siehe unten).
3. **Per Mail:** Kontakt über die Angaben auf der [Startseite](content/index.md).

### Einrichtung für die lokale Bearbeitung

**Voraussetzungen:**

- [Git](https://git-scm.com/) – zum Herunterladen und Hochladen der Dateien
- [VSCode](https://code.visualstudio.com/) (oder ein anderer Editor)
- [Python](https://www.python.org/) >= 3.10
- [UV](https://docs.astral.sh/uv/) – der Paketmanager, der die Bausteine automatisch installiert

**Schritt für Schritt:**

1. Repository herunterladen:
   ```sh
   git clone https://github.com/elektronik-ausbildung/elektronik-ausbildung.github.io.git
   cd elektronik-ausbildung.github.io
   ```
2. Abhängigkeiten installieren (einmalig):
   ```sh
   uv sync --directory sphinx --group docs
   ```
3. In VSCode öffnen: `code .`
4. In VSCode mit `CTRL+SHIFT+B` bauen: Die Webseite wird erstellt und im Browser geöffnet. Jede Änderung wird so sichtbar.

### Projektstruktur (das Wichtigste)

```
content/     ← Alle Quellen als Markdown (.md), nach Kapiteln sortiert
sphinx/      ← Bausteine (Konfiguration, Abhängigkeiten); bitte nicht ändern
sphinx/build/ ← Erzeugte Webseite (wird automatisch erstellt, nicht ins Repo übernehmen)
```

- Jedes Kapitel (`hardware/`, `software/`, `fertigung/`, `konzepte/`) enthält `theorie/` (Theorie) und `aufgaben/` bzw. `praktika/` (Übungen).
- Neue Aufgaben gehören in `content/<kapitel>/aufgaben/` und müssen zusätzlich in der `index.md` des Kapitels eingetragen werden, damit sie auf der Webseite erscheinen.
- **Wichtig:** Eure Änderungen werden erst online sichtbar, wenn sie auf GitHub (Branch `master`) liegen (siehe unten).

## Für Fortgeschrittene – wie die Webseite entsteht

### Die drei Begriffe kurz erklärt

- **Markdown (.md):** Ein einfaches Textformat für den Inhalt – ihr schreibt ganz normal, mit `#`-Zeichen für Überschriften.
- **Sphinx:** Ein Programm, das aus den Markdown-Dateien eine hübsche Webseite erzeugt. Es ist nur ein Werkzeug, ihr müsst es nicht verstehen, um Inhalte zu bearbeiten.
- **GitHub Pages:** Ein Gratis-Webhosting von GitHub. Sobald ihr Änderungen auf `master` veröffentlicht, baut GitHub die Webseite automatisch neu und stellt sie unter https://elektronik-ausbildung.github.io/ online. Das übernimmt die Datei `.github/workflows/pages.yml` – ihr müsst dort nichts konfigurieren.

### Manuell bauen (ohne VSCode)

```sh
uv sync --directory sphinx --group docs
uv run --directory sphinx sphinx-build -b html -c . ../content build
```

Die fertige Webseite liegt danach in `sphinx/build/`, die Startseite ist `sphinx/build/index.html`.

### Live-Vorschau (Webseite aktualisiert sich automatisch bei Änderungen)

```sh
uv run --directory sphinx sphinx-autobuild -b html -c . ../content build --open-browser
```

### Änderungen veröffentlichen (git)

```sh
git add .
git commit -m "Beschreibung eurer Änderung"
git push origin master
```

Nach dem `push` dauert der automatische Build auf GitHub einige Minuten. Danach ist die Änderung auf der Webseite sichtbar.

## Lizenz

Dieses Projekt steht unter der [Creative Commons Lizenz](LICENSE.MD). Alle Inhalte dürfen frei verwendet und weitergegeben werden, solange die Quelle genannt wird.
