# Einstieg mit dem STM32 DevKit

Du benötigst ein STM32Devkit.

## Installation

1. Installiere die Cube IDE
2. Setze das Projekt auf
3. Lasse eine LED blinken

## Lauflicht

1. Baue ein Lauflicht mit dem LED
2. Wird ein Taster gedrückt soll das Lauflicht stoppen und die entsprechende LED leuchten. Wird der Taster los gelassen, blinkt das Lauflicht weiter.
3. Verwende P0 und den ADC um die Geschwindigkeit des Lauflichtes ein zu stellen.

## Blinken

1. Lasse LED0 und LED1 unterschiedlich schnell blinken.
2. Verwende P0 und P1 die Blinkgeschwindigkeit der jeweiligen LED einzustellen. Das Blinken der beiden LED soll unabhängig voneinander eingestellt werden können.

## UART

1. Nimm UART in Betrieb, so dass du mit printf über USB Text an den Computer senden kannst
2. Nimm den Logic Analyzer und zeichne eine UART Transaktion auf. Markiere alle wichtigen Eigenschaften der UART Übertragung und zeige wie die Daten übertragen werden.
3. Mach ein Programm das es erlaubt vom Computer ein Befehl über UART zu senden, den ein LED an oder aus schaltet.

## Temperatursensor

1. Nimm I2C in Betrieb
2. Verwende den Temperatursensor um Temperatur und Luftfeuchtigkeit zu messen.
3. Wenn Taster 0 gedrückt wird, soll Temperatur und Luftfeuchtigkeit gemessen und über UART an den PC gesendet werden.

## Timer

1. Nimm einen Timer in Betrieb, so dass er alle 100ms abläuft.
2. Aktiviere den Timer Interrupt und programmiere ihn so, dass er eine LED toggelt.
3. Ändere das Programm so, dass du mit einem Poti die Timer Zeit einstellen kannst.
