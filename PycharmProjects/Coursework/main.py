from player import Player
from utils import read_json, load_random_word


def game():
    words_ = read_json()  # получаем список
    basic_word_ = load_random_word(words_)  # получаем объект класса basic_word
    count_words = basic_word_.count_of_valid_words()  # получаем кол-во правильных значений
    user_name = input("Введите имя игрока: ")  # Запрашиваем имя пользователя
    player = Player(user_name, [])  # Создаем объект класса player. Передаём имя игрока и пустой список
    print(f"Привет, {player.player_name}!")  # Приветствуем игрока
    print(f"Составьте {count_words} слов из слова {basic_word_.original_word}")  # Просим создать слова
    print(f"Поехали! Ваше первое слово?")
    for i in range(0, count_words):
        user_answer = input("Ввод: ")
        if user_answer.lower() == "stop" or user_answer.lower() == "стоп":
            return print(f"Конец игры\nВы угадали: {player.count_of_used_words()}")
        elif len(user_answer) <= 2:
            print("Слишком короткое слово")
        elif not basic_word_.user_answer_in_list(user_answer):
            print("Неверно")
        elif not player.append_to_used_words(user_answer, basic_word_.set_of_valid_words):
            print("Слово уже использованно")
        else:
            player.append_to_used_words(user_answer,basic_word_.set_of_valid_words)
            print("Слово было добавлено!")
    print(f"Конец игры\nВы угадали: {player.count_of_used_words()} из {count_words} слов")


game()
