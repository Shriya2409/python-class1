def getfactorial(n):
    """Return the factorial of a number."""
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


def main():
    num = int(input("Enter a number: "))

    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = getfactorial(num)
        print(f"Factorial of {num} is {result}")


if __name__ == "__main__":
    main()
