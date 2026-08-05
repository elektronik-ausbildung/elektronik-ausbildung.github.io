# Elektroniker Ausbildung

## Dokumentation erstellen

### Voraussetzungen

- [Python](https://python.org) >= 3.10
- [UV](https://docs.astral.sh/uv/)

Alle weiteren Pakete werden automatisch installiert.

### Bearbeiten

Bevorzugt wird die Seite mit VSCode bearbeitet.

In VSCode kann mit der Tastenkombination CTRL+SHIFT+B die Webseite erstellt und geöffnet werden. Funktioniert und getestet unter Windows 11 und WSL Ubuntu.

### Webseite generieren

```sh
uv sync --directory sphinx --group docs
uv run --directory sphinx sphinx-build -b html -c . ../content build
```

Die HTML-Dokumentation liegt anschliessend im Ordner `sphinx/build/`.
Die Startseite ist `sphinx/build/index.html`.
