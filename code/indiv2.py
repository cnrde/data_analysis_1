# Автоматическая проверка орфографии не помешала бы многим из нас. В данном
# упражнении мы напишем простую программу, сверяющую слова из текстового файла со
# словарем. Неправильно написанными будем считать все слова, которых не нашлось в
# словаре. Имя файла, в котором требуется выполнить орфографическую проверку,
# пользователь должен передать при помощи аргумента командной строки. В случае
# отсутствия аргумента должна выдаваться соответствующая ошибка. Сообщение об ошибке
# также должно появляться, если не удается открыть указанный пользователем файл. Также
# Вам следует игнорировать регистр символов при выполнении проверки.

import os
import sys

def load_dictionary(file_path):
    dictionary = set()
    with open(file_path, "r") as file:
        for line in file:
            dictionary.add(line.strip().lower())
    return dictionary

def spell_check(file_path, dictionary):
    misspelled_words = set()
    with open(file_path, "r") as file:
        for line in file:
            words = line.split()
            for word in words:
                if word.lower() not in dictionary:
                    misspelled_words.add(word)
    return misspelled_words

if len(sys.argv) < 2:
    print("Ошибка: Укажите путь к файлу в аргументе командной строки.")
    sys.exit(1)

file_path = sys.argv[1]
if not os.path.exists(file_path):
    print(f"Ошибка: Файл {file_path} не найден.")
    sys.exit(1)

try:
    dictionary = load_dictionary("slovar_indiv2.txt")  # Путь к файлу со словарем
    misspelled_words = spell_check(file_path, dictionary)
    if misspelled_words:
        print("Неправильно написанные слова:")
        for word in misspelled_words:
            print(word)
    else:
        print("Все слова в файле находятся в словаре.")
except FileNotFoundError:
    print(f"Ошибка: Не удается открыть файл {file_path}.")
