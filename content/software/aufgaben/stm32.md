# Einstieg mit dem STM32 DevKit

In dieser Übung arbeitest du dich Schritt für Schritt in die Entwicklung mit dem STM32 DevKit ein: vom ersten Blinkprogramm über Lauflicht, UART, I2C bis zum Timer. Du benötigst ein [STM32 Moba DevKit](https://github.com/elektronik-ausbildung/STM32-Moba-DevKit).

- Schwierigkeit: Leicht
- Semester: 2-3
- Material: STM32 DevKit, STM32 Cube IDE, Logic Analyzer, Labornetzteil
- Abgabe: Funktionierende Programme mit Nachweis pro Sektion (siehe unten)

> Jede Sektion hat ein klares Nachweis-Kriterium. Lade den Code laufend in dein Git-Repo und zeige das funktinierende Programm deinem Berufsbildner.

## Installation

1. Installiere die Cube IDE
2. Setze das Projekt auf
3. Lasse eine LED blinken

## Lauflicht

1. Baue ein Lauflicht mit den LED
2. Wird ein Taster gedrückt, soll das Lauflicht stoppen und die entsprechende LED leuchten. Wird der Taster losgelassen, blinkt das Lauflicht weiter.
3. Verwende das Potentiometer P0 und den ADC, um die Geschwindigkeit des Lauflichtes einzustellen.

## Blinken

1. Lasse LED0 und LED1 unterschiedlich schnell blinken.
2. Verwende die Potentiometer P0 und P1, um die Blinkgeschwindigkeit der jeweiligen LED einzustellen. Das Blinken der beiden LED soll unabhängig voneinander eingestellt werden können.


## Timer und Interrupts

1. Nimm einen Timer in Betrieb, so dass er alle 100 ms abläuft.
2. Aktiviere den Timer-Interrupt und programmiere ihn so, dass er eine LED toggelt.
3. Ändere das Programm so, dass du mit einem Potentiometer die Timer-Zeit einstellen kannst.
