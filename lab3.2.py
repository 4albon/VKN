import math
import sys

def main():
    r = float(sys.argv[1])
    h = float(sys.argv[2])
    v = math.pi * r**2 * h
    a = 2 * math.pi * r * (r + h)
    print("Volume: ", v)
    print("Surface area: ", a)

if __name__ == "__main__":
    main()