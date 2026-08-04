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
