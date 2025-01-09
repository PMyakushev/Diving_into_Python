def int_to_hex(num):
    # Проверяем, что число является целым
    if not isinstance(num, int):
        raise ValueError("Input must be an integer")

    # Преобразуем в шестнадцатеричное представление с применением встроенной функции
    hex_value = hex(num)
    return hex_value


# Пример использования
number = 255  # Замените на любое целое число
hex_result = int_to_hex(number)
print(f"Шестнадцатеричное представление {number}: {hex_result}")

# Проверка с помощью встроенной функции hex()
print(f"Проверка с встроенной функцией: {hex(number)}")
