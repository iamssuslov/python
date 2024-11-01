import os


def read_file(file_path: str):
    if not os.path.exists(file_path):
        raise FileNotFoundError('Файл не найден')

    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.readlines()
        for row in data:
            row = row.replace('\n', '', 1)
            if not row.isdigit():
                raise TypeError(f'Строка {row} содержит не только цифры')
            print(row)


if __name__ == '__main__':
    read_file('test.txt')
