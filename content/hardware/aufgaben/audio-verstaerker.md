# Schaltungsübung Audioverstärker

Transistoren werden nicht nur als Schalter, sondern auch als Verstärker analoger Signale verwendet. Die bekannteste Anwendung ist der Audioverstärker. Um analoge Verstärkerschaltungen mit Bipolartransistoren zu vertiefen, baust du einen einfachen Audioverstärker der Klasse AB. Ziel ist eine Ausgangsleistung von ca. 4 W an den Lautsprecher.

- Schwierigkeit: Schwer
- Semester: 6–8
- Material: Lautsprecher (4–8 Ω, Belastbarkeit 4–20 W), USB-Audio-Adapter, Steckbrett, Transistoren und weitere Bauteile, 3,5-mm-Audiokabel und Printbuchsen.
- Abgabe: Dokument (PDF) mit Schaltung, Berechnungen und Messungen.

> Der USB-Audio-Adapter schützt den Computer: Sollte bei der Übung ein Fehler passieren, wird der Audio-Ausgang des Rechners nicht beschädigt. Als USB-Audio-Adapter eignet sich zum Beispiel der [Ugreen External Sound Adapter](https://www.galaxus.ch/de/s1/product/ugreen-external-sound-adapter-30724-usb-soundkarte-15664082). Der Lautsprecher kann aus einem beliebigen alten Gerät ausgebaut werden; ansonsten eignet sich zum Beispiel der [AS05208PR-4-R von PUI Audio](https://www.digikey.ch/de/products/detail/pui-audio-inc/AS05208PR-4-R/13165929).

## Recherche

Beantworte folgende Fragen mit Recherche und/oder Messungen:

- Welche Strom- und Spannungspegel liegen am Verstärkereingang (Audio-Ausgang) an?
- Welche Strom- und Spannungspegel müssen am Lautsprecher anliegen, damit dieser mit ca. 4 W tönt?
- Welche Transistorschaltungen gibt es, um Audiosignale zu verstärken? Welche sind für diese Übung geeignet? Begründe die Wahl der Verstärkerklasse.

## Schaltungsentwurf

- Entwirf eine Schaltung, welche den Lautsprecher mit 4 Watt ansteuern kann.
- Wähle und dimensioniere die Bauteile
- Evaluiere die Transistoren für die Endstufe anhand der Datenblätter und begründe deine Wahl
- Simuliere die Schaltung am Computer. Funktioniert die Schaltung wie berechnet? Passe die Bauteile gegebenenfalls an.

## Aufbau

- Baue die Schaltung am Steckbrett auf
- Teste und verbessere die Schaltung, bis sie funktioniert

## Dokumentation

- Dokumentiere die Schaltung und die Berechnungen
- Dokumentiere den Aufbau
- Miss die wichtigsten Signale und weise die Funktion der Schaltung nach
- Beantworte zur Reflexion folgende Fragen:
  - Was hast du gelernt?
  - Wie könnte man die Schaltung weiter verbessern?
  - Was hast du gut gemacht?
  - Was würdest du das nächste Mal anders machen?

```{admonition} Referenzen zum Lehrplan
:class: references
:collapsible: closed

Die folgenden Leistungskriterien (LK) und Lernziele (LZ) aus dem Bildungsplan FutureMEM stehen in Bezug zu dieser Aufgabe.

- **HKB 9999 a** – Entwickeln von Ideen und Konzepten
  - **HK 9999 a.02** – Ideen, Konzepte und Lösungen für elektronische Hard- oder Softwareproblemstellungen entwickeln
    - **LK MEM 08 02** – Sie planen ihre Arbeit unter Einbezug naturwissenschaftlicher Aspekte und führen sie aus. (BFS · Semester 1, 2, 3, 4, 8)
      - **LZ_11345** – Sie erklären den Unterschied zwischen Gleich- und Wechselstrom. (Semester 1)
      - **LZ_11346** – Sie erklären, wie Wechselstrom funktioniert (Sinus, Frequenz). (Semester 1)
- **HKB 9999 b** – Entwickeln und Fertigen von elektronischer Hardware
  - **HK 9999 b.01** – elektronische Schaltungen dimensionieren und das Schema entwickeln
    - **LK ET b1 06** – Sie dimensionieren elektronische Komponenten. (BFS · Semester 1, 2, 3, 4, 5, 8)
      - **LZ_9035** – Sie wählen passende Leistungshalbleiter wie Thyristor, Triac, Power MOSFET und IGBT's für eine Leistungsendstufe aus. (Semester 8)
      - **LZ_5628** – Sie erklären die grundlegende Funktion und Anwendungen von Z-Dioden, LEDs und Schalttransistoren. (Semester 2)
    - **LK ET b1 07** – Sie erarbeiten klassische Grundschaltungen. (BFS · Semester 1, 2, 3, 4, 5, 8)
      - **LZ_2679** – Sie zeigen Anwendungen von Transistorschaltungen auf. (Semester 2)
      - **LZ_9029** – Sie dimensionieren Grundschaltungen mit Dioden, LEDs, Optokopplern, Feldeffekttransistoren und Bipolartransistoren. (Semester 2)
      - **LZ_4112** – Sie berechnen Gleichstromgrössen der Emitterschaltung und beschreiben das Verhalten des Wechselstroms. (Semester 2)
    - **LK ET b1 08** – Sie simulieren elektronische Schaltungen. (BFS · Semester 1, 2, 3, 4)
      - **LZ_9030** – Sie messen Schaltungen in einem Simulationstool aus. (Semester 1, 4)
      - **LZ_3865** – Sie erklären und berechnen die Periodendauer, die Frequenz, die Amplitude, den Momentanwert, den arithmetischen Mittelwert und den Effektivwert mit Hilfe von Liniendiagrammen. (Semester 4)
    - **LK ET b1 11** – Sie messen die Eigenschaften der elektronischen Komponenten. (üK · Semester 2, 3)
      - **LZ_126** – Sie messen und berechnen die Leistungen durch Spannungs- und Strommessungen an praktischen Anwendungen. (Semester 2)
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
    - **LK ET b4 15** – Sie beheben auf logische und strukturierte Weise Störungen an Schaltungen. (üK · Semester 3)
      - **LZ_11218** – Sie erkennen mögliche Ursachen der Abweichung zwischen Soll und Ist. (Semester 3)
      - **LZ_11178** – Sie grenzen Fehler mit den gängigen Messmitteln systematisch so weit wie möglich ein und beheben sie. (Semester 3)
    - **LK ET b4 11** – Sie ermitteln die geeigneten Messgeräte und Hilfsmittel für die durchzuführenden Messungen. (üK · Semester 2, 3)
      - **LZ_10095** – Sie benennen die Fähigkeiten der einzelnen Messmittel und deren Einsatzgrenzen. (Semester 3, 2)
      - **LZ_10096** – Sie kennen die Grundregeln bei der Auswahl eines Messmittels. (Semester 3, 2)
```
