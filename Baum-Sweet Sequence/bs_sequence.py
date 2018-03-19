# Baum-Sweet Sequence

def bs_sequence(range_nr):
    result = [1]  # 1 for bin(0)
    split_numbers = list(
        list(filter(lambda x: x != '', bin(number)[2:].split("1"))) for number in range(1, range_nr + 1))
    for item in split_numbers:
        item = [False for (element) in item if divmod(len(element), 2)[1] != 0]
        if False in item:
            result.append(0)
        else:
            result.append(1)
    return result
