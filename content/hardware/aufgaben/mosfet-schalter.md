# Messübung Mosfet als Schalter

Ein Mosfet kann als elektronischer Schalter eingesetzt werden. In dieser Übung lernst du seine Funktionsweise und die wichtigsten Kenndaten kennen und entwickelst eine Schaltung, mit der ein 12-V-RGB-LED-Streifen über ein 3.3-V-PWM-Signal eines Mikrocontrollers angesteuert wird.

Erstelle ein Word Dokument zu dieser Übung. Achte beim Messprotokoll darauf, es nach den Anforderungen des üK Zentrums zu führen.

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

## Referenzen zum Lehrplan

Die folgenden Leistungskriterien (LK) und Lernziele (LZ) aus dem Bildungsplan FutureMEM stehen in Bezug zu dieser Aufgabe.

- **HKB 9999 b** – Entwickeln und Fertigen von elektronischer Hardware
  - **HK 9999 b.01** – elektronische Schaltungen dimensionieren und das Schema entwickeln
    - **LK ET b1 06** – Sie dimensionieren elektronische Komponenten. (BFS · Semester 1, 2, 3, 4, 5, 8)
      - **LZ_2011** – Sie beschreiben den Transistor als Schalter in Schaltungen. (Semester 2)
      - **LZ_9035** – Sie wählen passende Leistungshalbleiter wie Thyristor, Triac, Power MOSFET und IGBT's für eine Leistungsendstufe aus. (Semester 8)
      - **LZ_5628** – Sie erklären die grundlegende Funktion und Anwendungen von Z-Dioden, LEDs und Schalttransistoren. (Semester 2)
    - **LK ET b1 07** – Sie erarbeiten klassische Grundschaltungen. (BFS · Semester 1, 2, 3, 4, 5, 8)
      - **LZ_9029** – Sie dimensionieren Grundschaltungen mit Dioden, LEDs, Optokopplern, Feldeffekttransistoren und Bipolartransistoren. (Semester 2)
      - **LZ_4156** – Sie erklären den Begriff elektromagnetische Verträglichkeit (EMV). (Semester 8)
      - **LZ_4193** – Sie beschreiben Methoden der Leistungssteuerung, wie die geschaltete-PWM, Phasenanschnitt- und Phasenabschnittsteuerung. (Semester 8)
    - **LK ET b1 11** – Sie messen die Eigenschaften der elektronischen Komponenten. (üK · Semester 2, 3)
      - **LZ_144** – Sie bauen und überprüfen einfache Schaltungsbeispiele anhand vorgegebener Schemas. (Semester 3, 2)
      - **LZ_126** – Sie messen und berechnen die Leistungen durch Spannungs- und Strommessungen an praktischen Anwendungen. (Semester 2)
      - **LZ_1952** – Sie zeichnen, berechnen und vermessen Serien- und Parallelschaltungen. (Semester 2)
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
    - **LK ET b4 04 (üK)** – Sie messen Schaltungen und achten darauf, deren ursprünglichen Funktion nicht zu beeinflussen. (üK · Semester 2)
      - **LZ_11220** – Sie führen mit geeigneten Messmittel die Messung durch. (Semester 2)
      - **LZ_11224** – Sie benennen Einflussfaktoren von Messmitteln auf das zu messende Bauteil. (Semester 2)
    - **LK ET b4 11** – Sie ermitteln die geeigneten Messgeräte und Hilfsmittel für die durchzuführenden Messungen. (üK · Semester 2, 3)
      - **LZ_10095** – Sie benennen die Fähigkeiten der einzelnen Messmittel und deren Einsatzgrenzen. (Semester 3, 2)
      - **LZ_10096** – Sie kennen die Grundregeln bei der Auswahl eines Messmittels. (Semester 3, 2)
      - **LZ_8263** – Mit standardisierten Messmitteln führen Sie Messungen und Prüfungen durch. (Semester 3)
- **HKB 9999 c** – Entwickeln von Software
  - **HK 9999 c.01** – Mikrocontroller-Programme entwickeln
    - **LK ET c1 16** – Sie setzen verschiedene digitale oder analoge Schnittstellen an beispielhaften Aufgaben ein. (BFS · Semester 6)
      - **LZ_11193** – Sie realisieren Funktionen mit Hilfe von Timern. (Semester 6)
