import sqlite3

conn = sqlite3.connect("books.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    year INTEGER,
    part INTEGER,
    current_page INTEGER,
    total_pages INTEGER,
    words_per_minute INTEGER,

    drive_url TEXT,
    book_url TEXT,
    pdf_url TEXT,

    category TEXT,
    notes TEXT
)
""")

conn.commit()
conn.close()

print("Database created!")