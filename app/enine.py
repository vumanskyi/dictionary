import json
from app.models.words import Words

PATH_TO_SOURCE = './source/'

LANGUAGE = {
    'en_to_de': 'dictionary_english_to_german.json',
    'de_to_en': 'dictionary_german_to_english.json'
}


def include_model(source):
    words = Words()
    words.set_source(source)


def choose_translation(lang):
    if lang in LANGUAGE:
        lang = lang.lower()
        # get file with translations
        data = json.load(open(PATH_TO_SOURCE + LANGUAGE[lang]))
        include_model(data)
    else:
        print("Sorry but the current translations does not exist")
