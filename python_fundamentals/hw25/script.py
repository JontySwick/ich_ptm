# 1. Напишите функцию find_longest_word, которая будет принимать список слов и возвращать самое длинное слово из списка.
# Аннотируйте типы аргументов и возвращаемого значения функции.

def find_longest_word(word_list: list[str]) -> str:
    return max(word_list, key=len)


words = ["apple", "banana", "cherry", "dragonfruit"]

result = find_longest_word(words)

print(result)  # Ожидаемый вывод: "dragonfruit"



# 2. Напишите программу, которая будет считывать данные о продуктах из файла и использовать аннотации типов для аргументов и возвращаемых значений функций.
# Создайте текстовый файл "products.txt", в котором каждая строка будет содержать информацию о продукте в формате "название, цена, количество"
# В программе определите функцию calculate_total_price, которая будет принимать список продуктов и возвращать общую стоимость.
# Продумайте, какая аннотация должна быть у аргумента! Считайте данные из файла, разделите строки на составляющие и создайте список продуктов.
# Затем вызовите функцию calculate_total_price с этим списком и выведите результат.

def import_list_from_file(file_name: str) -> list:
    result_list = list()
    with open(file_name, 'r', encoding="utf-8") as rows:
        for row in rows:
            result_list.append(row.replace(' ', '').split(','))

    return result_list

def calculate_total_price(product_list: list) -> float:
    total_price = 0
    for _, p, k in product_list:
        total_price += float(p) * float(k)

    return total_price


print(calculate_total_price(import_list_from_file('products.txt')))