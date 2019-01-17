import json

class Model:
    @property
    def get_source(self):
        return self.__source

    def set_source(self, source):
        self.__source = source

    def method(self):
        print('This is model class')

    def is_json(self, data):
        try:
            json_object = json.loads(data)
        except ValueError as e:
            return False
        return True