import os
import json
import csv
import pickle


def get_directory_info(root_dir):
    directory_info = []

    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Считаем размер файлов в текущей директории
        total_size = sum(os.path.getsize(os.path.join(dirpath, f)) for f in filenames)

        # Сохранение информации о директории
        directory_info.append({
            'name': os.path.basename(dirpath),
            'path': dirpath,
            'type': 'directory',
            'size': total_size,
            'parent': os.path.basename(os.path.dirname(dirpath)) if os.path.dirname(dirpath) else None
        })

        # Сохранение информации о файлах
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            directory_info.append({
                'name': filename,
                'path': filepath,
                'type': 'file',
                'size': os.path.getsize(filepath),
                'parent': os.path.basename(dirpath)
            })

    return directory_info


def save_to_json(data, output_file):
    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=4)


def save_to_csv(data, output_file):
    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


def save_to_pickle(data, output_file):
    with open(output_file, 'wb') as pickle_file:
        pickle.dump(data, pickle_file)


def main(root_dir, json_file, csv_file, pickle_file):
    directory_info = get_directory_info(root_dir)
    save_to_json(directory_info, json_file)
    save_to_csv(directory_info, csv_file)
    save_to_pickle(directory_info, pickle_file)
