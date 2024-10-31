# Напишите программу, которая принимает список слов и возвращает список, содержащий только анаграммы.
# Анаграммы - это слова, составленные из одних и тех же букв, но в разном порядке.
# Создайте функцию anagrams, которая принимает список слов в качестве аргумента и возвращает список анаграмм.
# Используйте множества и сортировку букв в слове для проверки на анаграмму. Выведите результат на экран.

def anagrams(words):
    main_result = []

    while len(words) > 1:
        needle = words[0]
        sorted_needle = str(sorted(list(needle)))
        needle_result = []
        i = 1
        while len(words) > i:
            word = words[i]
            sorted_word = str(sorted(list(word)))
            if sorted_word == sorted_needle:
                needle_result.append(word)
                del words[i]
            else:
                i += 1

        if needle_result:
            needle_result.insert(0, needle)
            main_result.append(needle_result)

        del words[0]

    return main_result


print('Анаграммы:', anagrams(input('Введите слова через пробел: ').split()))  # ['dog', 'god'], ['cat', 'tac', 'act']


# Напишите функцию is_subset, которая принимает два множества set1 и set2 и проверяет, является ли set1 подмножеством set2.
# Функция должна возвращать True, если все элементы из set1 содержатся в set2, и False в противном случае.
# Функция должна быть реализована без использования встроенных методов issubset или <=.

# {1, 2, 3}

# {1, 2, 3, 4, 5}

def is_subset(set1, set2):
    for el in set1:
        if el not in set2:
            return False

    return True


print(is_subset({1, 2, 3}, {1, 2, 3, 4, 5}))
print(is_subset({1, 2, 7}, {1, 2, 3, 4, 5}))
