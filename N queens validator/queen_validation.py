def isdiag(solution):
    solution = list(enumerate(solution, 1))
    temp_solution = solution[:]
    for element in solution:
        temp_solution.remove(element)
        for second_element in temp_solution:
            if (abs((element[1] - second_element[1])) / abs(
                    (element[0] - second_element[0]))) == 1:
                return False
    return True


def isrow(solution):
    return len(solution) == len(set(solution))


def qcheck(solution):
    return isdiag(solution) and isrow(solution)


def qfix(solution):
    for index in range(len(solution)):
        for second_index in range(len(solution)):
            temp_solution = solution[:]
            temp_solution[index], temp_solution[second_index] = solution[second_index], solution[
                index]
            if qcheck(temp_solution):
                return temp_solution
    return False
