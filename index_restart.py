import sqlite3

conn = sqlite3.connect('music_player.db')
cursor = conn.cursor()

# Drop all tables (CAUTION: permanent!)
cursor.execute('DROP TABLE IF EXISTS playback_history')
cursor.execute('DROP TABLE IF EXISTS playlist_songs')
cursor.execute('DROP TABLE IF EXISTS playlists')
cursor.execute('DROP TABLE IF EXISTS songs')

# Recreate the tables (example for songs only)
cursor.execute('''
    CREATE TABLE songs (
        song_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        artist TEXT,
        album TEXT,
        genre TEXT,
        length TEXT,
        file_path TEXT
    )
''')

conn.commit()
conn.close()
print("💥 Tables dropped and recreated. You can now insert fresh songs starting from ID 1.")
