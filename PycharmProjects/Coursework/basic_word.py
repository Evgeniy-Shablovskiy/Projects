class BasicWord:  # Класс, в котором хранится изначальное слово и набор допустимых значений

    def __init__(self, original_word, set_of_valid_words):
        self.original_word = original_word
        self.set_of_valid_words = set_of_valid_words

    def __repr__(self):
        return f"Оригинальное слово: {self.original_word}\nНабор слов: {', '.join(self.set_of_valid_words)}"

    def user_answer_in_list(self, user_answer):  # Если ответ игрока верен - возвращает True
        if user_answer in self.set_of_valid_words:
            return True
        else:
            return False

    def count_of_valid_words(self):  # Возвращает кол-во допустимых значений
        return int(len(self.set_of_valid_words))
