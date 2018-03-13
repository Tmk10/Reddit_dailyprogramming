def change_calculator(input):
    change_list = []
    change = input[0]
    coins = list(input[1:])
    print(change, "#####",coins)
    while sum(change_list) < change:
        if change > sum(change_list) and len(coins) == 0:
            return "Cannot return change, to insufficient coins in cashbox"
        change_list.append(coins.pop(0))
    return len(change_list)



