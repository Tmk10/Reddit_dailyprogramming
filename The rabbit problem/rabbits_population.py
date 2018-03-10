def rabbit_population(males, females, number):
    rabbits = [[males, females, 2]]
    months = 0
    while males + females < number:
        newborns = [0, 0, -1]
        for rabbit in rabbits:
            if rabbit[2] >= 4:
                newborns[0] += rabbit[1] * 5
                newborns[1] += rabbit[1] * 9
        if newborns[0] != 0:
            rabbits.append(newborns[:])
            males += newborns[0]
            females += newborns[1]
        for rabbit in rabbits:
            rabbit[2] += 1
        months += 1
        newborns.clear()
    return months
