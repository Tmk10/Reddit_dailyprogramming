#main challenge
def kaprekar_routine(number):
     number = list(str(number))
     if len(number) <4:
         number.insert(0,"0")
     return(max(number))

#bonus 1
def kaprekar_routine_1(number):
    number = list(str(number))
    if len(number) < 4:
        number.insert(0, "0")
    return "".join(sorted(number,reverse=True))

#bonus 2
def kaprekar_routine_2(number):
    counter =0
    while number != 6174:
        number = list(str(number))
        if len(number) < 4:
            number.insert(0, "0")
        if len(set(number)) < 2:
            counter =0
            return counter
        number = int("".join(sorted(number,reverse=True))) - int("".join(sorted(number)))
        counter+=1
    return counter

for number in range(1000,10000):
    print(kaprekar_routine_2(number))