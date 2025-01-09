import os


def rename_files(target_name, count_digits, source_ext, target_ext, name_range):
    # Получаем текущую директорию
    current_directory = os.getcwd()

    # Собираем все файлы в директории с заданным исходным расширением
    files = [f for f in os.listdir(current_directory) if f.endswith(source_ext)]

    for index, original_file in enumerate(files, start=1):
        # Получаем оригинальное имя файла без расширения
        original_name = os.path.splitext(original_file)[0]

        # Извлекаем диапазон индексов из оригинального имени
        original_part = original_name[name_range[0] - 1:name_range[1]]  # Индексы от 1, поэтому -1 для корректировки

        # Формируем новое имя файла
        new_name = f"{original_part}{target_name}{str(index).zfill(count_digits)}{target_ext}"

        # Полный путь к файлам
        old_file_path = os.path.join(current_directory, original_file)
        new_file_path = os.path.join(current_directory, new_name)

        # Переименование файла
        os.rename(old_file_path, new_file_path)
        print(f"Переименован '{original_file}' в '{new_name}'")


# Пример использования
rename_files(
    target_name="_new",
    count_digits=3,
    source_ext=".txt",
    target_ext=".md",
    name_range=(3, 6)
)