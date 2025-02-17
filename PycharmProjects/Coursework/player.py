class Player:  # Класс, в котором хранятся имя игрока и использованные слова

    def __init__(self, player_name, used_words):
        self.player_name = player_name
        self.used_words = used_words

    def __repr__(self):
        return f"{self.player_name}"

    def count_of_used_words(self):  # Возвращает кол-во использованных слов
        return len(self.used_words)

    def append_to_used_words(self, user_answer, set_of_valid_words):  # Если игрок ввёл ранее использованное слово -
        if user_answer in self.used_words:  # возвращает false. Если ответ игрока верный - возвращает true
            return False
        elif user_answer in set_of_valid_words:
            self.used_words.append(user_answer)
            return True
        else:
            return False

