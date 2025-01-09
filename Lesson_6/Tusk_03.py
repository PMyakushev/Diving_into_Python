import random

def random_queen_positions():
    return [(i, random.randint(1, 8)) for i in range(1, 9)]

def find_successful_arrangements(count):
    successful_arrangements = []
    while len(successful_arrangements) < count:
        queens = random_queen_positions()
        if are_queens_attacking(queens):
            successful_arrangements.append(queens)
    return successful_arrangements

# Пример использования
successful_positions = find_successful_arrangements(4)
for index, arrangement in enumerate(successful_positions):
    print(f"Успешная расстановка {index + 1}: {arrangement}")
