import math

a = float(input("Enter a ="))
b = float(input("Enter b ="))
h = float(input("Enter h ="))
def ff(x):
    z = math.sin((x+ math.pi) + math.cos(x + math.log(math.fabs(x))))
    return(z)
for i in range(100):
    y = ff(a)
    a = round(a,1)
    print(i,"   ",a,"   ",y)
    a = a + h
    if a>b:
        break