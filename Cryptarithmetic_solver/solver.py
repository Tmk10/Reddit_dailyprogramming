import re
from itertools import permutations

def solver(equation):
    words = equation.replace("+","").replace("=","").split()
    letters= set(re.findall(r"\w",equation))
    firsts = {element[0] for element in words}
    letters = "".join(firsts) + "".join(letters-firsts)
    for permutation in permutations("0123456789", len(letters)):
        if "0" not in permutation[:len(firsts)]:
            translation = "".maketrans(letters, "".join(permutation))
            eq_to_solve= equation.translate(translation)
            if eval(eq_to_solve):
                result = {chr(key):chr(item) for key, item in translation.items()}
                return {key:result[key] for key in sorted(result.keys())}
