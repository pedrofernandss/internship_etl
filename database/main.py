import sqlite3

connection = sqlite3.connect("vagas.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS vagas (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    link TEXT NOT NULL,
    company_name TEXT NOT NULL,
    created_at TEXT NOT NULL,   
)
''')

connection.commit()
connection.close()