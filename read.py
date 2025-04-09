import sqlite3

# Connect to your database
conn = sqlite3.connect('music_player.db')
cursor = conn.cursor()

# Fetch all songs
cursor.execute('SELECT song_id, title, artist, album, genre, length FROM songs')
songs = cursor.fetchall()

# Show results
if songs:
    print("\n🎵 Songs in your Music Library:\n")
    for song in songs:
        song_id, title, artist, album, genre, length = song
        print(f"[{song_id}] {title} by {artist} | Album: {album} | Genre: {genre} | Length: {length}")
else:
    print("😕 No songs found in your database.")

conn.close()
