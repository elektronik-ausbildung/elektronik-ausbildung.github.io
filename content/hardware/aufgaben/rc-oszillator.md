# Schaltungsübung RC Oszillator

Die folgenden Aufgaben sind Übungen zu RC-Oszillatoren und logischen Verknüpfungen. Du entwickelst die Schaltungen selbst: Ein Piezo soll über einen Schmitt-Trigger-Oszillator zum Tönen gebracht werden, die Frequenz wählbar sein und der Ton schliesslich zu einem automatisch ablaufenden Piepton ausgebaut werden.

Du entwickelst die Schaltungen selbst. Versuche dabei, eine Lösung zu finden. Wenn du nicht weiterkommst, frag ungeniert um Hilfe – du bekommst gerne Hinweise, wie die Aufgabe gelöst werden kann.

- Schwierigkeit: Einfach - Mittel
- Semester: 3-4
- Material: passiver Piezo Buzzer, Schmitt-Trigger-Inverter, Potentiometer (2x), Taster, Widerstände, Kondensatoren, Labornetzteil, Oszilloskop, Multimeter, Steckbrett
- Abgabe: Dokument (PDF oder Markdown) mit Schaltung, Dimensionierung und Messungen

> Verifiziere jede Stufe mit einer Tabelle «berechnet vs. gemessen» inklusive Abweichung in Prozent.

1. Bringe einen Piezo mit einem RC Oszillator mit 1 kHz zum tönen.
    Verwende einen Schmitt Trigger RC-Oszillator. Dokumentiere die Schaltung, die Dimensionierung und überprüfe die Berechnung mit einer Messung.

> Es gibt aktive Piezos (mit eingebauter Oszillator-Elektronik, sie tönen bereits bei Gleichspannung) und passive Piezos (ohne Elektronik, sie brauchen ein Wechsel- bzw. Pulssignal). Für diese Übung verwendest du einen **passiven Piezo**. Reicht der Ausgangsstrom des Oszillators nicht aus, um den Piezo hörbar anzutreiben, schalte ihn über einen Transistor.

2. Mache die Frequenz wählbar über ein Poti, es soll von 200Hz bis 5kHz eingestellt werden können
    Dokumentiere die Änderungen an der Schaltung, die Berechnungen und überprüfe die Ergebnisse einer Messung

3. Erweitere die Schaltung so, dass der Piezo nicht dauernd tönt, sondern piept. Die Geschwindigkeit soll ebenfalls über ein Poti eingestellt werden können (0.2 - 10 Hz)
    Dokumentiere die Änderungen an der Schaltung, die Berechnungen und überprüfe die Ergebnisse mit Messungen

4. Erweitere die Schaltung so, dass die Schaltung über einen Taster eingeschaltet wird, 5 mal piept und sich danach selber wieder abschaltet.
    Zeichne zuerst ein Blockdiagramm der Teilfunktionen (Oszillator, Timer, Zähler, Taster) und wie sie zusammenhängen, bevor du die Schaltung entwirfst.
    Dokumentiere die Änderungen an der Schaltung, die Berechnungen und überprüfe die Ergebnisse mit Messungen. Im ausgeschalteten Zustand darf die Schaltung nicht mehr als 10 µA Strom verbrauchen. Hinweis: Wenn du nicht weiterkommst, lass dich von der Ein/Aus-Automatik des elektrischen Würfels inspirieren ([Elektrischer Würfel auf Github](https://github.com/elektronik-ausbildung/elektronischer-wuerfel)).
