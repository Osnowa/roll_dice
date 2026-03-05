from database import users_add_get

def register_user(tg_id: int, conn):
    """Регистрация пользователя"""
    user = users_add_get.get_user(conn, tg_id)
    if user: # Если пользователь найден
        return False
    else:
        users_add_get.add_users(conn, tg_id)
        user = users_add_get.get_user(conn, tg_id)
        users_add_get.add_users_stats(conn, user["id"])
        return True
