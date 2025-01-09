from fractions import Fraction


def add_and_multiply_fractions(fraction1, fraction2):
    # Преобразуем строки в дроби
    frac1 = Fraction(fraction1)
    frac2 = Fraction(fraction2)

    # Вычисляем сумму и произведение дробей
    sum_result = frac1 + frac2
    product_result = frac1 * frac2

    return sum_result, product_result


# Пример использования
frac1 = "1/2"  # Замените на нужные дроби
frac2 = "3/4"
sum_fractions, product_fractions = add_and_multiply_fractions(frac1, frac2)

print(f"Сумма дробей {frac1} и {frac2}: {sum_fractions}")
print(f"Произведение дробей {frac1} и {frac2}: {product_fractions}")

# Проверка с использованием модуля fractions
# Убедимся, что результат соответствует ожидаемым
expected_sum = Fraction(frac1) + Fraction(frac2)
expected_product = Fraction(frac1) * Fraction(frac2)
assert sum_fractions == expected_sum, "Сумма дробей неверна"
assert product_fractions == expected_product, "Произведение дробей неверно"
