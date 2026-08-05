# Schalt- und Messtechnik mit Operationsverstärkern

Mit Operationsverstärkern lassen sich spannungsgesteuerte Stromquellen und lichtabhängige Schaltungen aufbauen. 

Operationsverstärker werden oft verwendet, um schwache Signale von Sensoren zu verstärken. In dieser Übung baust du eine spannungsgesteuerte Stromquelle für eine LED und erweiterst sie anschliessend mit einem Phototransistor.


- Schwierigkeit: Mittel
- Semester: 4-6
- Material: Operationsverstärker, Phototransistor (Everlight PT15-21B, SAP 102922), LED, Widerstände, Labornetzteil, Multimeter, Steckbrett
- Abgabe: Bericht (PDF oder Markdown) mit Schema, Berechnungen und Foto des Aufbaus

## 1. Stromquelle

Baue mit einem OP eine spannungsgesteuerte Stromquelle. Am Eingang liegt eine Spannung von 0–5 V an. Am Ausgang wird eine LED angeschlossen. Je nach Eingangsspannung soll die LED mit 0–20 mA Strom versorgt werden. 0 V entspricht 0 mA, 5 V entspricht 20 mA.

1. Zeichne das Schema der Schaltung
3. Berechne und dimensioniere die Bauteile. Formuliere die Übertragungsfunktion I_out = f(U_in) explizit (0 V → 0 mA, 5 V → 20 mA). Leite daraus die Widerstandswerte ab.
4. Wähle Bauteile aus dem Schubladenstock und baue die Schaltung auf einem Steckbrett auf.

## 2. Phototransistor

Hole am Lager einen Phototransistor (Everlight PT15-21B, SAP 102922).

Studiere das Datenblatt. Wie funktioniert der Phototransistor? Welches sind die wichtigen Kennwerte? Baue den Phototransistor am Eingang der Stromquelle ein. Das Ziel ist, eine dem Umgebungslicht angepasste Leuchtstärke der LED: Die Helligkeit soll reduziert werden, wenn es dunkel ist, so dass die LED im Dunkeln nicht blendet. Wenn es hell ist, soll die LED stärker leuchten, so dass sie gut sichtbar leuchtet.

1. Zeichne das Schema der Schaltung
2. Berechne und dimensioniere die Bauteile
3. Wähle Bauteile aus dem Schubladenstock und baue die Schaltung auf einem Steckbrett auf.

```{admonition} Referenzen zum Lehrplan
:class: references
:collapsible: closed

Die folgenden Leistungskriterien (LK) und Lernziele (LZ) aus dem Bildungsplan FutureMEM stehen in Bezug zu dieser Aufgabe.

- **HKB 9999 b** – Entwickeln und Fertigen von elektronischer Hardware
  - **HK 9999 b.01** – elektronische Schaltungen dimensionieren und das Schema entwickeln
    - **LK ET b1 06** – Sie dimensionieren elektronische Komponenten. (BFS · Semester 1, 2, 3, 4, 5, 8)
      - **LZ_4121** – Sie dimensionieren invertierende und nichtinvertierende Operationsverstärkerschaltungen und berechnen Eingangs- und Ausgangswiderstände. (Semester 4)
      - **LZ_4108** – Sie interpretieren Kennlinien, Grenz- und Kennwerte von Fotodioden, Fototransistoren, Leuchtdioden und Optokopplern. (Semester 2)
    - **LK ET b1 07** – Sie erarbeiten klassische Grundschaltungen. (BFS · Semester 1, 2, 3, 4, 5, 8)
      - **LZ_2234** – Sie erklären die entsprechenden Grundschaltungen mit Operationsverstärkern. (Semester 4)
      - **LZ_4117** – Sie zeichnen invertierende und nichtinvertierende Operationsverstärkerschaltungen (inklusive Impedanzwandler) auf und zu benennen. (Semester 4)
      - **LZ_4118** – Sie erklären das Prinzip der Mit- und Gegenkopplung und beschreiben den Einfluss der Gegenkopplung auf die Verstärkung und Bandbreite. (Semester 4)
    - **LK ET b1 12** – Sie entnehmen aus technischen Datenblättern die relevanten Eigenschaften von Bauteilen. (üK · Semester 2, 3)
      - **LZ_9062** – Sie suchen aufgrund der Bauteilbezeichnung das vom Hersteller herausgegebene Datenblatt und können damit die grundsätzliche Funktion des Bauteils herleiten. (Semester 3, 2)
    - **LK ET b1 13** – Sie wenden klassische Grundschaltungen an. (üK · Semester 2, 3)
      - **LZ_4148** – Sie dimensionieren Grundschaltungen mit Feldeffekttransistor, Bipolartransistor, linearem Spannungsregler und Operationsverstärker. (Semester 3)
  - **HK 9999 b.04** – Schaltungen in Betrieb nehmen, ausmessen und Fehler beheben
    - **LK ET b4 09** – Sie schätzen den Einfluss von Messgeräten auf Beispielschaltungen ab. (BFS · Semester 1)
      - **LZ_124** – Sie wenden Messgeräte zur Messung von Spannung, Strom und Widerstand an. (Semester 1)
      - **LZ_1948** – Sie führen Strom- und Spannungsmessungen in Stromkreisen durch. (Semester 1)
    - **LK ET b4 04 (üK)** – Sie messen Schaltungen und achten darauf, deren ursprünglichen Funktion nicht zu beeinflussen. (üK · Semester 2)
      - **LZ_11220** – Sie führen mit geeigneten Messmittel die Messung durch. (Semester 2)
      - **LZ_11224** – Sie benennen Einflussfaktoren von Messmitteln auf das zu messende Bauteil. (Semester 2)
```
