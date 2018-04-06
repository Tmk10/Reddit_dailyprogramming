import math

def smallest_complex(number):
    b= [(number/a,a, a+number/a) for a in range(1,int(math.sqrt(number)+1)) if(number % a == 0)]
    return b[-1]