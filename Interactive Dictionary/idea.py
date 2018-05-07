"""
It's a basic idea what we are trying to program.
"""


# Using module to access json files
import json

# Loading data
data = json.load(open('076 data.json'))

def translate(w):
    return data[w]

word = input('Enter word: ')

print(translate(word))
