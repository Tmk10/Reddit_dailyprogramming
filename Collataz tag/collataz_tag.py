
def collataz_tag(initial_word):
    sequence = {"a" :"bc" ,"b" :"a" ,"c" :"aaa"} output= initial_word
    while len(output) >1:
        output= output[2:]+ sequence[output[0]]
        print(output)


def collataz_tag_bonus(initial_word):
    sequence = {'a': 'bc', 'b': 'a', 'c': 'aaa'}
    coding = {97: '100', 98: '010', 99: '001'}
    output=""
    while initial_word:
        for key, item in coding.items():
            if item == initial_word[:3]:
                output+=chr( key)
                initial_word= initial_word[3:]
    numeric_output = output.translate(coding)
    while len(output) >1:
        output = output[2:] + sequence[output[0]]
        numeric_output = numeric_output[3:] +output. translate(coding)
        while numeric_output != output.translate(coding):
            numeric_output = numeric_output[1:]
            print(numeric_output)