import sqlite3
from pathlib import Path

# путь до файла
db_path = Path(__file__).parent / 'bot.db'

def connect_db(path:str = None):
    """Подключение к базе данных"""
    if path is None:
        path = db_path

    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row # словарь
    return conn

    