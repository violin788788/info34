import pandas as pd
import sqlite3
df = pd.read_excel("books.xlsx")
conn = sqlite3.connect("books.db")
df.to_sql("books", conn, if_exists="replace", index=False)
conn.close()