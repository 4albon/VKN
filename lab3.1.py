def main():
    a = int(input("Enter a number: "))

    if len(str(a)) != 3:
        print("The number is not 3 digits long")
        exit()

    digits = list(str(a))
    result = int(digits[0]) - int(digits[-1])

    print("The result is: " + str(result))

if __name__ == "__main__":
    main()