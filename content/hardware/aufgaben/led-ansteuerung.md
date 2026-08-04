# Vertiefung LED Ansteuerung

LED sind überall in unserem Alltag. Wenn man eine LED direkt an eine Spannungsquelle anschliesst, geht sie in Flammen auf. Damit LED dauerhaft leuchten, braucht es fast immer eine elektronische Schaltung. In dieser Übung dreht sich alles um die verschiedenen Schaltungen zum Ansteuern von LED. Erstelle ein Dokument zu diesem Auftrag. Schreibe die Lösungen zum Quiz und die Dokumentation der Messungen in dieses Dokument.

- Schwierigkeit: Mittel
- Semester: 4-6
- Material: Mikrocontroller-Board mit PWM-Ausgang (zum Beispiel das [STM32 Moba DevKit](https://github.com/elektronik-ausbildung/STM32-Moba-DevKit)), weisse LED >0.25W, Vorwiderstand und Transistor, Luxmeter, Oszilloskop, Labornetzteil
- Abgabe: Dokument (PDF oder Markdown) mit Quiz-Antworten und Messprotokoll

## Quiz

Recherche im Internet ist erlaubt. Versuche die Fragen genau und ausführlich zu beantworten.

1) Mit welchen Schaltungen können LED angesteuert werden? Zeichne vier gängige Schaltungen, und vergleiche Vor- und Nachteile.
2) Häufig werden LED mit Vorwiderständen angesteuert: Was sind Vor- und Nachteile dieser Variante?
3) Gehen wir davon aus, du willst eine LED Lampe bauen die an 24V läuft und mit Vorwiderständen betrieben wird. Wie sieht deine Schaltung aus und wie wählst du den Vorwiderstand? Wieso sollte der Widerstand nicht zu klein sein?
4) Wieso darf eine LED nicht zu heiss werden?
5) Eine LED Lampe soll die Helligkeit verändern können. Welche zwei Möglichkeiten gibt es, die Helligkeit einer LED einzustellen? Zähle Vor- und Nachteile auf.
6) In welchen Geräten aus deinem Alltag sind LED verbaut? Wie werden diese angesteuert? Beschreibe 4 Beispiele.
7) Wie wird Licht gemessen? Mit welchen Messwerten wird das Licht einer LED spezifiziert?
8) Was sind Lumen, Candela und Lux? Was ist der Unterschied?
9) Was ist Farbtemperatur und was ein CRI Index? Wann sind diese relevant?

## Messübung 1: PWM und Helligkeit

1. Baue die Schaltung auf: Verbinde die LED über einen geeigneten Vorwiderstand mit einem PWM-fähigen Ausgang des Mikrocontroller-Boards.
2. Programmieren: Schreibe ein Programm, das ein PWM-Signal mit einstellbarem Tastgrad (0 %, 25 %, 50 %, 75 %, 100 %) ausgibt.
3. Messung: Positioniere das Luxmeter in einem fixen Abstand (z. B. 10 cm) zur LED. Miss für jeden Tastgrad die Beleuchtungsstärke in Lux. Führe die Messung in einem dunklen Raum durch oder schirme die Messung mit einer Kartonkiste vom Umgebungslicht ab.
4. Dokumentation: Erstelle eine Tabelle (Tastgrad → Lux) und ein Diagramm. Ist der Zusammenhang linear? Begründe.
5. Subjektive Wahrnehmung: Betrachte die LED bei jedem Tastgrad und beurteile die empfundene Helligkeit (z. B. kaum sichtbar, mittel, sehr hell). Trage die Einschätzung in die Tabelle ein. Vergleiche die empfundene Helligkeit mit den gemessenen Lux-Werten: Wirkt der Zusammenhang für das Auge ebenfalls linear? Wo weicht die Wahrnehmung von der Messung ab? Begründe (nicht-lineare Helligkeitswahrnehmung des Auges vs. lineare Messung).

## Messübung 2: Vorwärtsspannung und Temperatur

Achtung: Die LED darf nicht heiss werden. Zwischen den Versuchen mindestens eine Minute abkühlen lassen.

1. Schliesse die LED an das Labornetzteil an, das als Stromquelle arbeitet (Strom auf 90% des erlaubten Stromes einstellen, siehe LED Datenblatt).
2. Miss mit dem Oszilloskop die Vorwärtsspannung (U_F) der LED direkt nach dem Einschalten und zeige auf, wie sich die Spannung verändert.
3. Beobachte: Was passiert mit der Vorwärtsspannung, während die LED wärmer wird? Erkläre, warum dieser Effekt in der Praxis einer LED-Schaltung wichtig ist.
4. Bestimme den Temperaturkoeffizienten numerisch: Miss U_F bei bekannter Temperatur (z. B. Raumtemperatur) und nach dem Erwärmen der LED. Berechne den Temperaturkoeffizienten in mV/K und vergleiche ihn mit dem Wert aus dem LED-Datenblatt.
