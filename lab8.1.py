from array import *
import random


def bubble_sort(nums):
    # Устанавливаем swapped в True, чтобы цикл запустился хотя бы один раз
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
def main():
# task 1
    arr = array('f',[])

    n = 4

    for i in range(n):
        arr.append(pow((1/2), i))

    for i in range(n):
        arr.append(random.randint(-1,3))

    bubble_sort(arr)
    arr.reverse()
    print(arr)
    
    arr.pop(0)
    arr.pop(0)
    arr.pop(-1)
    arr.pop(-1)

    print(arr)

if __name__ == "__main__":
    main()