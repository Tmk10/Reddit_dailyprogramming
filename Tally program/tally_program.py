

def tally_program(input_string):
    score_dct = {letter.lower(): 0 for letter in input_string}
    for letter in input_string:
        score_dct[letter.lower()] += 1 if letter.islower() else -1
    return {x: score_dct[x] for x in (sorted(score_dct, key=lambda x: (-score_dct[x], x)))}


