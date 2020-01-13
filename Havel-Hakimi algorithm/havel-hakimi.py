def havel_hakimi(responses: list):
    while responses:
        responses = [element for element in responses if element != 0]
        if responses:
            responses.sort(reverse=True)
            n = responses.pop(0)
            if n > len(responses):
                return False
            for x in range(n):
               responses[x] -= 1

    return True


havel_hakimi([5, 3, 0, 2, 6, 2, 0, 7, 2, 5])
havel_hakimi([4, 2, 0, 1, 5, 0])
havel_hakimi([3, 1, 2, 3, 1, 0])
havel_hakimi([16, 9, 9, 15, 9, 7, 9, 11, 17, 11, 4, 9, 12, 14, 14, 12, 17, 0, 3, 16])
havel_hakimi([14, 10, 17, 13, 4, 8, 6, 7, 13, 13, 17, 18, 8, 17, 2, 14, 6, 4, 7, 12])
havel_hakimi([15, 18, 6, 13, 12, 4, 4, 14, 1, 6, 18, 2, 6, 16, 0, 9, 10, 7, 12, 3])
havel_hakimi([6, 0, 10, 10, 10, 5, 8, 3, 0, 14, 16, 2, 13, 1, 2, 13, 6, 15, 5, 1])
havel_hakimi([2, 2, 0])
havel_hakimi([3, 2, 1])
havel_hakimi([1, 1])
havel_hakimi([1])
havel_hakimi([])
