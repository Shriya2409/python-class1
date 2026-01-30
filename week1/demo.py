
def get_number():
    """Accept a number from the user."""
    return int(input("Enter a number: "))


def check_odd_even(num):
    """Return whether a number is odd or even."""
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


def display_numbers(limit):
    """Print numbers up to the given limit with odd/even status."""
    for i in range(1, limit + 1):
        print(f"{i} is {check_odd_even(i)}")


def main():
    number = get_number()
    display_numbers(number)


if __name__ == "__main__":
    main()