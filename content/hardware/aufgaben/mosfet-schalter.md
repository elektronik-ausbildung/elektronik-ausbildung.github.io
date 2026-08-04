# Messübung Mosfet als Schalter

Ein Mosfet kann als elektronischer Schalter eingesetzt werden. In dieser Übung lernst du seine Funktionsweise und die wichtigsten Kenndaten kennen und entwickelst eine Schaltung, mit der ein 12-V-RGB-LED-Streifen über ein 3.3-V-PWM-Signal eines Mikrocontrollers angesteuert wird.

Erstelle ein Word Dokument zu dieser Übung. Word Vorlagen findest du im Laborordner. Achte beim Messprotokoll darauf, es nach den Anforderungen des BBC zu führen. Einzige Ausnahme: Mach das Protokoll digital am Computer.

- Schwierigkeit: Leicht
- Semester: 2-4
- Material: RGB-LED-Streifen (12 V), Mikrocontroller mit PWM-Ausgang (zum Beispiel das [STM32 Moba DevKit](https://github.com/elektronik-ausbildung/STM32-Moba-DevKit)), Mosfet, Labornetzteil, Oszilloskop, Multimeter, Steckbrett
- Abgabe: Dokument (PDF oder Markdown) mit Fragen, Schema, Berechnungen und Messprotokoll

## 1. Beantworte folgende Fragen

- Was ist ein Mosfet und wie funktioniert dieser?
- Welche Arten von Mosfets gibt es?
- Wo liegen die Unterschiede zwischen einem idealen und einem realen Mosfet?
- Welcher Mosfet ist der gängigste?

> Erkläre detailliert, schreibe mehr als einen Satz pro Frage. Insgesamt (für alle 4 Fragen) solltest du 1-2 Seiten schreiben. Versuche zuerst, die Fragen aus dem Kopf zu beantworten. Wenn du nicht weiterweissst, recherchiere im Internet (oder in den Unterlagen der Schule).

## 2. Schaltung entwickeln

Du erhältst einen RGB-LED-Streifen, welcher mit 12 V betrieben wird. Über ein PWM-Signal kann die Helligkeit von jeder Farbe eingestellt werden. Das PWM wird von einem Mikrocontroller generiert und hat einen 3.3-V-Pegel.

Entwirf eine Schaltung, welche es ermöglicht, vom Mikrocontroller aus die Farbe der LED einzustellen.

- Entwickle eine geeignete Schaltung
  - Zeichne ein mögliches Schema
  - Bestimme die Anforderungen an den Mosfet
    - Welche Werte sind wichtig zum Auswählen eines Mosfets?
    - Vergleiche 2–3 Logic-Level-Mosfets anhand ihrer Datenblätter. Stelle die Werte in einer Tabelle gegenüber.
    - Welchen Typ wählst du? Begründe deine Wahl anhand der Daten.

Besprich deine Schaltung und die gewählten Bauteile mit deinem Berufsbildner.

## 3. Schaltung aufbauen

- Schreibe ein Programm für das STM32 Devkit das ein PWM mit einer Frequenz von 2kHz erzeugt. Der Duty Cycle wird über ein Poti eingestellt.
- Baue die Schaltung auf.
- Teste die Schaltung
- Mach ein Messprotokoll und bestimme die wichtigsten Werte
- Wie hoch darf die maximale Schaltfrequenz sein?

Dokumentiere das Messprotokoll gemäss Richtlinien des Kurzentrums

## 4. Reflexion

- Wie kann die Schaltung verbessert werden?
- Was hast du gelernt?
- Was hast du gut gemacht?
- Was machst du beim nächsten Mal besser?
