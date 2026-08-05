# Übung Linearregler

Linearregler erzeugen aus einer höheren Eingangsspannung eine stabile Ausgangsspannung und sind in praktisch jedem elektronischen Gerät zu finden. In dieser Übung beantwortest du Fragen zu Linearreglern, dimensionierst Schaltungen mit dem LM317 und entwickelst einen diskreten Linearregler.

- Schwierigkeit: Mittel
- Semester: 4-5
- Material: LM317, Widerstände, Kondensatoren, Transistoren, Kühlkörper (SAP 104224), Labornetzteil, Multimeter, Steckbrett
- Abgabe: Messbericht (PDF oder Markdown) mit Berechnungen und Messprotokoll

## Quiz

Beantworte folgende Fragen auf Papier. Versuche die Fragen ohne Hilfsmittel zu beantworten. Wenn du nicht weiterweissst, darfst du Hilfsmittel verwenden (Schulunterlagen und Internet).

- Was ist ein Linearregler?
- Wozu werden Linearregler eingesetzt?
- Zähle drei Vorteile von Linearreglern gegenüber Schaltreglern auf.
- Zähle drei Nachteile von Linearreglern gegenüber Schaltreglern auf.
- Zähle 5 wichtige Kennwerte von Linearreglern auf und erkläre sie.
  - Falls nicht bereits erklärt: Was bedeutet der Wert «Line Regulation» und worin unterscheidet er sich von der «Load Regulation»?
- Der LM317 ist ein klassischer Linearregler. Dimensioniere/zeichne eine Spannungsregler-Schaltung mit dem LM317 wie folgt: Eingang 12 V, Ausgang 5 V, Ausgangsstrom 100 mA.
  - Berechne die Junction-Temperatur des LM317 in der gezeichneten Schaltung.
  - Berechne die Junction-Temperatur des LM317, wenn er im TO-220-Gehäuse mit dem Kühlkörper SAP 104224 eingesetzt wird.
- Dimensioniere eine Stromquelle für 20 mA mit dem LM317. Zeichne die Schaltung auf.

## Messübung

Dokumentiere die Messung inklusive deiner Schaltung in einem Messbericht.
Entwickle eine Schaltung für einen diskreten Linearregler (ohne fertiges IC).

- Vin: 8 – 16 V
- Vout: 5 V
- IOut max: 50 mA

Baue die Schaltung auf und überprüfe, ob sie funktioniert. Miss folgende Kennwerte:

- Dropout-Spannung Ud
- Querstrom Iq
- Genauigkeit der Ausgangsspannung
- Line Regulation

## Referenzen zum Lehrplan

Die folgenden Leistungskriterien (LK) und Lernziele (LZ) aus dem Bildungsplan FutureMEM stehen in Bezug zu dieser Aufgabe.

- **HKB 9999 b** – Entwickeln und Fertigen von elektronischer Hardware
  - **HK 9999 b.01** – elektronische Schaltungen dimensionieren und das Schema entwickeln
    - **LK ET b1 07** – Sie erarbeiten klassische Grundschaltungen. (BFS · Semester 1, 2, 3, 4, 5, 8)
      - **LZ_9029** – Sie dimensionieren Grundschaltungen mit Dioden, LEDs, Optokopplern, Feldeffekttransistoren und Bipolartransistoren. (Semester 2)
      - **LZ_9032** – Sie erklären die Funktion von unterschiedlichen Stabilisierungsschaltungen für Spannung und Strom. (Semester 8)
      - **LZ_9033** – Sie unterscheiden verschiedene Arten von Spannungswandlerschaltungen. (Semester 8)
    - **LK ET b1 12** – Sie entnehmen aus technischen Datenblättern die relevanten Eigenschaften von Bauteilen. (üK · Semester 2, 3)
      - **LZ_9062** – Sie suchen aufgrund der Bauteilbezeichnung das vom Hersteller herausgegebene Datenblatt und können damit die grundsätzliche Funktion des Bauteils herleiten. (Semester 3, 2)
    - **LK ET b1 13** – Sie wenden klassische Grundschaltungen an. (üK · Semester 2, 3)
      - **LZ_4148** – Sie dimensionieren Grundschaltungen mit Feldeffekttransistor, Bipolartransistor, linearem Spannungsregler und Operationsverstärker. (Semester 3)
  - **HK 9999 b.04** – Schaltungen in Betrieb nehmen, ausmessen und Fehler beheben
    - **LK ET b4 09** – Sie schätzen den Einfluss von Messgeräten auf Beispielschaltungen ab. (BFS · Semester 1)
      - **LZ_124** – Sie wenden Messgeräte zur Messung von Spannung, Strom und Widerstand an. (Semester 1)
      - **LZ_1948** – Sie führen Strom- und Spannungsmessungen in Stromkreisen durch. (Semester 1)
      - **LZ_1951** – Sie erläutern die Eigenschaften von digitalen und analogen Messgeräten. (Semester 1)
      - **LZ_1993** – Sie erklären den Einfluss des Innenwiderstandes. (Semester 1)
    - **LK ET b4 11** – Sie ermitteln die geeigneten Messgeräte und Hilfsmittel für die durchzuführenden Messungen. (üK · Semester 2, 3)
      - **LZ_10095** – Sie benennen die Fähigkeiten der einzelnen Messmittel und deren Einsatzgrenzen. (Semester 3, 2)
      - **LZ_10096** – Sie kennen die Grundregeln bei der Auswahl eines Messmittels. (Semester 3, 2)
