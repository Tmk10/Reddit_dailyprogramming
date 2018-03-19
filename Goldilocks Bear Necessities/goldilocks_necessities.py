def goldilocks_neccesities(input_file):
    counter = 1
    with open(input_file, "r") as file:
        goldilocks = list(map(int, file.readline().split(" ")))
        for line in file.readlines():
            line = list(map(int, line.split(" ")))
            if goldilocks[0] <= line[0] and goldilocks[1] >= line[1]:
                print(counter, end=" ")
            counter += 1
