import json
from app.source.enine import choose_translation

class Model:
    def __init__(self, lang):
        self.set_language(lang)

    def get_source(self):
        return self.__source

    def is_json(self, data):
        try:
            json_object = json.loads(data)
        except ValueError as e:
            return False
        return True

    def set_language(self, lang):
        self.__source = choose_translation(lang)
