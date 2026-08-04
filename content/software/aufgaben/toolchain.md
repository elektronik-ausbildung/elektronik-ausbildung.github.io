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
