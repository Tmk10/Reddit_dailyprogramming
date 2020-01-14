def additive_persitence(number: int):
    if number < 9:
        return 0
    new_number = 0
    while number:
        quotient, reminder = divmod(number, 10)
        number = quotient
        new_number += reminder

    if new_number > 9:
        return 1 + additive_persitence(new_number)
    else:
        return 1


