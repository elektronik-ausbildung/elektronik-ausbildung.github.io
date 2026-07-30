# Git Tutorial

## Empfohlene Tools

- Git [(Windows Download)](https://github.com/git-for-windows/git/releases/download/v2.33.0.windows.1/Git-2.33.0-64-bit.exe)
- Windows Terminal [(Microsoft Store)](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701#activetab=pivot:overviewtab)
- Sourcetree [(Download)](https://www.sourcetreeapp.com/)
- Visual Studio Code [(Download)](https://code.visualstudio.com/)
  - Extension "Markdown All in One"
  - Extension "Git Lens"

## Übersicht

![Version control is hard](images/essay-final-final.jpg)

- Herausforderung: Versionskontrolle
- Gitlab: Plattform für Softwareentwicklung (DevOps)
  - Projektmanagement
  - Versionskontrolle
    - Git!
  - Code Review Tool
  - Testautomation
  - Auto Deployment
  - Release Management
- Git
  - Versionskontrollsystem
  - Kollaborationssystem
  - Kommandozeilentool
    - Viele Client GUI verfügbar
    - Sourcetree ist ein Git Client GUI
- Git Flow ist ein Set von Abmachungen, wie man Git Branches verwendet

## Konzept

Viele Englische Begriffe

<img src=images/repository.svg width=60% >

- Repository 
  - Ordner / Lager für Dateien deren Änderungen nachverfolgt werden sollen
  - Hat einen oder mehrere Branches
  - Ich kann jeden beliebigen Stand auswählen

<img src=images/branch.svg width=60% >

- Branch
  - Ast / Abzweigung
  - Eine separate Version des Ordners / eine Kopie davon
  - So können mehrere Version unterschieden werden
  - Jeder kann jederzeit neue Äste abzweigen
- Commit
  - Beitrag
  - Ein Commit fügt einem Branch eine Änderung hinzu
  - Jeder kann beliebig viele Commits hinzufügen

<img src=images/merge.svg width=60% >

- Merge
  - Zusammenführen
  - Ich kann einen Branch mit einem anderen zusammenfügen
  - Achtung: Es kann zu Konflikten kommen

## Arbeiten mit Git

- Vorbereitung
  - `git config --global user.name "FIRST_NAME LAST_NAME"` Teilt git deinen Namen mit
  - `git config --global user.email "MY_NAME@example.com"` Hinterlegt deine Email Adresse
- `dir git-test-repo` Erstellt einen Ordner
- `cd git-test-repo` Wechsel in diesen Ordner
- `git init` verwandelt den Ordner in ein Git Repository
  - Nun haben wir ein lokales Repository
  - Davon eine lokale Kopie als Arbeitsplatz
- Damit das Repository funktionsfähg ist, müssen wir eine erste Datei hinzufügen
  - `echo "# Gitignore of the Test Repo" >> .gitignore`
  - `git status`
  - `git add .gitignore`
  - `git commit -m "Initialize repository with empty gitignore file"`
  - (zu diesen Kommandos später mehr)
- `git branch --list` Zeigt alle Branches: Der erste Branch heisst standardmässig `master`
- Wir erstellen einen neuen Branch mit Namen `develop`: `git branch develop`
- `git branch --list` Zeigt nun beide Branches, allerdings ist unser lokaler Arbeitsplatz immer noch auf `master`.
- `git checkout develop` Wechselt auf den `develop` branch.
- Mit `git status` überprüfen wir den Stand. Es gibt keine Änderungen und nun ist der Arbeitsplatz auf dem `develop` Stand
- Nun fügen wir neue Dateien hinzu, zum Beispiel ein `Readme.md`. Dort wird normalerweise das Projekt vorgestellt und alles wichtige erklärt.
- Mit `git status` sehen wir zu jeder Zeit, welche Dateien geändert wurden und welche Dateien neu hinzugefügt oder entfernt wurden.
- Wir müssen nicht alle Änderungen dem Repo hinzufügen, wir können auswählen, welche Änderungen wann hinzugefügt werden.
  - `git add Readme.md` verschiebt einzelne Dateien oder Ordner in den `staging` Bereich - sie werden so zum hinzufügen vorbereitet
  - `git reset Readme.md` entfernt diese wieder aus dem `staging` Bereich.
  - `git commit -m "Change something because of another thing` fügt alle Änderungen aus dem `staging` Bereich als Änderung oder Beitrag dem aktiven Branch hinzu.
  - `git diff` zeigt detailiert alle Änderungen.
- Nun kann ich beliebig lange weiter arbeiten und beliebig viele Commits machen
- Wenn ich fertig bin, kann ich alle Änderungen in den `master` Branch zurück führen. Dieser Vorgang nennt sich `merge`
  - Voraussetzung: Alle Änderungen wurden hinzugefügt oder rückgängig gemacht.
  - `git checkout master` Wechselt zurück zum `master` Branch.
  - `git merge develop` Fügt die Änderungen in von `develop` in den aktuellen Branch ein (hier `master`)
- Mit `git stash` kann ein beliebiger Stand auf die Seite gelegt werden.

### Sonderfall Merge Konflikt

- Git hat alle Änderungen im Griff
- Wenn in zwei Branches dieselben Zeilen geändert werden und diese Änderungen nicht identisch sind, kann Git die Branches nicht mergen. In dem Fall kann Git nicht wissen welche Änderung übernommen werden soll. Dieser Fall nennt man `Merge Konflikt` - Merge Konflikte müssen von hand gelöste werden.

### Welche Dateien gehören ins Repo

- Keine Generierten Dateien
- Wenn möglich nur Text-, keine Binärdateien
- Nicht erwünschte Files können in `.gitignore` Datei eingetragen werden und werden fortan ignoriert

### Git Commit Messages

Es ist wichtig, gute Commit Messages zu schreiben, so kann man anhand des Verlaufs die Entwicklung nachvollziehen.

- Gegenwartsform
- Keinen Punkt
- Kurze Beschreibung was/wieso

## Arbeiten mit Sourcetree

Das arbeiten mit Sourcetree funktioniert sehr ähnlich wie mit git auf der Kommandozeile. Es sind nämlich dieselben Vorgänge, nur anstelle einer CLI verwenden wir ein UI. Das ist praktisch, da vor allem Änderungen und die Commit Listen übersichtlich dargestellt werden.

## Arbeiten mit Gitlab (oder Github)

<img src=images/remote.svg width=60%>

Gitlab und Github sind ursprünglich Git Server - ein Weg Git Repositories mit anderen zu teilen. Heute machen sie noch viel mehr. Damit ein Repository auf Gitlab hinzugefügt werden kann, muss in Gitlab ein leeres Projekt erstellt werden. Dessen Link muss dann unserem Git Repository mitgeteilt werden.

- `git remote add origin https://mbs-git.mobatime.com/my-test-repo.git`
  - Das verbindet das lokale Repo mit demjenigen auf Gitlab
  - Nun hat unser (lokales) Repository ein Remote Repository
- Daten werden nicht automatisch ausgetauscht, die beiden Repositories sind grundsätzlich unabhängig.
- `git pull` lädt alle Änderungen für den aktuellen Branch aus dem Remote herunter
- `git push` fügt alle Änderungen auf dem lokalen Branch dem Remote hinzu
- Achtung: Bevor gepusht wird, sollte immer ein `git pull` gemacht werden, sonst kann es zu Konflikten kommen.
- Ein Repository kann mehre Remotes haben.
- `git clone <repo-url> <folder-path>` Erstellt eine lokale Kopie eis Repos auf Gitlab/Github.

### Merge Requests

- Merge Requests sind ein Gitlab Werkzeug um Änderungen zu kontrollieren und zu diskutieren
- Will ich einen eigenen Branch in den develop branch mergen, erstelle ich einen Merge Request. Es ist eine Art Anfrage "Ist es ok, wenn wenn ich diese Änderungen einfüge." Die Idee ist, dass jemand anderes den Code anschauen und kontrollieren kann, bevor er eingefügt wird.

### Projekt Planung

- Gitlab hat eingebaute Funktionen zur Projektplanung
  - Issues sind Aufgabenpakete
  - Milestones sind Gruppen von Issues
- Issues können mit Labels organisiert werden
- Boards können den aktuellen Stand zeigen

### Gitlab Struktur bei Moser-Baer

- Gruppe mit Projektnamen
- Einzelne Projekte für Teilaufgaben
  - Dokumentation
  - Hardware
  - Firmware

## Arbeiten im Team

### Git-flow

Abmachungen in einem Team wie man mit Branches umgeht.
Gute Erklärung von [Atlassian](https://www.atlassian.com/de/git/tutorials/comparing-workflows/gitflow-workflow)

<img src="images/Release%20branches.svg" width="60%">

#### Master Branch (manchmal auch Main genannt)

- Funktionierender Code / Release Versionen
- Hier wird nicht gearbeitet
- Hier sollte es keine Fehler geben

#### Develop Branch

- Hier fliessen laufend alle Änderungen ein
- Funktionsfähiger Stand, aber nicht eingehend getestet

#### Feature Branch und Fix Branch

- Soll ich was ändern, öffne ich pro Feature oder pro Bug einen neuen Branch
- Für jeden Schritt der Arbeit mache ich einen Commit mit Beschreibung
- Sobald die Aufgabe fertig ist, wird mein Branch in den Develop Branch gemergt

#### Release Branch

- Soll eine Version veröffentlicht werden, wird vom Master Branch ein Release Branch abgezweigt
  - Dieser Branch wird eingehen getestet
- Fehler werden geflickt
- Wenn alles funktioniert, wird der Release Branch in den Master Branch gemergt
- Zusätzlich wird der Release Branch zurück in den Develop Branch gemergt

#### Sonderfall Hotfix Branch

- Notfallmässiges beheben von schweren Fehlern
- Abzweigung vom Master
- Fix
- Test
- In den Master zurück führen
- Ebenfalls in develop zurück führen

## Checkliste neues Repo

- Gitlab Projekt erstellen
- Branching Modell wählen
  - Branches erstellen
- `.gitignore` Datei erstellen
- `Readme.md` erstellen, Projekt dokumentieren
- Wenn nötig `Changelog.md` erstellen
- Wenn nötig `.gitlab-ci` erstellen
