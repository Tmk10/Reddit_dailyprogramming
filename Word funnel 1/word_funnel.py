from requests import get
import re


data = get(r"https://raw.githubusercontent.com/dolph/dictionary/master/enable1.txt")




def funnel(first_word, second_word):
    for position, letter in enumerate(first_word):
        new_word = first_word[:position] + first_word[position+1:]
        if second_word == new_word:
            return True
    return False

def funnel_bonus1(word):
    result = set()
    for position, letter in enumerate(word):
        new_word = word[:position] + word[position + 1:]
        if new_word in data.text.splitlines():
            result.add(new_word)
    print(result)
    return list(result)

def funnel_bonus2():
    pass
# no second bonus

