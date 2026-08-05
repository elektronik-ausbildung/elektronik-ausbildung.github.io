# Aufgabe I2C

In dieser Aufgabe nimmst du das I2C-Interface des STM32 DevKits in Betrieb und liest mit dem Temperatur- und Feuchtigkeitssensor SHT31 von Sensirion Temperatur und Luftfeuchtigkeit aus.

- Schwierigkeit: Einfach
- Semester: 3-4
- Material: STM32 DevKit, SHT31 Sensor, Logic Analyzer, USB-Serial-Wandler, STM32 Cube IDE
- Abgabe: Bericht (PDF oder Markdown) mit Code und Aufzeichnung der I2C-Kommunikation

## Ablauf

1) Studiere das Datenblatt des SHT31 Sensors
2) Nimm das STM32 DevKit und nimm den Temperatur- und Feuchtigkeitssensor SHT31 von Sensirion in Betrieb. Lies Luftfeuchtigkeit und Temperatur aus. Du kannst die STM32 Cube MX Bibliotheken verwenden, sonst aber keine weiteren Bibliotheken – schreibe den Code für den Sensor selbst.
3) Sende die Messwerte per UART an deinen Computer (zum Beispiel 1x pro Sekunde)
4) Zeichne die I2C Kommunikation für eine Messung mit einem Logic Analyzer auf. Markiere Start- und Stop-Bedingung, die 7-bit-Slave-Adresse und die ACK/NACK-Bits.
5) Fehlersuche: Programmiere absichtlich eine falsche Slave-Adresse (z. B. um einen Bit verschoben) und zeichne die Kommunikation erneut auf. Interpretiere das NACK im Logic Analyzer: Woran erkennst du, dass die Kommunikation scheitert, und wie verhält sich der Master?
6) Dokumentiere diese Aufgabe in einem kurzen Bericht.

```{admonition} Referenzen zum Lehrplan
:class: references
:collapsible: closed

Die folgenden Leistungskriterien (LK) und Lernziele (LZ) aus dem Bildungsplan FutureMEM stehen in Bezug zu dieser Aufgabe.

- **HKB 9999 c** – Entwickeln von Software
  - **HK 9999 c.01** – Mikrocontroller-Programme entwickeln
    - **LK ET c1 12** – Sie wählen für beispielhafte Anwendungen geeignete Mikrocontroller. (BFS · Semester 2)
      - **LZ_11213** – Sie zählen Typen von Schnittstellen in Mikrocontrollern auf und kennen das Einsatzgebiet. (Semester 2)
    - **LK ET c1 16** – Sie setzen verschiedene digitale oder analoge Schnittstellen an beispielhaften Aufgaben ein. (BFS · Semester 6)
      - **LZ_11192** – Sie setzen unterschiedliche serielle Schnittstellen zur Ansteuerung von externer Hardware ein. (Semester 6)
    - **LK ET c1 19** – Sie realisieren in den Grundstrukturen eines Mikrocontrollers einfachste Programme. (üK · Semester 4)
      - **LZ_4276** – Sie schreiben einfache Programme (Standardanweisungen). (Semester 4)
      - **LZ_11203** – Sie schreiben verständliche und nachvollziehbare Kommentare im Code. (Semester 4)
      - **LZ_11204** – Sie nutzen die unterstützenden Funktionen einer Entwicklungsumgebung. (Semester 4)
    - **LK ET c1 25** – Sie finden und beheben mit Hilfe der Entwicklungsumgebung Fehler in der Software. (üK · Semester 4)
      - **LZ_9782** – Sie setzen den Compiler zur Fehlersuche ein. (Semester 4)
      - **LZ_11249** – Sie erklären die Fehlermeldungen eines Compilers und kennen die Ursachen der Fehlermeldungen. (Semester 4)
    - **LK ET c1 27** – Sie steuern mit Software-Beispielen im Mikrocontroller integrierte Hardware an. (üK · Semester 4)
      - **LZ_9573** – Sie konsultieren die Dokumentation des Mikrocontrollers und der Peripheriegeräte, um technische Daten zu identifizieren. (Semester 4)
      - **LZ_9572** – Sie programmieren Anwendungen, indem sie Bibliotheken verwenden, ändern oder erstellen. (Semester 4)
    - **LK ET c1 28** – Sie kommunizieren über im Mikrocontroller integrierten Schnittstellen mit externer Hardware. (üK · Semester 4)
      - **LZ_9573** – Sie konsultieren die Dokumentation des Mikrocontrollers und der Peripheriegeräte, um technische Daten zu identifizieren. (Semester 4)
      - **LZ_11255** – Sie nutzen Bibliotheken zur Ansteuerung einer externen Hardware. (Semester 4)
```
