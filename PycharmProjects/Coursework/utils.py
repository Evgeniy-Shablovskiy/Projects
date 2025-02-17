import json
import random
from basic_word import BasicWord


def read_json():  # возвращает словарь
    with open("words.json", "r", encoding='UTF-8') as words:
        words_ = json.load(words)
    return words_


def load_random_word(words_):  # Возвращает объект с оригинальным словом и набор допустимых значений
    word_from_dict = random.sample(words_, 1)  # выбираем случайный словарь из списка
    basic_word_ = BasicWord(word_from_dict[0]["word"], word_from_dict[0]["subwords"])  # помещаем в объект ориг. слово и допусттмые значения
    return basic_word_
