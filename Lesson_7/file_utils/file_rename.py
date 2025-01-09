import os


def rename_files(target_name, count_digits, source_ext, target_ext, name_range):
    current_directory = os.getcwd()
    files = [f for f in os.listdir(current_directory) if f.endswith(source_ext)]

    for index, original_file in enumerate(files, start=1):
        original_name = os.path.splitext(original_file)[0]
        original_part = original_name[name_range[0] - 1:name_range[1]]
        new_name = f"{original_part}{target_name}{str(index).zfill(count_digits)}{target_ext}"

        old_file_path = os.path.join(current_directory, original_file)
        new_file_path = os.path.join(current_directory, new_name)

        os.rename(old_file_path, new_file_path)
        print(f"Переименован '{original_file}' в '{new_name}'")
