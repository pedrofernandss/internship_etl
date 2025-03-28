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

def save_data(job_id: str, title: str, link: str, company_name: str, created_at: str):
    connection = sqlite3.connect("vagas.db")
    cursor = connection.cursor()

    cursor.execute('''
    INSERT INTO vagas (id, title, description, link, company_name, created_at)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (job_id, title, description, link, company_name, created_at))
    
    connection.commit()
    connection.close()