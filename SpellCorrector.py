from spellchecker import SpellChecker

spell = SpellChecker()

# find those words that may be misspelled

def SpellCorrect(text):
    misspelled = spell.unknown(text.split(' '))
    res = text
    for word in misspelled:
    # Get the one `most likely` answer
        correct = (spell.correction(word))
        res.replace(word, correct)
    
    return res

