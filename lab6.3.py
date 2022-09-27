from math import *

a = float(input("Enter a ="))
b = float(input("Enter b ="))
h = float(input("Enter h ="))
spisok = [] 
g = 0 
x = a

for i in range(100):
    y = round(sin(x + pi) + cos(x + log(abs(x))), 3)
    spisok.append([x, y])
    g += y 
    x += h
    if x > b:
        break
g = round(g, 3)
print(g)
print(spisok)