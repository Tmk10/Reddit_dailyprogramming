def recurse():
    yield 2
    output = 1
    for x in recurse():
        for i in range(x):
            yield output
        output = 3 - output

def kolakoski():
    yield 1
    yield 2
    for x in recurse():
        yield x
