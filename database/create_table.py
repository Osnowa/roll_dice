from database import db_conncet

def init_db() -> None:
    """Создание таблицы"""
    with db_conncet.connect_db(db_conncet.db_path) as conn:
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                telegram_id int UNIQUE,
                is_game int DEFAULT 0,
                score int DEFAULT 100
            )
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS users_stats (
                user_id INTEGER PRIMARY KEY ,
                games_win int DEFAULT 0,
                games_loss int DEFAULT 0,
                games_draw int DEFAULT 0,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        """)

        conn.commit()