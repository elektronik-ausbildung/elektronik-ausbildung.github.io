# Schaltungsübung Temperatursensor

Ein Temperatursensor (LM20, SAP# 102949) soll zusammen mit einer Auswerteschaltung eine einfache Temperaturanzeige mit drei LED ergeben: Eine blaue LED leuchtet unter 20 °C, eine grüne zwischen 20 °C und 25 °C und eine rote über 25 °C.

- Schwierigkeit: Leicht
- Semester: 2-3
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
