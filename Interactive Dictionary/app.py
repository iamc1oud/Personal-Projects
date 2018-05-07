# Modules
import json
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open('076 data.json'))

def translate(w):
    w = w.lower()
    return data[w]

word = input('Enter word: ')

try:
    print(translate(word))
except KeyError:
    new_word = get_close_matches(word, list(data.keys()))
    print('Did you mean {}? Press Y for Yes or N for No.'.format(new_word[0]))
    answer = input()
    if answer == 'Y'  or answer == 'y':
        print(translate(new_word[0]))
    else:
        print('Not found')

    

