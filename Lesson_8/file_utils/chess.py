def are_queens_attacking(queens):
    rows = set()
    cols = set()
    diag1 = set()
    diag2 = set()

    for x, y in queens:
        if x in cols or y in rows or (x + y) in diag1 or (x - y) in diag2:
            return False
        cols.add(x)
        rows.add(y)
        diag1.add(x + y)
        diag2.add(x - y)

    return True
