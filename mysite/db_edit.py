import sqlite3
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1500)
headers = ['id', 'title', 'author', 'year wrote', 'page', 'part', 'page min', 'total audio', 'total text', 'pages left', '% done', 'hours left', 'hours left done', 'total words (k)', 'pdf url', 'col16', 'col17', 'col18', 'col19']
conn = sqlite3.connect('books.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM books")
rows = cursor.fetchall()
conn.close()
df = pd.DataFrame(rows, columns=headers[:len(rows[0])])
print(df)
