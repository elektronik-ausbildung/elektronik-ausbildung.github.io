# Schaltungsübung Temperatursensor

Ein Temperatursensor (LM20, SAP# 102949) soll zusammen mit einer Auswerteschaltung eine einfache Temperaturanzeige mit drei LED ergeben: Eine blaue LED leuchtet unter 20 °C, eine grüne zwischen 20 °C und 25 °C und eine rote über 25 °C.

- Schwierigkeit: Leicht
- Semester: 2-4
- Material: LM20 Temperatursensor (SAP# 102949), 3 LED (blau, grün, rot), diverse Bauteile, Labornetzteil, Multimeter, Steckbrett
- Abgabe: Dokument (PDF oder Markdown) mit Schema, Berechnungen und Aufbau der Schaltung

Arbeite die folgenden Schritte nacheinander ab. Schreibe bei jedem Schritt auf, welche Berechnungen du machst und welche Bauteile du wählst.

## 1. Datenblatt studieren

Lade das Datenblatt des LM20 und beantworte folgende Fragen:

- Wie lautet die Übertragungsfunktion V_out(T) des LM20 (Steigung und Offset)?
- Wie gross ist der Betriebsspannungsbereich des Sensors und in welchem Bereich liegt die Ausgangsspannung?

## 2. Übertragungsfunktion anwenden

- Berechne die Ausgangsspannung des LM20 bei den drei relevanten Temperaturen.
- Wie gross ist der Spannungshub zwischen 20 °C und 25 °C? Was bedeutet das für die Genauigkeit der Auswerteschaltung?

## 3. Schwellwerte festlegen

- Lege fest, welche LED bei welcher Temperatur leuchten soll.
- Wähle die Referenzspannungen, bei denen die Auswerteschaltung umschalten soll, und begründe die Wahl.

## 4. Komparator-Fensterdetektor entwerfen

- Zeichne das Schema der Auswerteschaltung auf Papier.
- Berechne die Vorwiderstände der LED und die Widerstände für die Referenzspannungen.

## 5. Aufbau und Verifikation

Baue die Schaltung auf einem Steckbrett auf.

- Prüfe jede der drei Umschalt-Temperaturen messtechnisch nach: Verändere die Temperatur am Sensor (z. B. Erwärmen mit einer Wärmequelle oder Abkühlen mit Kältespray) und kontrolliere, welche LED leuchtet.
- Vergleiche die gemessenen Umschaltpunkte mit den berechneten Werten und erkläre Abweichungen.

## Bericht

Dokumentiere die Schaltung, deine Berechnungen und den Aufbau in einem kurzen Bericht (PDF oder Markdown).

## Referenzen zum Lehrplan

Die folgenden Leistungskriterien (LK) und Lernziele (LZ) aus dem Bildungsplan FutureMEM stehen in Bezug zu dieser Aufgabe.

- **HKB 9999 a** – Entwickeln von Ideen und Konzepten
  - **HK 9999 a.02** – Ideen, Konzepte und Lösungen für elektronische Hard- oder Softwareproblemstellungen entwickeln
    - **LK MEM 08 02** – Sie planen ihre Arbeit unter Einbezug naturwissenschaftlicher Aspekte und führen sie aus. (BFS · Semester 1, 2, 3, 4, 8)
      - **LZ_9512** – Sie rechnen die Temperaturskalen Celsius und Kelvin um. (Semester 4)
      - **LZ_9515** – Sie zählen verschiedene Temperaturmessgeräte auf. (Semester 4)
      - **LZ_9516** – Sie beschreiben Temperaturmessgeräte den Anforderungen entsprechend. (Semester 4)
- **HKB 9999 b** – Entwickeln und Fertigen von elektronischer Hardware
  - **HK 9999 b.01** – elektronische Schaltungen dimensionieren und das Schema entwickeln
    - **LK ET b1 06** – Sie dimensionieren elektronische Komponenten. (BFS · Semester 1, 2, 3, 4, 5, 8)
      - **LZ_4123** – Sie dimensionieren den symmetrischen (invertierten und nicht invertierten) Komparator/Schwellwertschalter (Schmitt-Trigger). (Semester 4)
      - **LZ_4121** – Sie dimensionieren invertierende und nichtinvertierende Operationsverstärkerschaltungen und berechnen Eingangs- und Ausgangswiderstände. (Semester 4)
      - **LZ_5628** – Sie erklären die grundlegende Funktion und Anwendungen von Z-Dioden, LEDs und Schalttransistoren. (Semester 2)
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
      - **LZ_1993** – Sie erklären den Einfluss des Innenwiderstandes. (Semester 1)
