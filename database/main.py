import sqlite3

connection = sqlite3.connect("database/vagas.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS vagas (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    link TEXT NOT NULL,
    company_name TEXT NOT NULL,
    created_at TEXT NOT NULL
)
''')

connection.commit()
connection.close()

def is_registered(job_id: str) -> bool:
    connection = sqlite3.connect("database/vagas.db")
    cursor = connection.cursor()

    cursor.execute('SELECT 1 FROM vagas WHERE id = ?', (job_id,))
    result = cursor.fetchone()

    connection.close()

    return result is not None

def save_data(data: dict):
    connection = sqlite3.connect("database/vagas.db")
    cursor = connection.cursor()

    cursor.execute('''
    INSERT INTO vagas (id, title, link, company_name, created_at)
    VALUES (?, ?, ?, ?, ?)
    ''', (data['id'], data['title'],
          data['link'], data['company_name'], data['created_at']))
    
    connection.commit()
    connection.close()