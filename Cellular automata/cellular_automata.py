challenge_input = "00000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000"

def cellular_automata(first_line,steps):
    first_line= " " + first_line.replace("1","*").replace("0"," ") + " "
    result=[first_line]
    for step in range(steps+1):
        line=''
        for i in range(1,len(first_line)-1):
            line+= "*" if result[-1][i-1] != result[-1][i+1] else " "
        result.append(" "+line+" ")
    for item in result:
        print(item[1:-1])
