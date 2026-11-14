def make_album(artist, album_title, song_quanity=None):
    """Returns information about music albums as dictionary."""
    if song_quanity:
        album_info = {
            "artist": artist,
            "album title": album_title,
            "number of songs": song_quanity,
        }
    else:
        album_info = {"artist": artist, "album title": album_title}
    return album_info


album = make_album("Mitski", "Be the cowboy")
print(album)
album = make_album("Lemon Demon", "Nature tapes")
print(album)
album = make_album("Andrew Prahlow", "Outer Wilds (Original Soundtrack)", 28)
print(album)
