from collections import Counter


def balanced(word):
    return word.count('y') == word.count('x')


def balanced_bonus(word):
    counter = Counter(word)
    return len({item[1] for item in counter.most_common()}) <= 1
