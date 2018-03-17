from itertools import combinations

def three_sum(input_file):
    with open(input_file) as file:
        input_li = [list((map(int, item.split(" ")))) for item in file.readlines()]
    for element in input_li:
        result = {tuple(sorted(item)) for item in combinations(element,3) if sum(item) == 0}
        for item in result:
            print(item)
        print('\n')
