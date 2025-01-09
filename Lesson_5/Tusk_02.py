def calculate_bonuses(names, rates, bonuses):
    return {name: rate * (float(bonus[:-1]) / 100) for name, rate, bonus in zip(names, rates, bonuses)}

# Пример использования
names = ["Alice", "Bob", "Charlie"]
rates = [1000, 1500, 2000]
bonuses = ["10.25%", "5.00%", "12.50%"]
bonus_dict = calculate_bonuses(names, rates, bonuses)
print(bonus_dict)  # {'Alice': 102.5, 'Bob': 75.0, 'Charlie': 250.0}
