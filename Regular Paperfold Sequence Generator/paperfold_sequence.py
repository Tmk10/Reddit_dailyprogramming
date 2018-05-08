li="1"

for x in range(8):
    li += "1"
    temp = ("0" if x =="1" else "1" for x in li[-2::-1])
    li += "".join(temp)
print(li)