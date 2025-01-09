def create_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        # Если ключ хешируем, используем его напрямую
        # Иначе используем строковое представление ключа
        try:
            result[key] = value
        except TypeError:
            result[str(key)] = value
    return result

# Пример использования
dictionary = create_dict(a=1, b=2, c=3, d=[1, 2, 3])
print(dictionary)  # {'a': 1, 'b': 2, 'c': 3, 'd': [1, 2, 3]}
