import sqlite3

conn = sqlite3.connect('music_player.db')
cursor = conn.cursor()

# New song data
new_song = ('Thunder', 'Imagine Dragons', 'Evolve', 'Rock', '3:07', '/music/thunder.mp3')

# Check if the song already exists (based on title + artist)
cursor.execute('''
    SELECT * FROM songs WHERE title = ? AND artist = ?
''', (new_song[0], new_song[1]))

existing_song = cursor.fetchone()

if existing_song:
    print(f"⚠️ Song '{new_song[0]}' by {new_song[1]} already exists. Skipping insert.")
else:
    cursor.execute('''
        INSERT INTO songs (title, artist, album, genre, length, file_path)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', new_song)
    conn.commit()
    print(f"✅ Song '{new_song[0]}' inserted successfully!")

conn.close()
