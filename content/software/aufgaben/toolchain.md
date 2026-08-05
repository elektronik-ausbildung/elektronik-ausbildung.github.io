# Aufgabe Toolchain

Stell dir vor, du nimmst ein STM32 DevKit und erstellst ein neues Firmwareprojekt. Du schreibst ein einfaches Programm, welches eine LED blinken lässt. Damit das funktioniert, benötigst du eine ganze Reihe von Programmen, die nacheinander ihre Arbeit machen. Die Kette von Programmen nennt man auch Toolchain. Was muss alles passieren, damit dein Code auf dem Mikrocontroller landet und eine LED blinken lässt? Welche Programme benötigst du? Wofür? Mache eine Liste mit allen Programmen und Schritten der Toolchain. Beschreibe die Aufgaben eines jeden Programms in 1 - 2 Sätzen.

- Schwierigkeit: Mittel
- Semester: 3-4
- Material: STM32 DevKit, STM32 Cube IDE, Computer
- Abgabe: Dokument (PDF oder Markdown) mit Liste und Beschreibung der Toolchain-Schritte sowie Nachweis des praktischen Durchspielens (Zwischenprodukte, Fehler-Experiment)

> Hinweis: IDEs wie die STM32 Cube IDE bündeln die ganze Toolchain. Der Name Cube IDE steht für die Toolchain und nicht für ein einzelnes Programm. Wenn der Knopf «Debug» oder «Build» gedrückt wird, führt die IDE jedes Programm der Toolchain nacheinander aus. Jedes dieser Programme hat einen eigenen Namen und kann eigenständig verwendet werden. Beschreibe die einzelnen Schritte, die im Hintergrund passieren.

Für jedes Programm der Toolchain beantworte folgende Fragen:

- Was macht das Programm?
- Wieso braucht es das Programm?
- Welche Dateien und Eingaben verarbeitet das Programm?
- Was ist das Ergebnis des Programms?
- Was sind die wichtigsten Einstellungen, die man vornehmen muss?
- Gib 2-3 Beispiele von Programmen/Software für jeden Schritt der Toolchain. Welches Programm wird in der Cube IDE verwendet?

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
      - **LZ_11204** – Sie nutzen die unterstützenden Funktionen einer Entwicklungsumgebung. (Semester 1)
    - **LK ET c1 18** – Sie erläutern die grundsätzliche Funktion einer Toolchain. (BFS · Semester 3)
      - **LZ_11197** – Sie erklären die einzelnen Schritte und Tools zur Umsetzung von Code in einer Hochsprache bis zur Ausführung auf dem Mikrocontroller. (Semester 3)
      - **LZ_11198** – Sie beschreiben die Aufgaben und möglichen Parameter der einzelnen Tools. (Semester 3)
    - **LK ET c1 19** – Sie realisieren in den Grundstrukturen eines Mikrocontrollers einfachste Programme. (üK · Semester 4)
      - **LZ_11204** – Sie nutzen die unterstützenden Funktionen einer Entwicklungsumgebung. (Semester 4)
    - **LK ET c1 25** – Sie finden und beheben mit Hilfe der Entwicklungsumgebung Fehler in der Software. (üK · Semester 4)
      - **LZ_9782** – Sie setzen den Compiler zur Fehlersuche ein. (Semester 4)
      - **LZ_11249** – Sie erklären die Fehlermeldungen eines Compilers und kennen die Ursachen der Fehlermeldungen. (Semester 4)
```
