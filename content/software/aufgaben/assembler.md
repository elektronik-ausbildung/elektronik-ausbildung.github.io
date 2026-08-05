# Aufgabe Assembler

In dieser Aufgabe programmierst du einen PIC-Mikrocontroller in Assembler: zuerst ein Blinkprogramm, danach ein Lauflicht.

- Schwierigkeit: Mittel
- Semester: 4-5
- Material: PIC Board 7 (aus dem ÜK), MPLAB X, XC8-Compiler, Programmer, LED
- Abgabe: Programmcode und Bericht (PDF oder Markdown) mit Liste der Assembler-Befehle

Verwende dein PIC Board 7 aus dem ÜK (oder einen beliebigen anderen PIC-Mikrocontroller). Stelle sicher, dass MPLAB und der XC8-Compiler installiert und aktuell sind.

1) Erstelle ein neues Assembler-Projekt. Lade die Dokumentation des Mikrocontrollers und die Dokumentation der Assemblerbefehle aus dem Internet.
2) Schreibe ein Assembler-Programm, das eine LED blinken lässt.
3) Programmiere ein LED-Lauflicht.
4) Zusatz: Kehre die Laufrichtung des Lauflichtes um, wenn ein Schalter gedrückt wird.
5) Dokumentiere das Lauflicht-Programm in einem kurzen Bericht. Erstelle eine Liste mit allen verwendeten Assembler-Befehlen und erkläre deren Funktion.

```{admonition} Referenzen zum Lehrplan
:class: references
:collapsible: closed

Die folgenden Leistungskriterien (LK) und Lernziele (LZ) aus dem Bildungsplan FutureMEM stehen in Bezug zu dieser Aufgabe.

- **HKB 9999 c** – Entwickeln von Software
  - **HK 9999 c.01** – Mikrocontroller-Programme entwickeln
    - **LK ET c1 10** – Sie führen arithmetische und boolesche Operationen in verschiedenen Zahlensystemen durch. (BFS · Semester 1)
      - **LZ_11180** – Sie setzen logische oder bitweise Operationen anwendungsgerecht ein. (Semester 1)
      - **LZ_11181** – Sie rechnen in verschiedenen Zahlensystemen. (Semester 1)
      - **LZ_11183** – Sie verstehen die Darstellung von Zahlen in einem Mikrocontroller. (Semester 1)
    - **LK ET c1 11** – Sie wenden die Grundkonzepte einer Programmiersprache an. (BFS · Semester 1, 3, 4, 7)
      - **LZ_4276** – Sie schreiben einfache Programme (Standardanweisungen). (Semester 3, 1, 4)
      - **LZ_9579** – Sie nutzen die Grundstruktur einer imperativen Programmiersprache. (Semester 3, 1)
      - **LZ_11194** – Sie nutzen für den Zugriff auf Variablen indirekte Adressierung. (Semester 3)
      - **LZ_11203** – Sie schreiben verständliche und nachvollziehbare Kommentare im Code. (Semester 1)
      - **LZ_11204** – Sie nutzen die unterstützenden Funktionen einer Entwicklungsumgebung. (Semester 1)
    - **LK ET c1 12** – Sie wählen für beispielhafte Anwendungen geeignete Mikrocontroller. (BFS · Semester 2)
      - **LZ_529** – Sie beschreiben den Aufbau und die Funktionsweise eines Mikroprozessors. (Semester 2)
      - **LZ_4272** – Sie unterscheiden Halbleiterspeicher (EPROM, EEPROM, Flash, RAM) nach ihrer Aufgabe nennen deren spezifische Eigenschaften. (Semester 2)
      - **LZ_11212** – Sie benennen die typischen Einsatzgebiete verschiedener Mikrocontroller-Typen. (Semester 2)
      - **LZ_11213** – Sie zählen Typen von Schnittstellen in Mikrocontrollern auf und kennen das Einsatzgebiet. (Semester 2)
      - **LZ_11214** – Sie wählen auf Grund des vorgegebenen Einsatzgebietes einen geeigneten Mikrocontroller. (Semester 2)
    - **LK ET c1 17** – Sie erklären die Funktion von vorgegebenen Code Sequenzen. (BFS · Semester 1, 4)
      - **LZ_11206** – Sie erklären die Funktion von vorgegebenem Code und werten ihn aus. (Semester 1)
    - **LK ET c1 18** – Sie erläutern die grundsätzliche Funktion einer Toolchain. (BFS · Semester 3)
      - **LZ_11197** – Sie erklären die einzelnen Schritte und Tools zur Umsetzung von Code in einer Hochsprache bis zur Ausführung auf dem Mikrocontroller. (Semester 3)
      - **LZ_11198** – Sie beschreiben die Aufgaben und möglichen Parameter der einzelnen Tools. (Semester 3)
    - **LK ET c1 19** – Sie realisieren in den Grundstrukturen eines Mikrocontrollers einfachste Programme. (üK · Semester 4)
      - **LZ_4276** – Sie schreiben einfache Programme (Standardanweisungen). (Semester 4)
      - **LZ_11203** – Sie schreiben verständliche und nachvollziehbare Kommentare im Code. (Semester 4)
      - **LZ_11204** – Sie nutzen die unterstützenden Funktionen einer Entwicklungsumgebung. (Semester 4)
```
