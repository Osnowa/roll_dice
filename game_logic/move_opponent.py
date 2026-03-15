import random


def move_opponent() -> (int, int):
    """Ход противника"""
    bons1 = random.randint(1, 6)
    bons2 = random.randint(1, 6)
    return bons1, bons2


def move_me() -> (int, int):
    """Наш ход"""
    bons1 = random.randint(1, 6)
    bons2 = random.randint(1, 6)
    return bons1, bons2


def result_game() -> bool | str:
    """Результат игры"""
    m_o = sum(move_opponent())
    m_u = sum(move_me())
    if m_u > m_o:
        return True
    elif m_u == m_o:
        return "draw"
    else:
        return False
