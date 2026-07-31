# Messübung Mosfet als Schalter

Dokumentiere diese Aufgabe in einem Bericht. Achte beim Messprotokoll darauf, es nach den Anforderungen des üK Zentrums zu führen. 

## 1. Beantworte folgende Fragen

- Was ist ein Mosfet und wie funktioniert dieser?
- Welche Arten von Mosfet gibt es?
- Was wo liegen die Unterschiede zwischen einem idealen und realen Mosfet?
- Welches ist die gängigsten Mosfet?

> Erkläre detailliert, schreibe mehr als einen Satz pro Frage. Insgesamt (für alle 4 Fragen) solltest du 1-2 Seiten schreiben. Versuche zuerst die Fragen aus dem Kopf zu beantworten, wenn du nicht weiter weist, recherchiere im Internet (oder den Unterlagen der Schule).

## 2. Schaltung entwickeln

Zeichne eine Schaltung welche einen 24V LED-Streifen mit 1A Stromverbrauch schalten und dimmen kann. Es soll ein Mosfet als High-Side Schalter verwendet werden. Wähle und dimensioniere die Bauteile.

- Entwickle eine geeignete Schaltung
  - Zeichne ein mögliches Schema
  - Bestimme die Anforderungen an die Mosfet
    - Welche Werte sind wichtig zum auswählen eine Mosfet?
    - Berechne diese Werte
    - Welchen Typ wählst du? Wieso?

Besprich deine Schaltung und die gewählten Bauteile mit deinem Berufsbildner.

## 3. Schaltung aufbauen

- Schreibe ein Programm für das STM32 Devkit das ein PWM mit einer Frequenz von 2kHz erzeugt. Der Duty Cycle wird über ein Poti eingestellt.
- Baue die Schaltung auf.
- Teste die Schaltung

## 4. Messprotokoll

- Teste die Schaltung
- Miss die Slew-Rate vom 3.3V PWM-Signal und der 24V am LED-Streifen für positive und negative Flanken.
- Miss das Signal am LED-Streifen bei folgenden Duty-Cycles:
  - 0%
  - 5%
  - 30%
  - 60%
  - 95%
  - 100%

## 4. Reflexion

- Wie kann die Schaltung verbessert werden?
- Was hast du gelernt?
- Was hast du gut gemacht?
- Was machst du beim nächsten Mal besser?
