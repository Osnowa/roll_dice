def add_users(conn, telegram_id):
    """Добавление пользователя"""
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO users (telegram_id) VALUES (?)
    """, (telegram_id,))

    conn.commit()


def add_users_stats(conn, user_id):
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO users_stats (user_id) VALUES (?)
    """, (user_id,))

    conn.commit()


def get_user(conn, telegram_id):
    """Получение пользователя"""
    cur = conn.cursor()

    cur.execute("""
        SELECT * FROM users WHERE telegram_id = (?)
    """, (telegram_id,))

    row = cur.fetchone()
    return row
