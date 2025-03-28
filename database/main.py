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

def is_registered(job_id: str) -> bool:
    connection = sqlite3.connect("vagas.db")
    cursor = connection.cursor()

    cursor.execute('SELECT 1 FROM vagas WHERE id = ?', (job_id))
    result = cursor.fetchone()

    connection.close()

    return result is not None