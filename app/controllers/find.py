from app.controllers.controller import Controller


class Find(Controller):

    def set_list(self, list):
        self.__list = list

    def get_list(self):
        return self.__list

    def search(self, word):
        if word in self.__list:
            return self.__list[word.lower()]
        else:
            print("The word does not exist")