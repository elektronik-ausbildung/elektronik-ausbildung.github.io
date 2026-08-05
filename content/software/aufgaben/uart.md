# Aufgabe UART

In dieser Übung liest du eine UART-Übertragung mit einem Logic Analyzer auf und dekodierst sie von Hand. Du lernst dabei, wie einzelne Zeichen bitweise übertragen werden.

- Schwierigkeit: Leicht
- Semester: 3-4
- Material: USB-Serial-Wandler, Logic Analyzer, Computer mit Terminalprogramm, Papier, Bleistift, Lineal
- Abgabe: Ausgewertete Zeichnung mit markierten Bits, Erklärung der Dekodierung und dekodierten Zeichen

Besorge dir einen USB-Serial-Wandler. Zeichne das Signal mit einem Logic Analyzer auf. Bitte einen Arbeitskollegen, 4 Textzeichen zu senden, ohne dir die Buchstaben zu verraten – auch die Baudrate soll er dir nicht verraten.

## Vorgehen

1) Drucke die Aufzeichnung aus
2) Markiere im aufgezeichneten Signal der Zeichens die Start-, Daten- und Stoppbits. Wie erkennst du, welches Bit welches ist?
3) Miss die Dauer eines Bits und berechne daraus die Baudrate (Baud = 1 / Bitdauer). Stelle danach im Terminalprogramm genau diese Baudrate ein.
4) Drucke die aufgezeichnete Sequenz mit Bleistift und Lineal aus und dekodiere die Zeichen. Finde heraus, welche Buchstaben getippt wurden.

## Abgabe

- Die ausgedruckte Sequenz mit markierten Start-, Stopp- und Datenbits.
- Eine kurze Erklärung, wie du die Zeichen dekodiert hast.

```{admonition} Referenzen zum Lehrplan
:class: references
:collapsible: closed

Die folgenden Leistungskriterien (LK) und Lernziele (LZ) aus dem Bildungsplan FutureMEM stehen in Bezug zu dieser Aufgabe.

- **HKB 9999 c** – Entwickeln von Software
  - **HK 9999 c.01** – Mikrocontroller-Programme entwickeln
    - **LK ET c1 12** – Sie wählen für beispielhafte Anwendungen geeignete Mikrocontroller. (BFS · Semester 2)
      - **LZ_11213** – Sie zählen Typen von Schnittstellen in Mikrocontrollern auf und kennen das Einsatzgebiet. (Semester 2)
    - **LK ET c1 16** – Sie setzen verschiedene digitale oder analoge Schnittstellen an beispielhaften Aufgaben ein. (BFS · Semester 6)
      - **LZ_11192** – Sie setzen unterschiedliche serielle Schnittstellen zur Ansteuerung von externer Hardware ein. (Semester 6)
```
