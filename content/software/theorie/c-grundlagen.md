# C Grundlagen

## Befehle und Funktionen

Mikrocontroller und Computer im allgemeinen sind elektrische Maschinen, die vorgefertigte Anweisungen und Berechnungen ausführen. Dabei führen sie immer einen Befehl nach dem anderen aus.

Eine Liste oder Abfolge von solchen Anweisungen nennen wir "Software" oder "Code". Es gibt verschiedene Arten Code zu schreiben, diese Arten nennen wir Programmiersprachen. Für Mikrokontoroller verwenden wir die Programmiersprache C. C ist eine alte Programmiersprache, aber so einfach, dass sie selbst auf sehr kleinen Rechnern läuft.

Schauen wir uns an, wie wir einen Mikrocontroller mit C programmieren können.

## Entwicklungsumgebung

Jeder Hersteller von Mikrocontrollern stellt uns eine sogenannte "Entwicklungsumgebung" zur Verfügung. Eine Entwicklungsumgebung ist ein Programm, das uns hilft Code zu schreiben.

Zum üben verwenden wir einen PIC Mikrocontroller von Microchip und das passende Programm MPLABX.

## Anweisungen

In C gibt es zwei Arten von Anweisungen:

```c
DoSomething();       // Funktion/Anweisung
5 * 3 + 5;           // Berechnung
```

Die Funktion hat immer einen Namen und darauf folgend runde Klammern. Berechnungen können wie gewohnt in Mathematik geschrieben werden. Egal ob Anweisungen oder Berechnung, am Schluss braucht es ein Strichpunkt. Das sagt dem Computer "Hier ist die Anweisung fertig".

Funktionen können auch Antwort geben oder Resultate zurückgeben. In diesem Fall kann die Antwort zum Beispiel in einer Variable gespeichert werden.

```c
uint8_t number = RandomNumber();        // Die Funktion "RandomNumber() liefert uns als Antwort eine Zahl, 
                                        // die in der Variable mit dem Namen "Number" abgespeichert wird
uint8_t result = 4 + 8;                 // Berechnungen haben immer ein Ergebnis
```

## Variablen

Variabel sind dazu da, um Zahlen und Text ab zu speichern.

Jede Variable hat einen Typ, der besagt was gespeichert wird. Dazu einen Namen und einen Wert.

```c
uint8_t myNumber = 5;
int16_t myNegativeNumber = -56;
```

### Variablentypen

| Typ      | Eigenschaften                       | Zahlenbereich             |
| -------- | ----------------------------------- | ------------------------- |
| uint8_t  | positive, ganze Zahlen              | 0 - 255                   |
| uint16_t | positive, ganze Zahlen              | 0 - 65535                 |
| uint32_t | positive, ganze Zahlen              | 0 - 4294967295            |
| int8_t   | ganze Zahlen, auch negativ          | -128 - +127               |
| int16_t  | ganze Zahlen, auch negativ          | -32768 - +32767           |
| int32_t  | ganze Zahlen, auch negativ          | -2147483648 - +2147483648 |
| char     | Buchstaben / Zeichen                | ASCII                     |
| bool     | Kann nur 1/0, wahr oder falsch sein | 0 - 1                     |

### Listen / Arrays

```c
uint8_t number = 23;                    // Erstelle eine Variable/Zahl
uint8_t list[5] = { 0, 1, 2, 3, 4};     // Erstellt eine Liste mit 5 Zahlen
char text[] = "Hallo Welt";             // Erstellt einen Text (Eine Liste von Buchstaben)

// Listen können ihren Index/Nummer angesprochen werden. 
// Achtung, in C beginnen wir beim Zählen mit 0
counter[0] = 2;     // Die erste Zahl in der Liste ist nun 2
counter[2] = 7;     // Die dritte Zahl in der Zahl ist nun 7

```

## Verzweigungen

### if - else

Mit einer if Verzweigung können Anweisungen definiert werden, die nur ausgeführt werden wenn eine Bedingung zutrifft. Die Bedingung kommt in die Klammer nach dem `if`. Die Anweisungen in den geschwungenen Klammern werden nur ausgeführt, wenn die Bedingung zutrifft. Ist die Bedingung nicht erfüllt, werden die Anweisungen im Block nach `else` ausgeführt.

```c
// Es wird eine Variable erstellt, sie erhält den Namen "something". 
// Der Typ der Variable ist uint8_t - wir können also Zahlen von 0 - 255 abspeichern. 
uint8_t something = RandomNumber();     

if(something <= 10)
{
    DoSomeThing();  // Wird ausgeführt wenn die Variable "something" 
                    // kleiner oder gleich als 10 ist. 
}
else
{
    SomeFunction(); // Wird ausgeführt, wenn die Bedingungen oben nicht 
                    // zutrifft (in diesem Fall wenn die Variable "something" 
                    // grösser als 10 ist)
}
```

## Schleifen

Mit Schleifen kann man gewisse Dinge mehrfach tun. Es gibt mehrere Arten von Schleifen, die wichtigsten sin `while` und `for`.

### While

While Schleifen haben ähnlich wie `if` Verzweigungen eine Bedingung in der Klammer nach dem `while`. Solange die Bedingung wahr ist, werden die Anweisungen in der geschweiften Klammer immer wider ausgeführt. Das Programm läuft erst weiter, wenn die Bedingung nicht mehr wahr ist.

```c
while(something < 23)
{
    DoSomeThing();
}
```

Die `for` Schleife ist etwas komplizierter - in der Klammer stehen gerade drei Ausdrücke. Mit `for` kann man Anweisungen mehrmals ausführen. Der erste Ausdruck `i = 0` sagt wo wir beginnen - wir setzen die Variable `i` auf 0. Der zweite Ausdruck sagt, wie weit wir zählen. Wir führen die Schleife aus so lange wie `i < 7` wahr ist. Der dritte Ausdruck sagt, dass wir `i` in Einerschritten Hochzählen.

```c
uint8_t i;
for(i = 0; i < 7; i++)
{
    print(i);
}
```

Ausgabe:

```txt
0123456
```

Wir können `i` auch in Zweierschritten zählen:

```c
uint8_t i;
for(i = 2; i < 10; i = i + 2)
{
    print(i);
}
```

Ausgabe:

```txt
2468
```

## Hardware

Auf der Leiterplatte mit dem Mikrocontroller sind verschiedene Elemente verbaut. Schalter und LED, auch ein Display ist vorhanden. Um diese zu steuern gibt es Anweisungen für den Mikrocontroller.

## LED

Es gibt 10 LED, diese sind als LED Liste verfügbar.

Die LEDs kann man über Funktionen ein- und ausschalten.

```c
GPIO_TurnOn(...);   // Schaltet eine LED ein
GPIO_TurnOff(...);  // Schaltet eine LED an
GPIO_Toggle(...);   // Wechselt den Zustand der LED (ein -> aus oder aus -> ein)
```

In der Klammer muss man definieren, welche LED geändert werden soll:

```c
GPIO_TurnOn(LED[0]);   // Schaltet LED0 ein
GPIO_TurnOff(LED[1]);  // Schaltet LED1 ein
GPIO_Toggle(LED[7]);   // Schaltet LED7 um
```

Auf dem Board sind 10 LED, nummeriert von 0 - 9.

## Schalter

Schalter funktionieren mit ähnlichen Anweisungen wie LED. Es gibt eine Liste mit 8 Schalter `Button`.

Diese Funktion liest ein Schalter 3 ein, liefert "true" wenn er eingeschaltet ist, sonst "false".

```c
bool button3;
button3 = GPIO_Read(Button[3]);     
```

Das kann zum Beispiel mit Verzweigungen kombiniert werden. Das folgende Programm schaltet die LED0 ein wenn Schalter 0 ein ist. Ist Schalter 0 aus, wird auch die LED aus geschaltet.

```c
if(GPIO_Read(Button[0]) == true)
{
    GPIO_TurnOn(LED[0]);
}
else
{
    GPIO_TurnOff(LED[0]);
}
```

## Warten

Mikrocontroller sind schnell - sie verarbeiten mehrere Millionen Anweisungen pro Sekunde. Manchmal ist es nötig, dass sie eine gewisse Zeit warten. Das kann mit folgender Anweisung erreicht werden.

```c
DelayMS(100);
```

Die Zahl in Klammer gibt an, wie viele Millisekunden der Mikrocontroller warten soll.

## Aufgaben

1. Lasse eine LED 1 Mal pro Sekunde blinken.
2. Lassen zwei LED 10 Mal pro Sekunde blinken.
3. Lasse alle LED 10 Mal pro Sekunde blinken, aber nur, wenn Schalter 0 gedrückt ist.
4. Lasse LED 0-6 blinken wenn der zugehörige Schalter gedrückt ist.
