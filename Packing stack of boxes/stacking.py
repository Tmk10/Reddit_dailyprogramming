
from itertools import combinations, product, chain

def stacking(input_str):
    result = []
    nr_of_stacks = int(input_str[0])
    boxes = sorted(list(map(int, list(input_str[2:]))))
    quotient, reminder = divmod(sum(boxes), nr_of_stacks)
    if reminder:
        return "nothing"
    full_stack, partial_stack = divmod(len(boxes), nr_of_stacks)
    if partial_stack:
        stack_size = [partial_stack] + [nr_of_stacks] * full_stack
    else:
        stack_size = [nr_of_stacks] * 3
    for layer in stack_size:
        result.append({tuple(sorted(item)) for item in combinations(boxes, layer) if sum(item) == quotient})
    for item in product(*result):
        if sorted(chain(*item)) == boxes:
            return item