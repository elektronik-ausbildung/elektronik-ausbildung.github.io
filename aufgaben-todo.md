# Hardware

## diode.md – Messübung Diode

Klar: Ja, klar gegliedert. Didaktisch: Solide Grundlagenübung, aber klassisch.

1. ✅ Messung modernisieren: Zusätzlich einen Schritt einbauen bei dem die Kennlinie halbautomatisch mit Spannungsrampe und Oszilloskop im XY-Betrieb aufgenommen wird
2. ✅ Zusätzlich eine Schottky- und eine Leuchtdiode messen und die Flussspannungen vergleichen – macht Frage 4 („Arten von Dioden") praktisch greifbar.
3. ✅ Praxisbezug ergänzen: „Die Diode in der Gleichrichterschaltung eines Netzteils ist defekt – woran erkennst du das messtechnisch?" (Fehlerdiagnose).

## led-ansteuerung.md – LED Ansteuerung

Klar: Ja, sehr gut. Didaktisch: Stark, v.a. Photometrie und Temperatur-Effekt.

1. ✅ Messübung 1: zusätzlich die subjektive Helligkeit (Auge) mit den Lux-Werten diskutieren lassen – nicht-lineare Wahrnehmung vs. lineare Messung.
2. ✅ Messübung 2: Temperaturkoeffizient numerisch bestimmen (mV/K) und mit dem Datenblattwert vergleichen – verbindet Messung mit Datenblattarbeit.

## rc-oszillator.md – RC Oszillator

Klar: Ja, gute Eskalation in 4 Stufen. Didaktisch: Sehr wertvoll (Konstruktionsaufgabe + Messverifikation, 10-µA-Anforderung ist ein guter Bonus).

1. ✅ Stufe 1 klären: Hinweis auf aktiven vs. passiven Piezo (Treiber über Transistor) ergänzen – sonst Blockade beim Aufbau.
2. ✅ Stufe 4: vor dem Bau ein Blockdiagramm der Teilfunktionen (Oszillator + Timer + Zähler + Taster) verlangen – strukturiert das Entwickeln.
3. ✅ Messprotokoll konkretisieren: Tabelle „berechnet vs. gemessen" mit Abweichung in % verlangen.

## temperatursensor.md – Temperatursensor

Klar: Ziel verständlich, aber nur 1 Absatz – keine Schrittstruktur. Didaktisch: Nette Einstiegsschaltung, zu dünn.

1. ✅ In Schritte gliedern: Datenblatt → Übertragungsfunktion → Schwellwerte → Komparator-Fensterdetektor → Aufbau.
2. ✅ Abgabe präzisieren: Vorwiderstände und Schaltpunkte berechnen und die 3 Umschalt-Temperaturen messtechnisch nachweisen.

## mosfet-schalter.md – Mosfet als Schalter

Klar: Ja. Didaktisch: Motivierend (RGB-Streifen), Datenblattarbeit gut. Achtung: Schwierigkeit „Leicht"/Semester 2-4 passt nicht zur Aufgabe.

1. ✅ Konkreten Typenvergleich verlangen: 2–3 Logic-Level-Mosfets (z. B. IRLZ44N vs. BS170) aus Datenblättern auswählen und begründen.

## opamp.md – Operationsverstärker

Klar: Ja. Didaktisch: Stark (spannungsgesteuerte Stromquelle + Lichtregelung).

1. ✅ Die Übertragungsfunktion (0–5 V → 0–20 mA) explizit formulieren lassen, damit die Dimensionierung systematisch ist.
2. ✅ Toleranzanalyse: I_out bei 0 / 2,5 / 5 V messen und Abweichungen vom Sollwert erklären (Offset, R-Toleranz).

## Photodiode.md – Photodioden

Klar: Ja. Didaktisch: Sehr gut – Frage 7 („Wie hell ist es am Tag/Nacht?") und der Rückwärtsstrom-Vergleich sind hervorragende Aufgaben.

1. ✅ Frage 7 weiterführen: konkrete Lux-Werte abschätzen und in die Schaltungsdimensionierung (Widerstandswerte) einfliessen lassen.
2. ✅ Die zwei Messungen (Rückwärtsstrom LED vs. Photodiode) in einem gemeinsamen Diagramm darstellen – macht Frage 3 praktisch greifbar.

## linearregler.md – Linearregler

Klar: Ja. Didaktisch: Gut, Junction-Temperatur mit/ohne Kühlkörper ist sehr praxisnah.

1. ✅ Ergebnis der Temperatur-Berechnung auswerten lassen: Bedeutung für Lebensdauer/Derating diskutieren – erklärt das „Warum".
2. ✅ Messübung vertiefen: Lastsprung (10→50 mA) und daraus Load-/Line-Regulation aus der Oszilloskop-Aufzeichnung berechnen lassen statt nur aufzählen.
3. ✅ Wirkungsgrad bei kleiner vs. grosser Last berechnen lassen – macht die Schwäche des Linearreglers (Wärmeverlust) praktisch erfahrbar.

## 7-segment.md – 7 Segment Würfelanzeige

Klar: Ja, gut strukturiert.  Didaktisch: Motivierend, Logik-Verknüpfungen gut.

1. ✅ KV-Diagramm (Karnaugh) zur Minimierung verlangen und einen Funktionstest mit vorgegebenen Eingangskombinationen dokumentieren lassen.

## akku-laden.md – Akku Laden

Klar: Meistens. Didaktisch: Sehr praxisnah (Ikea Ladda, Auto-Batterie).

## solarzelle.md – Solarzelle

Klar: Ja, aber reines Quiz ohne praktischen Teil. Didaktisch: Fragen gut, Übung fehlt völlig.

1. ✅ Kennlinie einer Solarzelle mit variablem Widerstand messen und den MPP im Diagramm einzeichnen – macht Frage 5 greifbar.
2. ✅ Datenblattarbeit: U_OC, I_SC, P_MPP aus einem echten Solarzellen-Datenblatt auslesen lassen.
3. ✅ Rechenfrage ergänzen: „Warum arbeitet man im MPP und nicht bei I_SC oder U_OC?" (Leistungsprodukt).

# Software

## toolchain.md – Toolchain

Klar: Ja, Szenario und Fragen gut. Didaktisch: Verständlich, aber reine Recherche – etwas trocken.

1. ✅ Toolchain real ausführen lassen: Präprozessor → Compiler → Assembler → Linker → objcopy als Command-Line (arm-none-eabi-gcc …) durchspielen.
2. ✅ Zwischenprodukte (.i, .s, .elf, .hex) erzeugen und deren Unterschied beschreiben lassen.
3. ✅ Abschluss-Experiment: einen absichtlichen Fehler einbauen und die Fehlermeldung dem richtigen Toolchain-Schritt zuordnen – schult Fehlerinterpretation.

## uart.md – UART

Klar: Ja, einfach und konkret. Didaktisch: Sehr gut – die „Geheimnachricht" vom Kollegen ist ein motivierender Twist.

1. ✅ Baudrate nicht verraten: die Lernenden sollen Start-/Stopbits identifizieren und die Baudrate aus der Signallänge selbst messen.
2. ✅ Abgabe vertiefen: Markierungen (Start/Stop/Datenbits) im Ausdruck + Erklärung, wie die Zeichen dekodiert wurden.
3. ✅ Zusatz: dieselbe Nachricht mit falscher Baudrate aufzeichnen und zeigen, wie sich Fehldecodierung äussert.

## assembler.md – Assembler

Klar: Ja. Didaktisch: Motivierend, aber Überschneidung mit stm32-Lauflicht.

1. ✅ Lauflicht mit Timer/Interrupt statt Schleifen-Delay takten – zeigt die Stärke von Assembler.
2. ✅ Zusatz: Laufrichtung per Schalter umkehren.

## i2c.md – I2C

Klar: Ja, gut strukturiert. Didaktisch: Wertvoll (eigener Treiber ohne Library). Achtung: Schwierigkeit „Einfach" passt nicht.

2. ✅ LA-Aufzeichnung auswerten lassen: Start-/Stop-Bedingung, 7-bit-Adresse, ACK/NACK markieren.
3. ✅ Fehlersuche: bewusst eine falsche Slave-Adresse programmieren und das NACK im Logic Analyzer interpretieren.

## stm32.md – STM32 DevKit

Klar: Ja, gut in 6 Sektionen gegliedert, aber eine lange Aneinanderreihung vieler kleiner Aufgaben. Didaktisch: Sehr praktisch.

2. ✅ Pro Sektion ein Nachweis-Kriterium definieren (Screenshot, Video, Code im Git-Repo, LA-Aufzeichnung).
3. ✅ Überschneidungen reduzieren: UART-/I2C-Teile verlinken auf uart.md/i2c.md statt duplizieren; hier auf den Einstieg fokussieren.

## netzwerk-praktikum.md – Netzwerk

Klar: Ja, sehr gut strukturiert (OSI-Aufbau, echtes Equipment). Didaktisch: Stärkstes Praktikum im Projekt.

3. ✅ OSI-Kapitel als Konsolidierung nutzen: alle bisherigen Protokolle (Ethernet/IP/TCP/HTTP) den OSI-Schichten zuordnen lassen.

## repetition-syntax.md – C Repetition

Klar: Ja. Didaktisch: Farbmarkieren ist ungewöhnlich und für visuelle Lerntypen gut – aber derselbe Code 3× wird monoton.

1. ✅ Verschiedene Listings verwenden (eines mit Funktionen, eines mit Structs/Pointern aus 2.2–2.4) statt 3× identisch.
2. ✅ Reflexionsfrage ergänzen (warum unterscheidet man Deklaration/Definition?).

## git.md – Git

Klar: Ja, gut abgegrenzt. Didaktisch: Solide, interaktives Tutorial.

2. ✅ Abgabe präzisieren: zusätzlich zu den Screenshots pro Level eine kurze Reflexion (was war neu, was verwirrend).

## ltspice.md – Simulation

Klar: Ja. Didaktisch: Solide Simulation, Verifikation fehlt teilweise.

1. ✅ Grenzfrequenz aus dem Bode-Diagramm ablesen und mit f = 1/(2πRC) vergleichen (Abweichung in %).
2. ✅ Realität des OpAmp thematisieren: Ab welcher Frequenz weicht die Verstärkung von −100 ab? (begrenzte Bandbreite).
