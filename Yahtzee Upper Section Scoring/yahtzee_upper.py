from timeit import timeit
setup = """from yahtzee_upper import yahtzee_upper2
with open('challange_input.txt', "r") as file:
    result = file.readlines()
    result = [int(element) for element in result]"""

def yahtzee_upper(result):
    return (max((element * result.count(element) for element in result)))

def yahtzee_upper2(result):
    result_dict = {}
    for element in result:
        result_dict[element] = result_dict.get(element, 0)
        result_dict[element] += element

    max = 0
    for value in result_dict.values():
        if value > max:
            max = value
    return max

with open('challange_input.txt', "r") as file:
    result = file.readlines()
    result = [int(element) for element in result]
    print(timeit('yahtzee_upper2(result)', setup, number=100))





