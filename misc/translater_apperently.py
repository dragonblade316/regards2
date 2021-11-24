#puppylovera asked for it idc that he was jokeing (must speak germon at the very least)

from translate import Translator

def translate(language, message):
    translator= Translator(to_lang=language)
    translation = translator.translate(message)
    return translation
