# input format different from challenge requirements

from itertools import combinations_with_replacement


def goldbach_conjecture(number):
    odd_primes = [x for x in range(3, number + 1) if sum([x % y == 0 for y in range(2, x + 1)]) == 1]
    result = [str(number) + " = " + "+".join(str(y) for y in x) for x in combinations_with_replacement(odd_primes, 3) if
              sum(x) == number]
    return (result[-1])


