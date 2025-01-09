# Создайте файл chess.py
def are_queens_attacking(queens):
    rows = set()
    cols = set()
    diag1 = set()  # y = x + constant
    diag2 = set()  # y = -x + constant

    for x, y in queens:
        if x in cols or y in rows or (x + y) in diag1 or (x - y) in diag2:
            return False
        cols.add(x)
        rows.add(y)
        diag1.add(x + y)
        diag2.add(x - y)

    return True

# Пример использования
queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)]
print(are_queens_attacking(queens))  # Если ферзи не бьют друг друга, вернёт True
