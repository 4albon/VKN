import math

a = float(input("Enter a ="))
b = float(input("Enter b ="))
h = float(input("Enter h ="))
g = 1
def ff(x):
    z = math.sin((x+ math.pi) + math.cos(x + math.log(math.fabs(x))))
    return(z)
while a<b:
    y = ff(a)
    print(g,"   ",a,"   ",y)
    a = a + h
    g = 1 + g