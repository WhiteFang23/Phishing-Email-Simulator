import sqlite3

conn = sqlite3.connect("database/phishing.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT,
    clicked INTEGER,
    timestamp TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully")
