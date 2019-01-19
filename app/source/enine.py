import json
import os

PATH_TO_SOURCE = os.path.dirname(os.path.realpath(__file__))

LANGUAGE = {
    'en_to_de': '/dictionary_english_to_german.json',
    'de_to_en': '/dictionary_german_to_english.json'
}

def choose_translation(lang):
    if lang in LANGUAGE:
        lang = lang.lower()
        # get file with translations
        data = json.load(open(PATH_TO_SOURCE + LANGUAGE[lang]))
        return data
    else:
        print("Sorry but the current translations does not exist")
