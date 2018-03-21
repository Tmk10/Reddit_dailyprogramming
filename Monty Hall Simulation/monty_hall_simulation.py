from random import choice


def game(games_amount):
    gates = (1, 2, 3)
    standard_play_li=[]
    switch_gate_li=[]


    def standard_play():
        pick = choice(gates)
        return pick == winning_gate


    def switch_gate():
        pick = choice(gates)
        reduced_gates = [item for item in gates if item != winning_gate and item !=pick]
        if len(reduced_gates)==1:
            return True
        else:
            return False

    for _ in range(games_amount):
        winning_gate = choice(gates)
        standard_play_li.append(standard_play())
        switch_gate_li.append(switch_gate())
    return "Switch gate play: {:.1f} % to win\nStandard play: {:.1f} % to win".format\
                                                                ((switch_gate_li.count(True)/games_amount) * 100,
                                                                (standard_play_li.count(True)/games_amount) * 100)
