from math import * 

x = float(input("Enter x:"))

if  x <= -0.5:
    y= abs(-x**2 + (2*x)**-x)
    print("first")

elif x<5:
    y= (cos(x) + sin(2*x))
    print("second")

else:
    y= -9 + log(x) + sqrt(x)
    print("third")
print ("y =" ,y)
