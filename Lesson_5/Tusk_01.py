import os

def parse_file_path(file_path):
    # Используем os.path для разбора пути
    directory, file_name = os.path.split(file_path)
    name, extension = os.path.splitext(file_name)
    return (directory, name, extension)

# Пример использования
file_path = "/home/user/documents/example.txt"
result = parse_file_path(file_path)
print(result)  # ('/home/user/documents', 'example', '.txt')
