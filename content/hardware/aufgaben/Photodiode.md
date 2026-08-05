# Übung Photodioden

Photodioden wandeln Licht in einen elektrischen Strom um und werden überall dort eingesetzt, wo Helligkeit erfasst werden muss. In dieser Übung beantwortest du zuerst Fragen zur Photodiode und entwickelst danach eine Schaltung, die die Helligkeit einer LED dem Umgebungslicht anpasst.

- Schwierigkeit: Schwer
- Semester: 5-6
- Material: Photodiode, Operationsverstärker, LED, Widerstände, Labornetzteil, Multimeter, Oszilloskop, Steckbrett
- Abgabe: Bericht (PDF oder Markdown) mit Quiz-Antworten und Messbericht

## Quiz

Beantworte folgende Fragen schriftlich (wie an der Abschlussprüfung). Versuche die Fragen mit Hilfe deiner Unterlagen zu beantworten, falls das nicht klappt, kannst du auch im Internet suchen. Richtzeit: 60 min

1. Was ist eine Photodiode?
2. Zeige, wie eine Photodiode normalerweise betrieben wird. Was ist die häufigste Betriebsart für Photodioden?
3. Was ist der Unterschied zwischen Photodiode, Phototransistor und LED?
4. Zähle drei wichtige Kennwerte von Photodioden auf und erkläre deren Bedeutung.
5. In welchen Anwendungen / Geräten werden Photodioden eingesetzt?
6. Wie wird Helligkeit gemessen? Welche Einheiten werden verwendet?
7. Wie hell ist es am Tag? Wie hell in der Nacht (z. B. Mondschein)?
8. Erkläre das für den Menschen sichtbare Lichtspektrum.
9. Für welche Bereiche des Lichtspektrums werden Photodioden typischerweise verwendet?

## Schaltung

Löse folgende Aufgabe und dokumentiere sie mit einem Bericht:

LED werden fast überall als Indikatoren verwendet. Fast jedes Gerät hat eine LED, die anzeigt, ob das Gerät gerade läuft. Die Helligkeit dieser LED ist aber immer gleich. So kommt es oft vor, dass man das Leuchten der LED am Tag fast nicht sieht, sie in der Nacht aber viel zu hell ist.

Entwickle eine Schaltung, welche die Helligkeit einer LED dem Umgebungslicht anpasst. Wenn es hell ist (Tag), soll die LED hell leuchten, wenn es dunkel ist (Nacht), soll sie schwach leuchten. Verwende eine Photodiode und einen Operationsverstärker.

1. Zeichne und berechne die Schaltung.
   1. Wie wählst du den OP aus? Worauf ist zu achten?
   2. Schätze die Beleuchtungsstärke in Lux für «Tag» und «Nacht» ab (siehe Quiz, Frage 7) und leite daraus die Dimensionierung der Widerstandswerte ab. Wie viel Strom soll die Photodiode bei welcher Beleuchtungsstärke liefern?
2. Baue die Schaltung auf und überprüfe messtechnisch, ob sie wie geplant funktioniert.
3. Dokumentiere Schaltung und Messung in einem Messbericht.
4. Kannst du die Schaltung so anpassen, dass anstelle der Fotodiode eine LED als Lichtdetektor verwendet werden kann?
5. Miss und vergleiche den Rückwärtsstrom von LED und Photodiode bei unterschiedlichen Helligkeiten. Stelle die beiden Messungen in einem gemeinsamen Diagramm dar und dokumentiere die Ergebnisse.

```{admonition} Referenzen zum Lehrplan
:class: references
:collapsible: closed

Die folgenden Leistungskriterien (LK) und Lernziele (LZ) aus dem Bildungsplan FutureMEM stehen in Bezug zu dieser Aufgabe.

- **HKB 9999 b** – Entwickeln und Fertigen von elektronischer Hardware
  - **HK 9999 b.01** – elektronische Schaltungen dimensionieren und das Schema entwickeln
    - **LK ET b1 06** – Sie dimensionieren elektronische Komponenten. (BFS · Semester 1, 2, 3, 4, 5, 8)
      - **LZ_4108** – Sie interpretieren Kennlinien, Grenz- und Kennwerte von Fotodioden, Fototransistoren, Leuchtdioden und Optokopplern. (Semester 2)
      - **LZ_5628** – Sie erklären die grundlegende Funktion und Anwendungen von Z-Dioden, LEDs und Schalttransistoren. (Semester 2)
      - **LZ_4121** – Sie dimensionieren invertierende und nichtinvertierende Operationsverstärkerschaltungen und berechnen Eingangs- und Ausgangswiderstände. (Semester 4)
    - **LK ET b1 07** – Sie erarbeiten klassische Grundschaltungen. (BFS · Semester 1, 2, 3, 4, 5, 8)
      - **LZ_2234** – Sie erklären die entsprechenden Grundschaltungen mit Operationsverstärkern. (Semester 4)
      - **LZ_4117** – Sie zeichnen invertierende und nichtinvertierende Operationsverstärkerschaltungen (inklusive Impedanzwandler) auf und zu benennen. (Semester 4)
      - **LZ_4118** – Sie erklären das Prinzip der Mit- und Gegenkopplung und beschreiben den Einfluss der Gegenkopplung auf die Verstärkung und Bandbreite. (Semester 4)
      - **LZ_4151** – Sie erläutern das Spektrum elektromagnetischer Wellen. (Semester 8)
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
```
