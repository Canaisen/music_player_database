import sqlite3

conn = sqlite3.connect('music_player.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM songs')
rows = cursor.fetchall()

print("\n🎧 Songs in your database:")
for row in rows:
    print(row)

conn.close()
