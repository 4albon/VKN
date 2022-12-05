import math

a = (3,6,-2)
b = (1,-5,3)
c = (3,-8,-2)

ao = math.sqrt(pow(a[0],2) + pow(a[1],2) + pow(a[2],2))
bo = math.sqrt(pow(b[0],2) + pow(b[1],2) + pow(b[2],2))
co = math.sqrt(pow(c[0],2) + pow(c[1],2) + pow(c[2],2))
print(ao,bo,co)

if ao < bo and ao < co:
     print(f"Самое короткое растояние от точки A{a}")
elif bo < ao and bo < co:
     print(f"Самое короткое растояние от точки B{b}")
elif co < bo and co <ao:
     print(f"Самое короткое растояние от точки C{c}")
    
if ao > bo and ao > co:
     print(f"Самое длинное растояние от точки A{a}")
elif bo > ao and bo > co:
     print(f"Самое длинное растояние от точки B{b}")
elif co > bo and co >ao:
     print(f"Самое длинное растояние от точки C{c}")