def light_timer():
    light_li=[] # light_li is a list of lists, each element looks like [1,5]
    while True:
        temp = input()
        if temp:
            light_li.append(temp.split(" "))
        else:
            break
    total_time = len(set([x for element in light_li for x in range(int(element[0]),int(element[1]))]))
    return total_time

print(light_timer())