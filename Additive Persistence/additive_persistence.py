def additive_persitance(number: int):
    counter = 0
    quotient = 1
    digits = []
    while quotient:
        quotient, reminder = divmod(number, 10)
        digits.append(reminder)

    number = sum(digits)
    if number > 9:
        counter += 1
        additive_persitance(number)
    else:
        return counter

