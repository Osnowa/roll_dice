def score_minus(conn, id, sc_mov):
    """Списание очков"""
    cur = conn.cursor()

    cur.execute("""
        UPDATE users SET score = score - ? WHERE telegram_id = ?
    """, (sc_mov, id))

    conn.commit()

def user_is_game(conn, id, activ : int):
    """Активация or Деактивация игры пользователя"""
    cur = conn.cursor()

    cur.execute("""
        UPDATE users SET is_game = ? WHERE telegram_id = ?
    """, (activ, id))

    conn.commit()

