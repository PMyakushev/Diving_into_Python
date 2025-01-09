import os
import json
import csv
import pickle


def get_directory_info(directory):

    directory_info = []

    def process_directory(current_directory):
        total_size = 0  # Общий размер текущей директории

        for entry in os.scandir(current_directory):
            if entry.is_file():
                # Обработка файла
                size = entry.stat().st_size
                directory_info.append({
                    'name': entry.name,
                    'path': entry.path,
                    'parent_directory': current_directory,
                    'type': 'file',
                    'size': size
                })
                total_size += size
            elif entry.is_dir():
                # Обработка директории
                dir_size = process_directory(entry.path)
                directory_info.append({
                    'name': entry.name,
                    'path': entry.path,
                    'parent_directory': current_directory,
                    'type': 'directory',
                    'size': dir_size
                })
                total_size += dir_size

        return total_size

    # Рекурсивно обрабатываем указанную директорию
    process_directory(directory)
    return directory_info


def save_to_json(data, file_path):
    """
    Сохранение данных в файл JSON.

    :param data: Данные для сохранения.
    :param file_path: Путь к JSON-файлу.
    """
    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


def save_to_csv(data, file_path):
    """
    Сохранение данных в файл CSV.

    :param data: Данные для сохранения.
    :param file_path: Путь к CSV-файлу.
    """
    with open(file_path, 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


def save_to_pickle(data, file_path):
    """
    Сохранение данных в файл Pickle.

    :param data: Данные для сохранения.
    :param file_path: Путь к Pickle-файлу.
    """
    with open(file_path, 'wb') as pickle_file:
        pickle.dump(data, pickle_file)


def process_and_save(directory, output_prefix):

    # Собираем информацию о директории
    directory_info = get_directory_info(directory)

    # Сохраняем данные в JSON, CSV и Pickle файлы
    save_to_json(directory_info, f'{output_prefix}.json')
    save_to_csv(directory_info, f'{output_prefix}.csv')
    save_to_pickle(directory_info, f'{output_prefix}.pkl')


# Использование функции
if __name__ == "__main__":
    # Путь к директории
    directory = r"C:\Users\TEMP.HOME-PC.004\PycharmProjects\Diving_into_Python"

    # Префикс имени выходных файлов
    output_prefix = "directory_info"

    # Обработка и сохранение данных
    process_and_save(directory, output_prefix)
