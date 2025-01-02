import re
import random
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set up your Spotify API credentials
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id="2fc4b29950a24743be7406619a2c7523",
        client_secret="da24a21f6fdf4c6fbc76c51f2ecbf771",
        redirect_uri="http://localhost:8888/callback",
        scope="user-read-playback-state,user-modify-playback-state",
    )
)


def get_artist_id(artist_name):
    results = sp.search(q="artist:" + artist_name, type="artist")
    items = results["artists"]["items"]
    if len(items) > 0:
        return items[0]["id"]
    else:
        return None


def filter_albums(album_list):
    """
    Filter album list for unique albums and albums that are
    a audio play and not an audio book.
    """
    album_list_new = []
    seen_album_names = set()
    for album in album_list:
        if album["name"] not in seen_album_names:
            if not re.search(r".+liest.*\.\.\..+", album["name"]):
                album_list_new.append(album)
            seen_album_names.add(album["name"])
    return album_list_new


def get_random_album(artist_id):
    album_list = []
    limit = 50
    i_max = 10
    print("(frage höchstens 500 Alben ab)")
    for i in range(i_max):
        albums = sp.artist_albums(
            artist_id, album_type="album", limit=limit, offset=i * limit
        )
        album_list += albums["items"]
    album_list = filter_albums(album_list)
    if len(album_list) > 0:
        return random.choice(album_list)
    else:
        return None


def play_random_song_from_album(album_id, device_id):
    # Get the tracks from the album
    tracks = sp.album_tracks(album_id)
    track_uris = [track["uri"] for track in tracks["items"]]

    # Select a random track
    random_track_uri = random.choice(track_uris)

    # Start playback on the specified device with the random track
    sp.start_playback(device_id=device_id, uris=[random_track_uri])


def user_interface(album_name, device_id):
    """
    Hi! I'm the most intricate and intuitive user interface to ever enter this world lol
    """
    answer = ""
    while answer.lower() != "a":
        answer = input("Wähle p (pausieren), w (weiterspielen) oder a (auflösen): ")
        if answer.lower() == "a":
            print(f'Der Ausschnitt stammt aus "{album_name}".')
        elif answer.lower() == "p":
            sp.pause_playback(device_id=device_id)
        elif answer.lower() == "w":
            sp.start_playback(device_id=device_id)


def get_device_id():
    devices = sp.devices()
    if len(devices["devices"]) == 0:
        print("No devices found")
        return None
    return devices["devices"][0]["id"]


def main():
    artist_name = "Die drei ???"
    artist_id = get_artist_id(artist_name)
    device_id = get_device_id()
    if artist_id:
        album = get_random_album(artist_id)
        if album:
            print('Aus welchem "Die drei ???"-Hörspiel stammt dieser Ausschnitt?')
            # play a random song
            play_random_song_from_album(album["id"], device_id)
            # let the user decide when to see the album title
            user_interface(album["name"], device_id)
            # pause the song
            sp.pause_playback(device_id=device_id)
        else:
            print("No albums found for this artist.")
    else:
        print("Artist not found.")


if __name__ == "__main__":
    main()
    # id = get_artist_id(artist_name)
    # get_random_album(id)
