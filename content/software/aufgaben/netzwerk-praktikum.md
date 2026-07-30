# Praktikum Computer Netzwerk

Elektroniker 4. Lehrjahr

Computernetzwerke sind nur am Rand Thema der Elektroniker Ausbildung. In der Praxis sind sie aus unserem Berufsalltag nicht weg zu denken. Dieses Praktikum soll einen Einblick in die Grundlegenden Funktionsprinzipen von Computernetzwerken bieten.

Kaum ein Bereich der Technik kommt ohne Computernetzwerke aus. Vielleicht sprechen wir heute eher von "Cloud", "Internet der Dinge" oder ähnlichen Schlagwörtern - dahinter verstecken sich fast immer klassische Computernetzwerke. Wir gehen in diesem Praktikum von den Grundlagen der Elektronik aus und öffnen Schritt für Schritt die Welt des Internets.

Das Praktikum besteht aus Recherche, Bericht schreiben und Übungen lösen. Für jedes Kapitel soll gemäss der Fragestellung recherchiert und in einem Bericht zusamme gefasst werden. Besprich die Recherche in jedem Kapitel mit dem Berufsbildner bevor du die Antworten in einem Bericht dokumentierst und die Übungen löst.

> Bemerkung: Das verwenden von AI/LLM zur Recherche ist erlaubt, achte aber darauf dass auch andere Quellen einbezogen werden. AI geben oft sehr oberflächliche Antworten, manchmal sind die Antworten auch einfach falsch. Achte darauf die Aussagen der AI zu verstehen und zu überprüfen.

## Vorbereitung

Baue folgendes Netzwerk auf:

- Computer / Labtop mit NMS installiert
- Einfacher (unmanaged) Ethernet Switch mit POE
- DTS410x als Zeitserver
  - GPS Empfänger zur Synchronisation
  - Mobaline Uhr zur Kontrolle
- NCC
  - Mobaline Uhr zur Kontrolle
- NBU190

> Dokumentiere im Bericht den Aufbau mit Materialliste, einer Skizze wie dier Geräte verbunden sind und den Einstellungen der Geräte.
>
> Tip: die Manuals geben viel Infos zu den Geräten und wie man diese einsetzen kann.

## Kapitel 1: Bits

Recherchiere folgende Fragen und schreiben ein Kapitel zum Thema Ethernet in den Bericht

- Was ist Ethernet?
  - Welchem Ethernet Standard verwendet der NCC?
    - Wie werden Bits übertragen?
    - Wie hoch ist die Symbolrate?
    - Wie hoch die Bitrate?
    - Wie viele Kommunikationskanäle gibt es?
- Was ist WLAN?

> Übung: Zeichne ein Ethernet Paket mit einem KO auf und dokumentiere die Messung. Welche Spannungen und welche Frequenzen treten auf? Welcher Ethernet Stadard wird verwendet?

## Kapitel 2: Bytes

Recherchiere folgende Fragen und erweitere das Kapitel zum Thema Ethernet in deinem Bericht

- Wie ist eine Ethernet Frame aufgebaut? Erkläre die Funktion der einzelnen Blöcke.
  - Wie viele Daten kann in einem Frame maximal versendet werden?
  - Welche Art Daten können versendet werden?
- Was ist eine MAC Addresse und wozu dient diese?
  - Wie werden MAC-Addressen verteilt?
- Was macht ein (einfacher, unmanaged) Switch?

> Übung: Installiere Wireshark und analisiere ein Ethernet Frame. Lies deine MAC Addresse aus. Verwende Wirshark Pro um den Datenverkehr zum NBU abzuhören und lies die MAC-Addresse des NBU aus.

## Kapitel 3: Verbindung

Recherchiere folgende Fragen und schreiben ein Kapitel zum Thema IP in den Bericht.

- Wie können Daten an Computer versendet werden, die nicht direkt mit unserem Computer verbunden sind?
- Was ist eine IP Adresse?
  - Was ist die Subnetzmaske?
  - Wieso braucht es Subnetzmasken?
- Welches sind die wichtigsten Felder in einem IP Paket?
- Was ist der Unterschied zwischen IPv4 und IPv6? Wieso wurde IPv6 eingeführt?
- Wie werden IP Adressen verteilt?
- Woher weiss ein Switch wo ein Paket hin versendet werden muss?
- Was ist ein Router
  - Was macht ein Router?
  - Wieso braucht es Router?
  - Woher weiss ein Router wo ein Paket hin versendet werden muss?

> Übung 1: Verwende den Befehl `ipconfig` (Windows Terminal / Powershell) um die IP Addresse deines Computers aus zu lesen. Was siehst du? Was kannst du mit dem Befehl alles erkennen?
>
> Übung 2: Verwende den Befehl `tracert` um herauszufinden in welchem Rechenzentrum die Webseite "www.moser-baer.ch" betrieben wird. Was siehst du alles in den Infos von tracert?

## Kapitel 4: Transport

Recherchiere folgende Fragen und schreiben ein Kapitel zum Thema TCP/UDP Transport in den Bericht.

- Was ist ein UDP Datagram? Wie ist es aufgebaut?
  - Wozu dienen die Port Nummern?
  - Wie gross kann ein UDP Datagramm maximal sein?
- Was ist TCP?
  - Wie können grosse Dateien übertragen werden?
  - Wie wird sicher gestellt dass keine Daten verloren gehen?
- Vergleiche TCP und UDP:
  - Was sind die wichtigsten Unterschiede?
  - Wann wird sinvollerweise TCP verwendet?
  - Wann wird sinvollerweise UDP verwendet?

## Kapitel 5: Applikation

- Wozu verwendest du das Internet? Welche Applikationen verwendest du?
- Was für Pakete werden versendet, wenn du diese Applikationen benutzt? Was sind die verwendeten Protokolle?

### Kapitel 5.1 Webseiten

- Webseiten verwenden HTTP. Was ist HTTP?
  - Wie ist ein HTTP Request aufgebaut?
  - Wie wird ein HTTP Request versendet?
  - Was ist eine URL?
- Was ist ein Browser?
- Was ist ein Webserver?
- Was ist html?
- Was ist CSS?
- Was ist Javascript?
- Wie hängen all diese Stichworte zusammen?
- Wie veröffentlicht man eine Webseite?

> Übung: Erstelle eine einfache Webseite über dich selbst. Es sollte ähnlich wie dein Lebenlauf aussehen, ein Passfoto, persönliche Angaben und deine Beruflich Laufbahn zeigen. Dazu verwendest du HTML und CSS. Beginne mit HTML und dem Inhalt der Seite. Später kannst mit CSS bestimmen, wie das Design aussehen soll. Verwende die Tutorials auf [www.w3schools.com](www.w3schools.com) um HTML und CSS zu lernen. Es reicht dabei aber jeweils die ersten paar Kapitel zu machen, es brauch nicht das komplette Tutorial.

### Kapitel 5.2 DNS

- Wie findest du die IP von google.ch?
- Was ist DNS, wie funktioniert es?
- Was ist eine Domain?
  - Was eine TLD?
  - Was ist eine Subdomain
- Wie erhält man eine eigene Domain?

### Kapitel 5.2 DHCP

- Was ist DHCP?
- Wieso ist es hilfreich?
- Was ist speziell an der Netzwerkaddresse 192.168.0.0/16?
- Wann braucht man eine statische, wann eine dynamische IP Addresse?

### Kapitel 5.3 TLS

- Was ist TLS?
- Wozu wird es verwendet?
- Was ist HTTPS?
- Inwiefern ist HTTPS sicherer als HTTP?

## Kapitel 5.4 OSI Referenzmodel

- Was ist das OSI Referenzmodell?
- Wozu dienst das Modell?

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
- Wozu verwendet wird Moser-Baer SNMP?

> Aufgabe: Finde und Decodiere ein SNP Paket mit Wireshark

### SSH

- Was ist SSH?
- Wozu verwendet DTS SSH?

> Aufgabe: Verbinde ich per SSH mit einem DTS und stelle die Uhrenline auf 12h
