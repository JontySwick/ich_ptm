# 2. Напишите программу, которая принимает в качестве аргумента командной строки путь к директории и выводит список всех файлов и поддиректорий внутри этой директории.
# Для этой задачи используйте модуль os и его функцию walk.
# Программа должна выводить полный путь к каждому файлу и директории.

import argparse
import os

parser = argparse.ArgumentParser(prog='Directory scaner',
                                 description='Scan directory and print all files and subdirectories')
parser.add_argument('-dir', help='Path to directory for scan', required=True, metavar='/path/to/file')
path_to_scan_directory = parser.parse_args().dir

base_shift = os.path.abspath(path_to_scan_directory).count(os.path.sep) - 1

for path, directories, files in os.walk(path_to_scan_directory):
    # На случай если передан относительный путь, превращаем его в абсолютный
    absolute_path = os.path.abspath(path)
    shift_for_print = absolute_path.count(os.path.sep) - base_shift

    print('\t' * (shift_for_print - 1), absolute_path)

    for file in files:
        print('\t' * shift_for_print, os.path.join(absolute_path, file))
