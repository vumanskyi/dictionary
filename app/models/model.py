import json
from app.source.enine import choose_translation

class Model:

    def get_source(self):
        return self.__source

    def method(self):
        print('This is model class')

    def is_json(self, data):
        try:
            json_object = json.loads(data)
        except ValueError as e:
            return False
        return True

    def set_language(self, lang):
        self.__source = choose_translation(lang)