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

```{admonition} Referenzen zum Lehrplan
:class: references
:collapsible: closed

Die folgenden Leistungskriterien (LK) und Lernziele (LZ) aus dem Bildungsplan FutureMEM stehen in Bezug zu dieser Aufgabe.

- **HKB 9999 a** – Entwickeln von Ideen und Konzepten
  - **HK 9999 a.03** – die Machbarkeit von Ideen oder Aufträgen für elektronische Hard- oder Softwarelösungen abklären
    - **LK MEM 07 14** – Sie setzen ausgewählte Standardapplikationen und industrieübliche Software effektiv und effizient ein. (üK · Semester 4)
      - **LZ_11240** – Sie benennen den Funktionsumfang und Nutzen einer Entwicklungsumgebung. (Semester 4)
      - **LZ_11241** – Sie entwickeln in einer Entwicklungsumgebung Software für einen Mikrocontroller. (Semester 4)
      - **LZ_11242** – Sie nutzen Bibliotheken. (Semester 4)
- **HKB 9999 c** – Entwickeln von Software
  - **HK 9999 c.01** – Mikrocontroller-Programme entwickeln
    - **LK ET c1 11** – Sie wenden die Grundkonzepte einer Programmiersprache an. (BFS · Semester 1, 3, 4, 7)
      - **LZ_4276** – Sie schreiben einfache Programme (Standardanweisungen). (Semester 3, 1, 4)
      - **LZ_9579** – Sie nutzen die Grundstruktur einer imperativen Programmiersprache. (Semester 3, 1)
      - **LZ_11203** – Sie schreiben verständliche und nachvollziehbare Kommentare im Code. (Semester 1)
      - **LZ_11204** – Sie nutzen die unterstützenden Funktionen einer Entwicklungsumgebung. (Semester 1)
    - **LK ET c1 12** – Sie wählen für beispielhafte Anwendungen geeignete Mikrocontroller. (BFS · Semester 2)
      - **LZ_529** – Sie beschreiben den Aufbau und die Funktionsweise eines Mikroprozessors. (Semester 2)
      - **LZ_11213** – Sie zählen Typen von Schnittstellen in Mikrocontrollern auf und kennen das Einsatzgebiet. (Semester 2)
      - **LZ_11214** – Sie wählen auf Grund des vorgegebenen Einsatzgebietes einen geeigneten Mikrocontroller. (Semester 2)
    - **LK ET c1 16** – Sie setzen verschiedene digitale oder analoge Schnittstellen an beispielhaften Aufgaben ein. (BFS · Semester 6)
      - **LZ_11192** – Sie setzen unterschiedliche serielle Schnittstellen zur Ansteuerung von externer Hardware ein. (Semester 6)
      - **LZ_11193** – Sie realisieren Funktionen mit Hilfe von Timern. (Semester 6)
      - **LZ_9571** – Sie verwenden Interrupts. (Semester 6)
      - **LZ_9572** – Sie programmieren Anwendungen, indem sie Bibliotheken verwenden, ändern oder erstellen. (Semester 6)
      - **LZ_4262** – Sie beschreiben die Kenngrössen von A/D-D/A-Wandlern (Auflösung, Linearität, Sample rate). (Semester 6)
    - **LK ET c1 19** – Sie realisieren in den Grundstrukturen eines Mikrocontrollers einfachste Programme. (üK · Semester 4)
      - **LZ_4276** – Sie schreiben einfache Programme (Standardanweisungen). (Semester 4)
      - **LZ_11203** – Sie schreiben verständliche und nachvollziehbare Kommentare im Code. (Semester 4)
      - **LZ_11204** – Sie nutzen die unterstützenden Funktionen einer Entwicklungsumgebung. (Semester 4)
    - **LK ET c1 21** – Sie erstellen eine Hardwarestruktur inklusive der nötigen Schnittstellen und stellen diese graphisch dar. (üK · Semester 4)
      - **LZ_11246** – Sie benennen typische Schnittstellen an einem Mikrocontroller. (Semester 4)
      - **LZ_11247** – Sie weisen der geforderten Funktion entsprechend die korrekten I/Os zu. (Semester 4)
      - **LZ_11248** – Sie vergeben den I/Os aussagekräftige Namen zur Verwendung in der Software. (Semester 4)
    - **LK ET c1 22** – Sie setzen ein System für die Versionsverwaltung in der Software-Entwicklung ein. (üK · Semester 4)
      - **LZ_9582** – Sie verwenden eine kollaborative Versionverwaltungssoftware wie GitHub. (Semester 4)
      - **LZ_9583** – Sie führen Versionshistorien, insbesondere bei kollaborativer Entwicklungsarbeit. (Semester 4)
    - **LK ET c1 25** – Sie finden und beheben mit Hilfe der Entwicklungsumgebung Fehler in der Software. (üK · Semester 4)
      - **LZ_9782** – Sie setzen den Compiler zur Fehlersuche ein. (Semester 4)
      - **LZ_11249** – Sie erklären die Fehlermeldungen eines Compilers und kennen die Ursachen der Fehlermeldungen. (Semester 4)
    - **LK ET c1 26** – Sie finden und beheben mittels einer Debugschnittstelle Fehler in der Software. (üK · Semester 4)
      - **LZ_9783** – Sie setzen den Debugger zur Fehlersuche ein. (Semester 4)
      - **LZ_11250** – Sie benennen verschiedene Arten von Debuggern. (Semester 4)
      - **LZ_11251** – Sie erklären die Grundfunktionen eines Debuggers. (Semester 4)
    - **LK ET c1 29** – Sie nutzen mit Software Beispielen Interrupts. (üK · Semester 4)
      - **LZ_9571** – Sie verwenden Interrupts. (Semester 4)
      - **LZ_9573** – Sie konsultieren die Dokumentation des Mikrocontrollers und der Peripheriegeräte, um technische Daten zu identifizieren. (Semester 4)
      - **LZ_11256** – Sie lösen eine Problemstellung mit und ohne Interrupts. (Semester 4)
```
