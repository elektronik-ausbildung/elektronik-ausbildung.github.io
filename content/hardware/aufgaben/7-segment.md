# Schaltungsübung 7 Segment Würfelanzeige

Ein elektrischer Würfel zeigt den geworfenen Wert mit LED an. In dieser Übung erweiterst du den Würfel um eine digitale 7-Segment-Anzeige, die den Würfelwert anzeigt.

Nimm einen der [elektrischen Würfel](https://github.com/elektronik-ausbildung/elektronischer-wuerfel/tree/main). Mach dich mit der Schaltung des Würfels vertraut. Erweitere den Würfel so, dass er eine digitale Anzeige erhält.

- Schwierigkeit: Leicht
- Semester: 2-4
- Material: elektrischer Würfel, 7 LED, Widerstände, diverse logische Gatter IC, Binärzähler, Labornetzteil, Steckbrett
- Abgabe: Dokument (PDF oder von Hand) mit Schema, Wahrheitstabellen und Berechnungen

## Aufgabe

1) Baue mit 7 LED eine einstellige 7-Segment-Anzeige.
2) Die 7-Segment-Anzeige soll die Würfelzahl anzeigen. Verwende die Signale des Binärzählers als Eingang für deine Erweiterungen. Berechne die booleschen Verknüpfungen zum Ansteuern der Segmente. Verwende für die Minimierung der Verknüpfungen ein KV-Diagramm pro Segment und dokumentiere die minimierten Terme.
3) Zeichne das Schema der Erweiterung und baue die Schaltung auf.
4) Teste die Schaltung mit vorgegebenen Eingangskombinationen (alle Würfelwerte 1 bis 6). Notiere für jeden Wert, welche Segmente leuchten sollen und welche tatsächlich leuchten. Funktioniert die Schaltung wie du denkst? Falls nicht, ändere die Schaltung, bis sie funktioniert, und dokumentiere den Prozess.

Erstelle ein Dokument (PC oder von Hand), das erklärt, wie deine Schaltung funktioniert. Zeige deine Überlegungen und Berechnungen (z. B. Widerstände, Wahrheitstabellen usw.).

```{admonition} Referenzen zum Lehrplan
:class: references
:collapsible: closed

Die folgenden Leistungskriterien (LK) und Lernziele (LZ) aus dem Bildungsplan FutureMEM stehen in Bezug zu dieser Aufgabe.

- **HKB 9999 a** – Entwickeln von Ideen und Konzepten
  - **HK 9999 a.02** – Ideen, Konzepte und Lösungen für elektronische Hard- oder Softwareproblemstellungen entwickeln
    - **LK MEM 08 03** – Sie wenden bei der Bearbeitung technischer Problemstellungen mathematische Konzepte an. (BFS · Semester 1, 2, 3, 4, 8)
      - **LZ_11357** – Sie berechnen Stromkreise mit dem Ohm’schen Gesetz. (Semester 1)
      - **LZ_11358** – Sie berechnen Strom, Spannung und Widerstände in Serie- und Parallelschaltungen. (Semester 1)
- **HKB 9999 b** – Entwickeln und Fertigen von elektronischer Hardware
  - **HK 9999 b.01** – elektronische Schaltungen dimensionieren und das Schema entwickeln
    - **LK ET b1 07** – Sie erarbeiten klassische Grundschaltungen. (BFS · Semester 1, 2, 3, 4, 5, 8)
      - **LZ_130** – Sie beschreiben die Grundverknüpfungen UND, ODER, NICHT, NAND, NOR und erkennen deren Symbole. (Semester 1)
      - **LZ_4242** – Sie zeichnen Wertetabellen mit Eingangs- und Ausgangsvariablen auf. (Semester 1)
      - **LZ_2224** – Sie entwickeln kombinatorische Schaltungen. (Semester 1)
      - **LZ_2225** – Sie wenden die grundlegenden Gesetze der Schaltalgebra an. (Semester 1)
      - **LZ_2226** – Sie entwerfen und zeichnen logische Signalverknüpfungen. (Semester 1)
      - **LZ_2223** – Sie nennen Beispiele von integrierten Schaltungen wie AND, OR, NOT. (Semester 1)
      - **LZ_29** – Sie unterscheiden logische Grundfunktionen anhand des Symbols, der Wertetabelle, der Funktionsgleichung und des Zeitdiagrammes. (Semester 1)
      - **LZ_27** – Sie stellen den Zusammenhang zwischen einer Funktionsgleichung, einer Wertetabelle und dem Graphen einer Funktion her. (Semester 1)
      - **LZ_9045** – Sie unterscheiden unterschiedliche Arten von Zählerbausteinen und setzen diese in digitalen Schaltungen ein. (Semester 2)
      - **LZ_1899** – Sie unterscheiden und berechnen die Schaltungen von Spannungsteilern und Vorwiderständen. (Semester 1)
    - **LK ET b1 08** – Sie simulieren elektronische Schaltungen. (BFS · Semester 1, 2, 3, 4)
      - **LZ_2227** – Sie analysieren und entwickeln einfache Logikschaltungen. (Semester 1)
      - **LZ_1949** – Sie zeichnen gemischte Schaltungen auf, erklären, berechnen und messen sie aus. (Semester 1, 3, 4, 2)
    - **LK ET b1 10** – Sie zeichnen leserliche Schemas. (BFS · Semester 2)
      - **LZ_9082** – Sie platzieren die Bauteile im Schema so, dass möglichst wenige Kreuzungen der Verbindungen entstehen. (Semester 2)
      - **LZ_9083** – Sie vergeben allen Verbindungen aussagekräftige Netznamen (Labels). (Semester 2)
      - **LZ_9084** – Sie gliedern das Schema in logische Bau- und Funktionsgruppen. (Semester 2)
      - **LZ_9086** – Sie zeichnen die Signallaufrichtung von links nach rechts und von oben nach unten. (Semester 2)
      - **LZ_9087** – Sie versehen das Schema zur besseren Lesbarkeit mit Kommentaren und Berechnungshinweisen. (Semester 2)
      - **LZ_9088** – Bei grösseren Schaltplänen verwenden sie Querverweise (Netznamen, Labels, Ports), um Verbindungen zwischen verschiedenen Seiten oder Bereichen des Schaltplans zu kennzeichnen. (Semester 2)
    - **LK ET b1 09** – Sie setzen für das Schema nach geltenden Normen die richtigen Symbole und Bezeichner ein. (BFS · Semester 2)
      - **LZ_9078** – Sie wenden die korrekten Kennbuchstaben der Betriebsmittel/Bauteile gemäss aktueller Norm an. (Semester 2)
      - **LZ_9085** – Sie achten darauf, dass bei allen Bauteilen der Wert, die Toleranz und gegebenenfalls die genaue Typenbezeichnung ersichtlich ist. (Semester 2)
```
