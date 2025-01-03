# geheimnisvollesquiz

Ein "Die drei ???" Ratespiel, in dem ein Ausschnitt aus einem zufälligen Fall
abgespielt wird.
Schaffst du es, den Fall zu erkennen?

## Installation

### Als python Paket

Hierbei wird folgendes benötigt:

- Spotify-Account
- [python](https://www.python.org/downloads/) inklusive Paketmanager pip
- [git](https://git-scm.com/downloads)

Anschließend kann dieses Ratespiel mit dem python-Paketmanager pip installiert werden:

```bash
pip install git+https://github.com/afloetotto/geheimnisvollesquiz.git#egg=geheimnisvollesquiz
```

### Als eigenständiges Programm

Im Ordner `dist/` befindet sich eine unter Linux ausführbare Datei namens `quiz`.
Diese kann heruntergeladen und direkt im Terminal ausgeführt werden.
Um das in jedem Ordner machen zu können sollte der Speicherort der Datei der
Umgebungsvariable `PATH` hinzugefügt werden.

## Nutzung

[Öffne Spotify in deinem Browser](https://open.spotify.com/) und melde dich an.
Vor dem ersten quiz in einer "Sitzung" solltest du vielleicht irgendein Lied
kurz starten und dann wieder pausieren.
Dann minimiere das Browser-Fenster, um nicht zu schummeln!
Das Quiz kann nun über den Befehl `quiz` in einem Terminal gestartet werden.
