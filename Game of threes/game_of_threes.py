def three_game(number):
    while number >= 1:
        if divmod(number, 3)[1] == 0:
            print("{} {}".format(int(number), 0))
            number = number / 3
        elif divmod((number + 1), 3)[1] == 0:
            print("{} {}".format(int(number), "+1"))
            number = (number + 1) / 3
        elif divmod((number - 1), 3)[1] == 0:
            print("{} {}".format(int(number), "-1"))
            number = (number - 1) / 3
    print(1)
