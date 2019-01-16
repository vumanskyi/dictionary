import app.models.words as Words


class WordsEngine(Words):

    def __init__(self, Words):
        self.__words = Words

    def get_words(self):
        return self.__words

    def set_words(self, Words):
        self.__words = Words

