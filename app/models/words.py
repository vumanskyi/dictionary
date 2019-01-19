from app.models.model import Model


class Words(Model):
    def get_all_words(self):
        print(self.get_source)

    def set_word(self, word):
        self.__word = word

    def get_word(self):
        return self.__word

    def get_result(self):
        if self.__word in self.get_source():
            words = self.get_source()
            return words[self.__word.lower()]
        else:
            return "The word does not exists in vocabulary"

