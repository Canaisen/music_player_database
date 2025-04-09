import sqlite3

conn = sqlite3.connect('music_player.db')
cursor = conn.cursor()

cursor.execute('DELETE FROM playlist_songs')
cursor.execute('DELETE FROM playlists')
cursor.execute('DELETE FROM songs')
cursor.execute('DELETE FROM playback_history')

conn.commit()
conn.close()

print("🔄 Tables cleared!")
