import random

def toFixed(numObj, digits=0):
        return f"{numObj:.{digits}f}"

x1 = set()
x2 = {2.30,345.23,12.23,3.23}

for i in range(10):
        x1.add(toFixed(random.uniform(0.7 , 150), 2))   
res1 = x1 & x2
res2 = x1 - x2
print(x1,x2)
print(res1,res2)