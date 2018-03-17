from random import shuffle

def kids_lotto(kids_list,lotto_size):
    kids_list=kids_list.split(";")
    def list_gen(kid):
        result_li=[]
        temp=kids_list[:]
        temp.remove(kid)
        shuffle(temp)
        if temp[0:lotto_size] not in result_li:
            result_li.append(temp[0:lotto_size])
            return temp[0:lotto_size]
        elif temp[0:kids_lotto()] in result_li:
            return list_gen(kid)
    result = {kid:list_gen(kid) for kid in kids_list}
    for key in result:
        print("{} > {}".format(key,";".join(result[key])))
