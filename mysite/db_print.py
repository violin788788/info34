

import sqlite3
conn = sqlite3.connect('books.db')
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
for table_name in tables:
    name = table_name[0]
    print(f"\n=== TABLE: {name} ===")
    cursor.execute(f"SELECT * FROM {name}")
    headers = tuple(desc[0] for desc in cursor.description)
    print(headers)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
conn.close()



"""
import sqlite3
# 1. Connect to the database
conn = sqlite3.connect('books.db')
cursor = conn.cursor()
# 2. Get a list of all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
# 3. Print the data from each table
for table_name in tables:
    name = table_name[0]
    print(f"\n=== TABLE: {name} ===")
    cursor.execute(f"SELECT * FROM {name}")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
# 4. Close the connection
conn.close()
"""