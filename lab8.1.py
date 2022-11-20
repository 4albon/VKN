from array import *
import random

def main():
# task 1
    arr = array('i',[])

    n = 4

    arr = [pow((1/2), i) for i in range(n)]
    # for i in range(n):
    #     arr.append(pow((1/2), i))

    # arr = [random.randint(-1,3) for i in range(n)]

    for i in range(n):
        arr.append(random.randint(-1,3))

    arr.sort(reverse=True)

    arr.pop(0)
    arr.pop(0)
    arr.pop(-1)
    arr.pop(-1)
    print(arr) 


if __name__ == '__main__':
    main()

