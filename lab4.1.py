from math import *

def solve(x):
    first = sin(x**2) - tan(x - 8)
    second = log(x**3-sin(x))

    return first / second

def main():
    x = float(input("Enter x: "))
    print(solve(x))

if __name__ == "__main__":
    main()