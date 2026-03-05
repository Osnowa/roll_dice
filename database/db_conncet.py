import sqlite3
from pathlib import Path

# путь до файла
db_path = Path(__file__).parent / 'bot.db'

def connect_db(path:str):
    """Подключение к базе данных"""
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row # словарь
    return conn

