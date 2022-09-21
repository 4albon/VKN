from math import *

def solve(t, k, n):
    first = 4.17 * sqrt(t)
    second = sin(pi * n + pi / 7)
    third = e ** ((k / t) + n)

    return first - second + third

def main():
    t = float(input("Enter t: "))
    k = float(input("Enter k: "))
    n = float(input("Enter n: "))

    print(solve(t, k, n))

if __name__ == "__main__":
    main()