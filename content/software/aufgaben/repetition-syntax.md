# C Repetition Syntax

In dieser Übung wiederholst du die Grundlagen der C-Syntax. Du liest aus dem Buch «Modern C» und markierst die verschiedenen Elemente des C-Codes farblich.

- Schwierigkeit: Leicht
- Semester: 3-4
- Material: Buch «Modern C» von Jens Gustedt, Computer mit PDF-Viewer, Stifte in verschiedenen Farben
- Abgabe: Markierter Code

1) Lies Kapitel 2.1 aus dem Buch [Modern C von Jens Gustedt](https://inria.hal.science/hal-02383654v2/file/modernC.pdf) sorgfältig durch. Nutze gegebenenfalls ein LLM zum Übersetzen oder Erklären.

2) Nimm folgenden Code (Listing 1.1 aus dem Buch) und markiere in unterschiedlichen Farben.

- Alle Kommentare
- Alle Zahlen (englisch "literals")
- Alle Bezeichnungen (englisch "identifiers")

```c
/* This may look like nonsense , but really is C */
/* The main thing that this program does . */
void main () {
    // Declarations
    int i;
    double A [5] = {
        9.0 ,
        2.9 ,
        3.E+25 ,
        .00007 ,
    };

    // Doing some work
    for (i = 0; i < 5; ++i) {
        printf (" element  %d is %g, \ tits   square  is %g\n",
        i,
        A[i],
        A[i]*A[i]);
    }
    return 0;
}
```

3) Nimm folgenden Code (Listing 1.1 aus dem Buch) und markiere in unterschiedlichen Farben.

- Variablennamen
- Bezeichnungen von Datentypen
- Funktionsnamen
- Alle Operatoren

```c
/* This may look like nonsense , but really is C */
/* The main thing that this program does . */
void main () {
    // Declarations
    int i;
    double A [5] = {
        9.0 ,
        2.9 ,
        3.E+25 ,
        .00007 ,
    };

    // Doing some work
    for (i = 0; i < 5; ++i) {
        printf (" element  %d is %g, \ tits   square  is %g\n",
        i,
        A[i],
        A[i]*A[i]);
    }
    return 0;
}
```

4) Lies Kapitel 2 zu Ende (2.2, 2.3 und 2.4)

5) Nimm folgenden Code (Listing 1.1 aus dem Buch) und markiere in unterschiedlichen Farben.

- Alle Deklarationen
- Alle Definitionen
- Alle Statements

```c
/* This may look like nonsense , but really is C */
/* The main thing that this program does . */
void main () {
    // Declarations
    int i;
    double A [5] = {
        9.0 ,
        2.9 ,
        3.E+25 ,
        .00007 ,
    };

    // Doing some work
    for (i = 0; i < 5; ++i) {
        printf (" element  %d is %g, \ tits   square  is %g\n",
        i,
        A[i],
        A[i]*A[i]);
    }
    return 0;
}
```

6) Beantworte schriftlich: Warum unterscheidet man zwischen Deklaration und Definition?

## Referenzen zum Lehrplan

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
      - **LZ_11203** – Sie schreiben verständliche und nachvollziehbare Kommentare im Code. (Semester 1)
      - **LZ_11204** – Sie nutzen die unterstützenden Funktionen einer Entwicklungsumgebung. (Semester 1)
    - **LK ET c1 17** – Sie erklären die Funktion von vorgegebenen Code Sequenzen. (BFS · Semester 1, 4)
      - **LZ_11205** – Sie stellen gegebenen Code strukturiert grafisch dar. (Semester 1)
      - **LZ_11206** – Sie erklären die Funktion von vorgegebenem Code und werten ihn aus. (Semester 1)
