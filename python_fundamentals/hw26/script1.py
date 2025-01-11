# 1. Напишите программу, которая принимает в качестве аргумента командной строки путь к файлу .py и запускает его.
# При запуске файла программа должна выводить сообщение "Файл <имя файла> успешно запущен".
# Если файл не существует или не может быть запущен, программа должна вывести соответствующее сообщение об ошибке.
import argparse
import os
import sys

parser = argparse.ArgumentParser(prog='Strange py file executer', description='Execute your py file')
parser.add_argument('-f', help='Path to file for execute', required=True, metavar='path_to_file.py')

file_name = parser.parse_args().f

if not file_name.endswith('.py'):
    sys.exit('File should be .py')

if os.system(f'python3 {file_name}') == 0:
    print('File successfully executed!')
