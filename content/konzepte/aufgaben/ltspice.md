# Simulation

In dieser Übung simulierst du mit LTSpice einen invertierenden Verstärker mit Operationsverstärker, erweiterst ihn um eine Tiefpasscharakteristik und überprüfst die Grenzfrequenz per Bode-Diagramm.

Dokumentiere deine Arbeit mit einem Bericht.

- Schwierigkeit: Mittel
- Semester: 4-6
- Material: LTSpice, Computer
- Abgabe: Bericht (PDF oder Markdown) mit Schaltung, Simulationen und Bode-Diagramm

1) Simuliere mit LTSpice einen op-basierten invertierenden Verstärker. Dimensioniere die Verstärkung mit Faktor 100.

2) Mache eine Zeitsimulation und zeige das Ausgangssignal bei einem Eingangssignal von einem 1 kHz, 20 mV Sinus.

3) Baue den Verstärker so um, dass er zusätzlich eine Tiefpasscharakteristik erhält. Dimensioniere die Grenzfrequenz bei 10 kHz.

4) Simuliere einen Frequenz-Sweep und zeichne das Bode-Diagramm der Schaltung auf.

5) Lies die Grenzfrequenz aus dem Bode-Diagramm ab und vergleiche sie mit dem berechneten Wert f = 1/(2πRC).

6) Untersuche die Realität des Operationsverstärkers: Ab welcher Frequenz weicht die Verstärkung von −100 ab? Wie wirkt sich die begrenzte Bandbreite des OpAmp auf das Bode-Diagramm aus?

## Referenzen zum Lehrplan

Die folgenden Leistungskriterien (LK) und Lernziele (LZ) aus dem Bildungsplan FutureMEM stehen in Bezug zu dieser Aufgabe.

- **HKB 9999 b** – Entwickeln und Fertigen von elektronischer Hardware
  - **HK 9999 b.01** – elektronische Schaltungen dimensionieren und das Schema entwickeln
    - **LK ET b1 06** – Sie dimensionieren elektronische Komponenten. (BFS · Semester 1, 2, 3, 4, 5, 8)
      - **LZ_4121** – Sie dimensionieren invertierende und nichtinvertierende Operationsverstärkerschaltungen und berechnen Eingangs- und Ausgangswiderstände. (Semester 4)
      - **LZ_4138** – Sie zeichnen und berechnen RC-Filter (1. Ordnung) mit OPV. (Semester 5)
    - **LK ET b1 07** – Sie erarbeiten klassische Grundschaltungen. (BFS · Semester 1, 2, 3, 4, 5, 8)
      - **LZ_2234** – Sie erklären die entsprechenden Grundschaltungen mit Operationsverstärkern. (Semester 4)
      - **LZ_4117** – Sie zeichnen invertierende und nichtinvertierende Operationsverstärkerschaltungen (inklusive Impedanzwandler) auf und zu benennen. (Semester 4)
      - **LZ_4118** – Sie erklären das Prinzip der Mit- und Gegenkopplung und beschreiben den Einfluss der Gegenkopplung auf die Verstärkung und Bandbreite. (Semester 4)
    - **LK ET b1 08** – Sie simulieren elektronische Schaltungen. (BFS · Semester 1, 2, 3, 4)
      - **LZ_9030** – Sie messen Schaltungen in einem Simulationstool aus. (Semester 1, 4)
      - **LZ_3865** – Sie erklären und berechnen die Periodendauer, die Frequenz, die Amplitude, den Momentanwert, den arithmetischen Mittelwert und den Effektivwert mit Hilfe von Liniendiagrammen. (Semester 4)
      - **LZ_1952** – Sie zeichnen, berechnen und vermessen Serien- und Parallelschaltungen. (Semester 1)
    - **LK ET b1 13** – Sie wenden klassische Grundschaltungen an. (üK · Semester 2, 3)
      - **LZ_4148** – Sie dimensionieren Grundschaltungen mit Feldeffekttransistor, Bipolartransistor, linearem Spannungsregler und Operationsverstärker. (Semester 3)
  - **HK 9999 b.04** – Schaltungen in Betrieb nehmen, ausmessen und Fehler beheben
    - **LK ET b4 08** – Sie stellen die Signalverläufe von klassischen Grundschaltungen grafisch dar. (BFS · Semester 3, 4)
      - **LZ_4024** – Sie berechnen den Amplituden- und Phasengang an passiven Filtern (Hoch- und Tiefpass) und stellen diese im Bodediagramm dar. (Semester 4)
      - **LZ_4136** – Sie ordnen Hoch- und Tiefpassfilter nach ihrer Ordnungszahl ein und zeichnen entsprechende idealisierte Amplitudengänge auf. (Semester 4)
      - **LZ_4008** – Sie beschreiben den Amplitudengang an einem RC-Hochpass und RC-Tiefpass. (Semester 4)
