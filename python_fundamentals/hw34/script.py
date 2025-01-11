# 1. Напишите функцию extract_emails(text), которая извлекает все адреса электронной почты из заданного текста и возвращает их в виде списка.
from re import findall


def extract_emails(text: str):
    pattern = r'\b[\w%.-]+@[\w\.-]+\.[\w]{2,}\b'
    return findall(pattern, text)


text = "Contact us at info@example.c_om or support@example.com for assistance."

emails = extract_emails(text)
print(emails)  # Вывод: ['info@example.com', 'support@example.com']

# 2. Напишите функцию highlight_keywords(text, keywords), которая выделяет все вхождения заданных ключевых слов в тексте,
# окружая их символами *.
# Функция должна быть регистронезависимой при поиске ключевых слов.
import re


def highlight_keywords(text, search_list):
    for keyword in search_list:
        keyword = fr"\b({keyword})\b"
        text = re.sub(keyword, r'*\1*', text, flags=re.IGNORECASE)

    return text


text = "This is a sample text. We need to highlight Python and programming."
keywords = ["python", "programming"]

highlighted_text = highlight_keywords(text, keywords)
print(highlighted_text)

# Вывод: "This is a sample text. We need to highlight *Python* and *programming*."
