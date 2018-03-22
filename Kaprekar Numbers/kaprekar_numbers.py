def kaprekar_numbers(range_start, range_end):
    for number in range(range_start, range_end + 1):
        square = str(number ** 2)
        if len(square) == 1:
            if int(square) == number:
                print(number)
        else:
            for i in range(1, len(square)):
                a, b = square[0:i], square[i:]
                if int(b) != 0 and int(a) + int(b) == number:
                    print(number,"***",square)
                    break




