def get_number():
    num = int(input("Enter a number: "))
    return num


def count_digits(num):
    count = 0

    if num == 0:
        return 1

    while num > 0:
        count = count + 1
        num = num // 10

    return count


def main():
    number = get_number()
    digits = count_digits(number)
    print("Number of digits:", digits)


if __name__ == "__main__":
    main()