

def pancake_flip(pancakes):
    sorted_pancakes = " ".join([str(x) for x in sorted(pancakes)])
    total_result = []
    output = " ".join([str(x) for x in pancakes]) + " ".join([str(y) for y in total_result])
    flips = 0
    while output != sorted_pancakes:
        for item in pancakes:
            if item == max(pancakes) and pancakes.index(item) == 0:
                pancakes.reverse()
                flips += 1
                total_result.insert(0, pancakes.pop())
                output = " ".join([str(x) for x in pancakes]) + " " + " ".join([str(y) for y in total_result])
                print(output + " Flips: " + str(flips))
            elif item == max(pancakes):
                result = pancakes[:]
                result = pancakes[0:pancakes.index(item) + 1]
                result.reverse()
                result.extend(pancakes[pancakes.index(item) + 1:])
                pancakes = result[:]
                flips += 1
                output = " ".join([str(x) for x in pancakes]) + " " + " ".join([str(y) for y in total_result])
                print(output + " Flips: " + str(flips))
