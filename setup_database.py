import sqlite3

conn = sqlite3.connect("maintenance.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS maintenance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    aircraft TEXT NOT NULL,
    task TEXT NOT NULL,
    status TEXT NOT NULL,
    date TEXT NOT NULL
)
""")

conn.commit()
conn.close()
print("Database dan tabel berhasil dibuat!")