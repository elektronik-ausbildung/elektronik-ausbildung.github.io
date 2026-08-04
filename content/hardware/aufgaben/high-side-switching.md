# Messübung Mosfet als High-Side-Schalter

Mosfets werden häufig als Leistungsschalter eingesetzt. Oft muss auch der Plus-Pol einer Last geschaltet werden. Solche High-Side-Schalter untersuchen wir in dieser Übung. Dokumentiere diese Aufgabe in einem Bericht.

- Schwierigkeit: Mittel
- Semester: 4-7
- Material: LED-Streifen weiss (24 V, mindestens 1 A), Mikrocontroller mit PWM-Ausgang (zum Beispiel das [STM32 Moba DevKit](https://github.com/elektronik-ausbildung/STM32-Moba-DevKit)), Mosfet (N- und/oder P-Kanal), Treiber- bzw. Pegelschieberstufe (Transistoren, Widerstände), Labornetzteil, Oszilloskop, Multimeter, Steckbrett
- Abgabe: Dokument (PDF oder Markdown) mit Fragen, Schema, Berechnungen und Messprotokoll

## 1. Repetition Mosfet

Die Grundlagen zum Mosfet hast du in der Aufgabe [Mosfet als Schalter](mosfet-schalter.md) behandelt. Wiederhole sie kurz aus dem Kopf und konzentriere dich danach auf die High-Side-Spezifika. Beantworte schriftlich:

- Was ist ein Mosfet und wie funktioniert dieser?
- Welche Arten von Mosfet gibt es?
- Was ist der Unterschied zwischen einem Low-Side- und einem High-Side-Schalter? Wo liegt die Last bzw. der Schalter in der Versorgungsschiene?
- Welche Vorteile hat ein High-Side-Schalter gegenüber einem Low-Side-Schalter?
- Was wo liegen die Unterschiede zwischen einem idealen und realen Mosfet?

## 2. Schaltung entwickeln

Zeichne eine Schaltung, die einen 24-V-LED-Streifen mit 1 A Stromverbrauch schalten und dimmen kann. Es soll ein Mosfet als High-Side-Schalter verwendet werden. Wähle und dimensioniere die Bauteile.

- Entwickle eine geeignete Schaltung
  - Zeichne ein mögliches Schema inklusive der Ansteuerung des Mosfets durch das 3.3-V-PWM-Signal
  - Bestimme die Anforderungen an den Mosfet
    - Welche Werte sind wichtig zum Auswählen eines Mosfets (U_DS, I_D, R_DS(on), U_GS(th), U_GS max)?
    - Berechne diese Werte
    - Vergleiche N-Kanal- und P-Kanal-Typen aus ihren Datenblättern: Welchen Typ wählst du? Wieso?
  - Berechne die Verlustleistung und die Junction-Temperatur des Mosfets bei 1 A und PWM-Betrieb. Ist ein Kühlkörper nötig?

Besprich deine Schaltung und die gewählten Bauteile mit deinem Berufsbildner, bevor du aufbaust.

## 3. Schaltung aufbauen

- Schreibe ein Programm für das STM32 DevKit, das ein PWM-Signal mit einer Frequenz von 2 kHz erzeugt. Der Duty Cycle wird über ein Poti eingestellt.
- Baue die Schaltung auf dem Steckbrett auf.
- Teste die Schaltung: Kann der LED-Streifen geschaltet und gedimmt werden?

## 4. Messprotokoll

Teste die Schaltung.

- Miss die Slew-Rate des 3.3-V-PWM-Signals und der 24-V-Spannung am LED-Streifen für positive und negative Flanken.
  - Erkläre, wovon die Slew-Rate abhängt und warum sie für EMV und Schaltverluste wichtig ist.
- Miss das Signal am LED-Streifen bei folgenden Duty Cycles: 0 %, 5 %, 30 %, 60 %, 95 %, 100 %.
  - Notiere für jeden Duty Cycle die Spannung U_DS über dem Mosfet und den Strom I. Berechne daraus R_DS(on) = U_DS / I und vergleiche mit dem Datenblattwert.
- Miss U_DS und I durch den Mosfet und berechne die Verlustleistung und die Junction-Temperatur. Vergleiche mit deiner Berechnung aus Abschnitt 2.

## 5. Reflexion

- Wie kann die Schaltung verbessert werden?
- Was hast du gelernt?
- Was hast du gut gemacht?
- Was machst du beim nächsten Mal besser?
