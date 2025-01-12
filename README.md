# geheimnisvollesquiz

Ein "Die drei ???" Ratespiel, in dem ein Ausschnitt aus einem zufälligen Fall
abgespielt wird.
Schaffst du es den Fall zu erkennen?

## Installation

### Python Code lokal ausführen

Hierfür wird folgendes benötigt:

- Spotify-Account
- [python](https://www.python.org/downloads/) inklusive Paketmanager pip
- [git](https://git-scm.com/downloads)

Anschließend kann dieses Ratespiel mit dem python-Paketmanager pip installiert werden:

```bash
pip install git+https://github.com/afloetotto/geheimnisvollesquiz.git#egg=geheimnisvollesquiz
```

Nach der Installation sollte der Befehl `quiz` im Terminal verfügbar sein.
Wichtig hierfür ist, dass der Order `<Pfad zu python Installation>/Scripts` in
der Umgebungsvariable `PATH` enthalten ist.
Dies sollte normalerweise bei der python Installation automatisch eingerichtet werden.

Alternativ zur Installation als python Paket kann dieses repository heruntergeladen
werden und die Datei ``quiz.py`` mit der lokalen python Installation ausgeführt werden.
Mit den folgenden Befehlen wird das Programm im aktuellen Arbeitsverzeichnis
gespeichert.

```bash
git clone https://github.com/afloetotto/geheimnisvollesquiz.git
python geheimnisvollesquiz/src/geheimnisvollesquiz/quiz.py
```

### Als eigenständiges Programm

Hierfür wird nur ein Spotify-Account benötigt.
Im Ordner `dist/` befindet sich eine unter Linux ausführbare Datei namens `quiz`.
Diese kann heruntergeladen und direkt im Terminal ausgeführt werden.
Damit das in jedem Ordner funktioniert kann der Speicherort der Datei der
Umgebungsvariable `PATH` hinzugefügt werden.

## Nutzung

[Öffne Spotify in deinem Browser](https://open.spotify.com/) und melde dich an.
Vor dem ersten Quiz in einer "Sitzung" solltest du vielleicht irgendein Lied
kurz starten und dann wieder pausieren.
Dann minimiere das Browser-Fenster, um nicht zu schummeln!
Das Quiz kann nun wie oben unter der ausgewählten Installationsmethode beschrieben gestartet werden.
