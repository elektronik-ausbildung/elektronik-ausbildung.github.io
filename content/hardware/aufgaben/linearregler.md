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
