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
