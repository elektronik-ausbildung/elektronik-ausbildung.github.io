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

## Referenzen zum Lehrplan

Die folgenden Leistungskriterien (LK) und Lernziele (LZ) aus dem Bildungsplan FutureMEM stehen in Bezug zu dieser Aufgabe.

- **HKB 9999 a** – Entwickeln von Ideen und Konzepten
  - **HK 9999 a.02** – Ideen, Konzepte und Lösungen für elektronische Hard- oder Softwareproblemstellungen entwickeln
    - **LK MEM 08 02** – Sie planen ihre Arbeit unter Einbezug naturwissenschaftlicher Aspekte und führen sie aus. (BFS · Semester 1, 2, 3, 4, 8)
      - **LZ_11345** – Sie erklären den Unterschied zwischen Gleich- und Wechselstrom. (Semester 1)
      - **LZ_11346** – Sie erklären, wie Wechselstrom funktioniert (Sinus, Frequenz). (Semester 1)
- **HKB 9999 b** – Entwickeln und Fertigen von elektronischer Hardware
  - **HK 9999 b.01** – elektronische Schaltungen dimensionieren und das Schema entwickeln
    - **LK ET b1 06** – Sie dimensionieren elektronische Komponenten. (BFS · Semester 1, 2, 3, 4, 5, 8)
      - **LZ_4123** – Sie dimensionieren den symmetrischen (invertierten und nicht invertierten) Komparator/Schwellwertschalter (Schmitt-Trigger). (Semester 4)
      - **LZ_3966** – Sie beschreiben den Zusammenhang zwischen Ladung, Kapazität, Energie, Spannung, Strom und Zeit und führen Berechnungen durch. (Semester 3)
    - **LK ET b1 07** – Sie erarbeiten klassische Grundschaltungen. (BFS · Semester 1, 2, 3, 4, 5, 8)
      - **LZ_9044** – Sie setzen zeitabhängige Monoflops/ Verzögerungsglieder in Schaltungen ein. (Semester 2)
      - **LZ_9045** – Sie unterscheiden unterschiedliche Arten von Zählerbausteinen und setzen diese in digitalen Schaltungen ein. (Semester 2)
      - **LZ_2052** – Sie beschreiben die Anwendungen des Kondensators, einschliesslich der Zeitverzögerung, Energiespeicherung, Überspannungsschutz, Störschutz und Kompensation. (Semester 3)
  - **HK 9999 b.04** – Schaltungen in Betrieb nehmen, ausmessen und Fehler beheben
    - **LK ET b4 08** – Sie stellen die Signalverläufe von klassischen Grundschaltungen grafisch dar. (BFS · Semester 3, 4)
      - **LZ_3982** – Sie zeichnen das zeitliche Verhalten von Spannungen und Strömen in RC-Schaltungen auf und berechnen die Grössen (e-Funktion). (Semester 3)
      - **LZ_3988** – Sie zeichnen und berechnen die Lade- und Entladefunktion des Kondensators bei konstantem Strom. (Semester 3)
      - **LZ_3994** – Sie zeichnen das Impulsverhalten von RC-Schaltungen auf. (Semester 3)
      - **LZ_1990** – Sie berechnen Lade- und Entladekapazitäten. (Semester 3)
    - **LK ET b4 09** – Sie schätzen den Einfluss von Messgeräten auf Beispielschaltungen ab. (BFS · Semester 1)
      - **LZ_124** – Sie wenden Messgeräte zur Messung von Spannung, Strom und Widerstand an. (Semester 1)
      - **LZ_1948** – Sie führen Strom- und Spannungsmessungen in Stromkreisen durch. (Semester 1)
      - **LZ_1951** – Sie erläutern die Eigenschaften von digitalen und analogen Messgeräten. (Semester 1)
      - **LZ_1993** – Sie erklären den Einfluss des Innenwiderstandes. (Semester 1)
