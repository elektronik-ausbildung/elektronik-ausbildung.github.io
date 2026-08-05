# Praktikum Computer Netzwerk

Computernetzwerke sind nur am Rand Thema der Elektroniker Ausbildung. In der Praxis sind sie aus unserem Berufsalltag nicht wegzudenken. Dieses Praktikum soll einen Einblick in die grundlegenden Funktionsprinzipien von Computernetzwerken bieten.

Kaum ein Bereich der Technik kommt ohne Computernetzwerke aus. Vielleicht sprechen wir heute eher von "Cloud", "Internet der Dinge" oder ähnlichen Schlagwörtern – dahinter verstecken sich fast immer klassische Computernetzwerke. Wir gehen in diesem Praktikum von den Grundlagen der Elektronik aus und öffnen Schritt für Schritt die Welt des Internets.

Das Praktikum besteht aus Recherche, Bericht schreiben und Übungen lösen. Für jedes Kapitel soll gemäss der Fragestellung recherchiert und in einem Bericht zusammengefasst werden. Besprich die Recherche in jedem Kapitel mit dem Berufsbildner, bevor du die Antworten in einem Bericht dokumentierst und die Übungen löst.

> Bemerkung: Das Verwenden von AI/LLM zur Recherche ist erlaubt, achte aber darauf, dass auch andere Quellen einbezogen werden. AI geben oft sehr oberflächliche Antworten, manchmal sind die Antworten auch einfach falsch. Achte darauf, die Aussagen der AI zu verstehen und zu überprüfen.

- Schwierigkeit: Schwer\*
- Semester: 7-8
- Material: Computer mit Wireshark und NMS, Ethernet-Switch (unmanaged, PoE), DTS410x mit GPS-Antenne, Mobaline-Uhr, NCC, NBU190, Netzwerkkabel
- Abgabe: Bericht (PDF oder Markdown) mit Recherche, Übungen und Dokumentation des Aufbaus

> \* Die Aufgabe ist nicht per se schwierig, für Elektroniker aber ausserhalb ihrer Komfortzone.

## Vorbereitung

Baue folgendes Netzwerk auf:

- Computer / Laptop mit NMS installiert
- Einfacher (unmanaged) Ethernet Switch mit PoE
- DTS410x als Zeitserver
  - GPS Empfänger zur Synchronisation
  - Mobaline Uhr zur Kontrolle
- NCC
  - Mobaline Uhr zur Kontrolle
- NBU190

> Dokumentiere im Bericht den Aufbau mit Materialliste, einer Skizze, wie die Geräte verbunden sind, und den Einstellungen der Geräte.
>
> Tipp: Die Manuals geben viele Infos zu den Geräten und wie man diese einsetzen kann.

## Kapitel 1: Bits

Recherchiere folgende Fragen und schreibe ein Kapitel zum Thema Ethernet in den Bericht.

- Was ist Ethernet?
  - Welchen Ethernet-Standard verwendet der NCC?
    - Wie werden Bits übertragen?
    - Wie hoch ist die Symbolrate?
    - Wie hoch ist die Bitrate?
    - Wie viele Kommunikationskanäle gibt es?
- Was ist WLAN?

> Übung: Zeichne ein Ethernet-Paket mit einem Oszilloskop (KO) auf und dokumentiere die Messung. Welche Spannungen und welche Frequenzen treten auf? Welcher Ethernet-Standard wird verwendet?

## Kapitel 2: Bytes

Recherchiere folgende Fragen und erweitere das Kapitel zum Thema Ethernet in deinem Bericht

- Wie ist ein Ethernet-Frame aufgebaut? Erkläre die Funktion der einzelnen Blöcke.
  - Wie viele Daten können in einem Frame maximal versendet werden?
  - Welche Art Daten können versendet werden?
- Was ist eine MAC-Adresse und wozu dient diese?
  - Wie werden MAC-Adressen verteilt?
- Was macht ein (einfacher, unmanaged) Switch?

> Übung: Installiere Wireshark und analysiere ein Ethernet-Frame. Lies deine MAC-Adresse aus. Verwende Wireshark Pro, um den Datenverkehr zum NBU abzuhören, und lies die MAC-Adresse des NBU aus.

## Kapitel 3: Verbindung

Recherchiere folgende Fragen und schreibe ein Kapitel zum Thema IP in den Bericht.

- Wie können Daten an Computer versendet werden, die nicht direkt mit unserem Computer verbunden sind?
- Was ist eine IP-Adresse?
  - Was ist die Subnetzmaske?
  - Wieso braucht es Subnetzmasken?
- Welches sind die wichtigsten Felder in einem IP-Paket?
- Was ist der Unterschied zwischen IPv4 und IPv6? Wieso wurde IPv6 eingeführt?
- Wie werden IP-Adressen verteilt?
- Woher weiss ein Switch, wo ein Paket hingeschickt werden muss?
- Was ist ein Router?
  - Was macht ein Router?
  - Wieso braucht es Router?
  - Woher weiss ein Router, wo ein Paket hingeschickt werden muss?

> Übung 1: Verwende den Befehl `ipconfig` (Windows Terminal / Powershell), um die IP-Adresse deines Computers auszulesen. Was siehst du? Was kannst du mit dem Befehl alles erkennen?
>
> Übung 2: Verwende den Befehl `tracert`, um herauszufinden, in welchem Rechenzentrum die Webseite «www.moser-baer.ch» betrieben wird. Was siehst du alles in den Infos von tracert?

## Kapitel 4: Transport

Recherchiere folgende Fragen und schreibe ein Kapitel zum Thema TCP/UDP Transport in den Bericht.

- Was ist ein UDP-Datagramm? Wie ist es aufgebaut?
  - Wozu dienen die Portnummern?
  - Wie gross kann ein UDP-Datagramm maximal sein?
- Was ist TCP?
  - Wie können grosse Dateien übertragen werden?
  - Wie wird sichergestellt, dass keine Daten verloren gehen?
- Vergleiche TCP und UDP:
  - Was sind die wichtigsten Unterschiede?
  - Wann wird sinnvollerweise TCP verwendet?
  - Wann wird sinnvollerweise UDP verwendet?

## Kapitel 5: Applikation

- Wozu verwendest du das Internet? Welche Applikationen verwendest du?
- Was für Pakete werden versendet, wenn du diese Applikationen benutzt? Was sind die verwendeten Protokolle?

### Kapitel 5.1 Webseiten

- Webseiten verwenden HTTP. Was ist HTTP?
  - Wie ist ein HTTP-Request aufgebaut?
  - Wie wird ein HTTP-Request versendet?
  - Was ist eine URL?
- Was ist ein Browser?
- Was ist ein Webserver?
- Was ist HTML?
- Was ist CSS?
- Was ist JavaScript?
- Wie hängen all diese Stichworte zusammen?
- Wie veröffentlicht man eine Webseite?

> Übung: Erstelle eine einfache Webseite über dich selbst. Sie sollte ähnlich wie dein Lebenslauf aussehen: ein Passfoto, persönliche Angaben und deine berufliche Laufbahn. Dazu verwendest du HTML und CSS. Beginne mit HTML und dem Inhalt der Seite. Später kannst du mit CSS bestimmen, wie das Design aussehen soll. Verwende die Tutorials auf [www.w3schools.com](https://www.w3schools.com), um HTML und CSS zu lernen. Es reicht dabei aber jeweils, die ersten paar Kapitel zu machen – es braucht nicht das komplette Tutorial.

### Kapitel 5.2 DNS

- Wie findest du die IP von google.ch?
- Was ist DNS, wie funktioniert es?
- Was ist eine Domain?
  - Was eine TLD?
  - Was ist eine Subdomain
- Wie erhält man eine eigene Domain?

### Kapitel 5.3 DHCP

- Was ist DHCP?
- Wieso ist es hilfreich?
- Was ist speziell an der Netzwerkadresse 192.168.0.0/16?
- Wann braucht man eine statische, wann eine dynamische IP-Adresse?

### Kapitel 5.4 TLS

- Was ist TLS?
- Wozu wird es verwendet?
- Was ist HTTPS?
- Inwiefern ist HTTPS sicherer als HTTP?

## Kapitel 5.5 OSI Referenzmodell

- Was ist das OSI Referenzmodell?
- Wozu dient das Modell?
- Konsolidierung: Ordne alle in diesem Praktikum behandelten Protokolle (Ethernet, IP, TCP, UDP, HTTP, DNS, DHCP, TLS, NTP, SNMP, SSH) den OSI-Schichten zu. Stelle die Zuordnung in einer Tabelle dar und begründe sie. Wo passt ein Protokoll in mehr als eine Schicht?

## Kapitel 6: Uhrensystem Moser Baer

Welche Netzwerkprotokolle werden von Uhren und Zeitservern bei Moser Baer verwendet?

### NTP & PTP

- Was ist NTP?
- Wozu wird das Protokoll verwendet?
- Wie sind die Pakete aufgebaut?
- Was ist PTP?
- Wieso ist es genauer als NTP?

### SNMP

- Was ist SNMP?
- Wozu verwendet Moser-Baer SNMP?

> Aufgabe: Finde und decodiere ein SNMP-Paket mit Wireshark

### SSH

- Was ist SSH?
- Wozu verwendet der DTS SSH?

> Aufgabe: Verbinde dich per SSH mit einem DTS und stelle die Uhrenlinie auf 12 h

```{admonition} Referenzen zum Lehrplan
:class: references
:collapsible: closed

Die folgenden Leistungskriterien (LK) und Lernziele (LZ) aus dem Bildungsplan FutureMEM stehen in Bezug zu dieser Aufgabe.

- **HKB 9999 a** – Entwickeln von Ideen und Konzepten
  - **HK 9999 a.03** – die Machbarkeit von Ideen oder Aufträgen für elektronische Hard- oder Softwarelösungen abklären
    - **LK MEM 07 07** – Sie visualisieren Daten. (BFS · Semester 2, 3, 4)
      - **LZ_1131** – Sie erstellen eine Wertetabelle und zeichnen das entsprechende Diagramm auf. (Semester 2, 3, 4)
      - **LZ_1133** – Sie fügen Tabellen und Diagramme ein und bearbeiten diese. (Semester 2, 3, 4)
    - **LK MEM 07 08** – Sie vernetzen Komponenten zu Systemen, um Arbeitsprozesse zu unterstützen und kontinuierlich zu verbessern. (BFS · Semester 2)
      - **LZ_9205** – Sie erstellen oder interpretieren Netzwerkpläne und führen Änderungen korrekt nach. (Semester 2)
      - **LZ_9206** – Sie beurteilen grundlegende Sicherheitskriterien zu sicheren Passworten, 2Faktor Authentifizierung, Antivirensoftware und Firewalls (Basisschutz) und zählen typische Cyber Gefahren auf. (Semester 2)
      - **LZ_9207** – Sie beurteilen die Netzwerkzuverlässigkeit und erkennen Engpässe hinsichtlich des Datendurchsatzes bzw. können Optimierungen diesbezüglich vornehmen. (Semester 2)
    - **LK MEM 07 09** – Sie setzen einzelne Komponenten entsprechend ihrer Funktion ein, und konstruieren digitale Netzwerke. (BFS · Semester 2)
      - **LZ_9202** – Sie erläutern die Funktionen eines Routers oder Switches und verstehen den Aufbau der IP-Adressen, die Funktionsweise der Ports sowie der Subnetz Adressierung und zählen die Vor- und Nachteile von fixer oder dynamischer IP-Adresse Vergabe auf. (Semester 2)
      - **LZ_9203** – Sie konfigurieren einen Router mit fixer oder dynamischer IP-Adressvergabe. (Semester 2)
      - **LZ_9204** – Sie verbinden Netzwerkkomponenten und testen deren Funktion. (Semester 2)
    - **LK MEM 07 10** – Sie erläutern Vor- und Nachteile von vernetzten Komponenten. (BFS · Semester 2)
      - **LZ_1362** – Sie erläutern den Aufbau von Informations- und Kommunikationsnetzen. (Semester 2)
      - **LZ_9201** – Sie bezeichnen die Netzwerkkomponenten und nennen die Funktionen der notwendigen Hardware eines Netzwerkes (Router, Switch, Netzwerkkabel, Geschwindigkeiten) und zählen die Vor- und Nachteile von kabelgebundenen oder kabellosen Netzwerken auf. (Semester 2)
    - **LK MEM 07 11** – Sie schützen sich und ihr Umfeld gegen Cyberbedrohungen. (BFS · Semester 1)
      - **LZ_9181** – Sie wenden die vorgegeben Software gegen Cyberangriffe an. (Semester 1)
    - **LK MEM 07 12** – Sie schätzen mögliche Auswirkungen von Cyberbedrohungen und Sicherheitslücken ab. (BFS · Semester 1)
      - **LZ_9178** – Sie zählen die aktuellen Cyberbedrohungen und Gefahren auf. (Semester 1)
      - **LZ_9179** – Sie können die Bedrohlichkeit von Cyberangriffen und mögliche Sicherheitslücken abschätzen. (Semester 1)
      - **LZ_9180** – Sie nennen die Richtlinien und das Verhalten gegen Cyberangriffe. (Semester 1)
    - **LK MEM 07 13** – Sie identifizieren aktuelle Cyberbedrohungen und Gefahren. (BFS · Semester 1)
      - **LZ_9182** – Sie erkennen mögliche aktuelle Cyperbedrohungen. (Semester 1)
- **HKB 9999 c** – Entwickeln von Software
  - **HK 9999 c.03** – intelligente Komponenten und Dienste in einem Netz oder einer Cloud einbinden
    - **LK ET c3 01** – Sie integrieren Geräte, Sensoren oder Aktoren in einem Netzwerk oder Bussystem und konfigurieren diese, um die Kommunikation zu ermöglichen. (BE · Semester 5, 6, 7, 8)
    - **LK ET c3 03** – Sie dokumentieren die Netz- oder Bustopologie zusammen mit den gemachten Konfigurationen in der Entwicklungsdokumentation. (BE · Semester 5, 6)
```
