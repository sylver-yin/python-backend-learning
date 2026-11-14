def make_album(user, artist, album_title, song_quantity=None):
    """Returns information about music albums as dictionary."""
    if song_quantity:
        album_info = {
            "user": user,
            "artist": artist,
            "album title": album_title,
            "number of songs": song_quantity,
        }
    else:
        album_info = {"user": user, "artist": artist, "album title": album_title}
    return album_info


while True:
    print("\nHello! Please, enter information about your favorite album!")
    print("(enter 'q' at any step to quit.)")

    username = input("Please, write down your nickname or your real name: ")
    if username == "q":
        break
    artist_name = input("Please, write down artist's nickname or their real name: ")
    if artist_name == "q":
        break
    album_name = input("Please, write down the album's title: ")
    if album_name == "q":
        break
    song_number_optional = input(
        "Please, write down the number of songs in this album (optional, skip by pressing Enter if you don't want to): "
    )
    if song_number_optional == "q":
        break

    album_info_gathered = make_album(
        username, artist_name, album_name, song_number_optional
    )
    print(album_info_gathered)
