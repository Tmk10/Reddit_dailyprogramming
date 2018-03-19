from random import shuffle

bag = list("OISZLJT")


def make_tetris(length):
    output = ""
    while len(output) < length:
        shuffle(bag)
        output += "".join(bag)
    return output


def verification(tetris_string):
    while tetris_string:
        if len(set(tetris_string[0:len(bag)])) != len(list(tetris_string[0:len(bag)])):
            return False
        tetris_string = tetris_string[len(bag):]
    return True
