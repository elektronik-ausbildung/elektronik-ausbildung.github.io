# Clean Code 101 - Was ist Sauberer Code?

Lesetipp - [Wieso ist sauberer Code wichtig?](assets/James%20O.%20Coplien%20on%20Clean%20Code.md) - Vorwort zum von James Coplien zum Buch Clean Code von Bob Martin.

## Stinkender Code

Manche Programme funktionieren, sind semantisch korrekt und trotzdem ist es schwer, die Übersicht zu gewinnen und den Code zu verstehen. Solcher Code stinkt! Wir wollen genauer untersuchen, wie es dazu kommt.

Was heisst es eigentlich, wenn wir sagen, ein Programm funktioniert? Meistens meinen wir, dass ein Programm in einem oder mehreren Punkten das Verhalten zeigt welche wir erwarten. Mir meinen damit meisten nicht: Das Programm hat keine Fehler. Je grösser das Programm, desto grösser die Wahrscheinlichkeit, dass es Fehler enthält. Es ist nicht möglich zu beweisen, dass ein Programm immer funktioniert, und es ist sehr schwer alle möglichen Fehler zu finden.

Ein Meme sagt dazu:

> Dein erster Podcast wir schlecht sein. Dein erstes Video wir schlecht sein. Dein erster Aufsatz wird schlecht sein. Deine erste Kunst wird schlecht sein. Dein erstes Foto wird schlecht sein. Sein erstes Computerspiel wird schlecht sein. Aber dein erstes Programm wird perfekt sein. Es wird keine Fehler haben und sehr sauber sein. Es wird heissen "Hallo Welt".

Nur die kleinsten Programme sind fehlerfrei. Wenn wir Fehler nicht verhindern können müssen wir vorbeugen. Wir müssen lernen Code so zu schreiben, dass Fehler wenn immer möglich auffallen. Wir müssen Mechanismen einführen um Fehler zu finden. Code muss übersichtlich und lesbar sein, ansonsten wirst du und deine Kollegen immer mehr Fehler machen. Bedenke, der Code, den du heute schreibst, wir dir in 6 Monaten fremd erscheinen. Wie ist es erst für den Kollegen, der in 20 Jahren einen Fehler in deinem Programm beheben muss?

Was aber macht, dass Code schwer lesbar ist? Wie beginnt ein Code zu Stinken? Es gibt viele Merkmale von schlechtem Code. Wichtig ist, es gibt hier selten richtig oder falsch. Es gibt selten ein klares richtig oder falsch - vielmehr die Frage "Können wir das besser, übersichtlicher, einfacher und verständlicher machen?" Merkmale von schlechtem Code nennt man Code Gerüche (Übersetzt vom Englischen "Code Smells").

## Sauberer Code

Was ist sauberer Code? Sauberer Code ist...

- Verständlich, auch für Programmierer die den Code nicht selbst geschrieben haben
- Übersichtlich
- Wenige Fehler
- Fehler sind einfach zu reparieren
- Der Code kann einfach weiterentwickelt werden
- Der Code kann ohne grosse Anpassungen in anderen Projekten verwendet werden

Aus dem Buch Clean Code:

> Denken Sie an einen gut geschriebenen Zeitungsartikel. Sie lesen ihn von oben nach unten. Oben erwarten Sie eine Überschrift, die Ihnen sagt, worum es in dem Artikel geht, und Ihnen die Möglichkeit gibt, zu entscheiden, ob Sie ihn lesen wollen. Der erste Absatz gibt einen Überblick über die ganze Geschichte, wobei alle Details verborgen bleiben, während man die groben Konzepte erfährt. Je weiter Sie nach unten gehen, desto mehr Details erfahren Sie, bis Sie alle Daten, Namen, Zitate, Behauptungen und andere Kleinigkeiten haben.  
> Wir möchten, dass eine Quelldatei wie ein Zeitungsartikel aussieht. Der Name sollte einfach, aber aussagekräftig sein. Der Name allein sollte ausreichen, um uns zu sagen, ob wir uns im richtigen Modul befinden oder nicht. Die obersten Teile der Quelldatei sollten die übergeordneten Konzepte und Algorithmen enthalten. Der Detailgrad sollte nach unten hin zunehmen, bis wir am Ende die Funktionen und Details der untersten Ebene in der Quelldatei finden. Eine Zeitung besteht aus vielen Artikeln; die meisten sind sehr klein. Einige sind ein wenig größer. Nur sehr wenige enthalten so viel Text, wie eine Seite fassen kann. Das macht die Zeitung benutzbar. Wäre die Zeitung nur eine lange Geschichte mit einer ungeordneten Ansammlung von Fakten, Daten und Namen, würden wir sie einfach nicht lesen.

Solchen Code zu schreiben ist nicht einfach - es gibt hier keine sturen Regeln, kein schwarz / weiss. Aber es gibt Prinzipien und Muster die uns helfen, besseren Code zu schreiben. Das wichtigste ist aber, das wir überhaupt versuchen besseren Code zu schreiben.

### Kommentare

Code Smells im Bezug auf Kommentare sind warscheineich am einfachsten zu erkennen. Es ist offensichtlich, wenn Kommentare schlecht sind - gute Kommentare zu schreiben ist aber sehr schwer. Normalerweise entsteht darüber bereits in der Schule eine Diskussion. Woran erkennt man schlechte Kommentare?

- Information am falschen Ort
  - Lizenzinformationen oder Changelogs gehören nicht in Code Dateien
  - Alle unnötigen Kommentare löschen!
- Falsche, alte oder halb wahre Informationen
  - Diese Schaden mehr als sie helfen
  - Vorsicht mir Zahlen, Werten und Einheiten in Kommentaren

```c
#define SEND_TIMEOUT_MS 50
...
...
DelayMS(SEND_TIMEOUT_MS); // Wait 10 ms
```

- Überflüssige Kommentare
  - Verschwenden Platz und machen Code unübersichtlich
  - Beispiel 1:

```c
i++; // increment i
```

  - Beispiel 2:

```c
/*****************************************************************************
 * function :       getDayWeek
 *****************************************************************************/
 /*! \brief         calculate weekday number from a Edt time.
 *
 *
 * \param           pEdtTime    pointer to a Edt time structure
 * \param           pDow        pointer to the day of week
 *
 *****************************************************************************/
void getDayWeek(tstEdtTime* pEdtTime, U16* pDow) { ... }
```

- Unverständliche Kommentare
- Auskommentierter Code
  - Ist nie ok! Es wird niemand wissen was damit ist. Warum auskommentiert? Ist er defekt? Ist er alt? Löschen! Das Versionskontrollsystem (git) erinnert sich sowieso daran.

Wie schreiben wir gute Kommentare? Es gibt kein Patentrezept. Was muss jemand wissen um den Code zu verstehen? Was kann man leicht übersehen? Wieso habe ich das so programmiert? Kommentare die nur wiederhohlen was im Code steht bringen nichts - löschen!

Besser ist es aber, Code so zu schreiben, dass er selbsterklärend und ohne Kommentare verständlich ist.

### Funktionen

- Funktionen, die auf globale Variablen zugreifen sind schwer zu verstehen. Es ist besser, Variablen als Argumente zu übergeben.

```c
uint8_t blinkTimeMS = 100;
...
...
void LED_Blink(void);

//Besser
void LED_Blink(uint8_t blinkTimeMS);
```

- Viele Argumente sind auch nicht übersichtlich. Die Beste Funktion hat keine Argumente, die zweitbeste hat eines. Die drittbeste hat 2 Argumente. Bist du sicher dass es mehr als 2 braucht? Wenn eine Funktion viele Argumente hat, hilft es oft, diese in eine Struktur zu verpacken.

```c
typedef struct {
  uint16_t x;
  uint16_t y;
} point_t;

void drawCircle(uint16_t x, uint16_t y, uint16_t radius);
void drawCircle(point_t center, uint16_t radius);
```

- Output Argumente sind schwerer verständlich, deshalb besser vermeiden. Wenn man Sie verwendet, dies mit Kommentaren klar deklarieren
- Flag Argumente sind schwer lesbar (Was bedeutet true oder false genau?). - Es ist ein Zeichen, dass eine Funktion zwei Dinge macht statt einem.

```c
// Was macht diese Funktion? Was bedeutet das Flag?
int16_t SHTC_GetTemperatureData(bool raw)
{
  int16_t temperature = 0;
  I2C_ReadRegister(TEMPERATURE, &temperature);
  if(!raw)
  {
    temperature = temperature >> 5 + 47;
  }
  return temperature;
}

// Verständlicher sind zwei separate Funktionen
int16_t SHTC_GetTemperatureCelsius(void) 
{ 
  int16_t temperatureCelsius = SHTC_GetRawTemperatureReading();
  temperatureCelsius = temperatureCelsius >> 5 + 47;
  return temperatureCelsius;
}

int16_t SHTC_GetRawTemperatureReading(void) 
{   
  int16_t rawTemperatureData = 0;
  I2C_ReadRegister(TEMPERATURE, &rawTemperatureData);
  return rawTemperatureData;
}
```

- Unverständliche Funktionsnamen - Funktionsnamen sollen sagen was sie machen!
- Lange / unübersichtliche Funktionen - Die Implementierung sollte verständlich und möglichst kurz sein
- Nicht verwendete Funktionen - Toter, nicht verwendeter Code sollte gelöscht werden
- Funktionen haben mehr als eine Aufgabe - Eine Funktion soll eine Aufgabe erfüllen. Wenn eine Funktion mehrere unterschiedliche Dinge macht, dann sollte man zwei Funktionen daraus machen.
- Funktionen haben Nebeneffekte - Eine Funktion soll keine unerwarteten Nebenaufgaben ausführen.
- Verschiedene Abstraktionslevel gemischt

### Variablen

- Der Name der Funktion erklärt die Variable nicht gut. Inhalt, Zweck und Funktion der Variable sind nicht klar.
- Die Variable hat einen unpassenden Typ und/oder Grösse (Hinweis: `void*` sind selten wirklich nötig)
- Der Geltungsbereich der Variable ist grösser als nötig. Globale Variablen (die über Dateien hinweg geteilt werden) sind fast immer schlecht. Um Daten zwischen Dateien auszutauschen gibt es Funktionen.
- Der Code enthält magische Zahlen. Zahlen im Code sollten durch Konstanten oder Makros mit einem Namen versehen werden.

```c
// Magische Zahlen
WeekNumber = Timestamp / 86400) % 7;

// Besser
#define SECONDS_PER_DAY 86400
#define DAYS_PER_WEEK 7
...
...
WeekNumber = Timestamp / SECONDS_PER_DAY) % DAYS_PER_WEEK;
```

```c
// Das erste Beispiel war ja vielleicht einfach zu verstehen, auch ohne Namen für die Konstanten
// Aber das hier versteht kein Mensch
year = (pEdtTime->byYear >= 88) ? (pEdtTime->byYear - 88) : (pEdtTime->byYear + 12);
```

### Generell

- Keine Dokumentation für Bibliotheken. Erkläre was eine Funktion / Bibliothek macht. Was muss jemand wissen der die Funktion / Bibliothek verwenden will?
- Inkonsistenter Stil: Verwende einen konsistenten Stil für Funktionsnamen, Variablennamen, Formatierung, Klammern usw
  - In einem Team, einer Firma sollten allen denselben Stil verwenden
- Der Build Prozess funktioniert nicht (= hat Fehler oder Warnungen). Ein Build ist nur ok, wenn es keine Warnungen gibt!
- Der Build Prozess ist nicht dokumentiert - zum Beispiel im "readme.md"
- Der Build Prozess ist kompliziert
