import sqlite3
conn = sqlite3.connect("books.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    year TEXT,
    category TEXT
)
""")
books = [
    ("french_revolution", "tocqueville", "1856", ""),
    ("ten days", "john reed", "1919", ""),
    ("too_big_to_fail", "sorkin", "2009", ""),
    ("jp_morgan", "martin", "2022", ""),
    ("common sense", "paine", "1775", ""),
    ("finance", "libby", "idk..?", ""),
    ("grant", "grant", "1885", ""),
    ("state and revolution", "lenin", "1917", "bolshevism"),
    ("imperialism", "lenin", "1917", "bolshevism"),
    ("ochrana", "", "1917", "imperialists"),
    ("medici money", "", "2006", "imperialists"),
    ("practical idealism", "kalergi", "1925", "imperialists")
]
cursor.executemany("""
INSERT INTO books (title, author, year, category)
VALUES (?, ?, ?, ?)
""", books)
conn.commit()
conn.close()
print("Database created and books added!")