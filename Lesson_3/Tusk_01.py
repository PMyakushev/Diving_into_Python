from collections import Counter


def find_duplicates(input_list):
    # Подсчитать количество встречаемых элементов
    element_count = Counter(input_list)

    # Вернуть список дубликатов без повторений
    duplicates = [item for item, count in element_count.items() if count > 1]

    return duplicates


# Пример использования
example_list = [1, 2, 3, 4, 5, 1, 2, 3, 6, 7, 8, 3]
duplicates = find_duplicates(example_list)
print(f"Дублирующиеся элементы: {duplicates}")
