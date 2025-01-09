import string
from collections import Counter


def count_words(text):
    # Убираем знаки препинания и приводим текст к нижнему регистру
    text = text.translate(str.maketrans("", "", string.punctuation)).lower()

    # Разбиваем текст на слова
    words = text.split()

    # Подсчитываем частоту слов
    word_count = Counter(words)

    # Находим 10 самых частых слов
    most_common = word_count.most_common(10)

    return most_common


# Пример использования
sample_text = """
Python is an interpreted, high-level and general-purpose programming language. 
Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability 
with the use of significant indentation. Its language constructs and object-oriented approach aim to help programmers 
write clear, logical code for small and large-scale projects.
"""

top_words = count_words(sample_text)
print("10 самых частых слов:", top_words)
