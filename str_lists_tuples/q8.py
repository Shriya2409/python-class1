"""
8. Filter Even Numbers
Problem:
Given a list of numbers, return a new list containing only even numbers.
Input:
[1, 2, 3, 4, 5, 6]
Output:
[2, 4, 6]
"""

def filter_even_numbers(numbers):
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num)
    return result


def main():
    numbers = [1, 2, 3, 4, 5, 6]
    result = filter_even_numbers(numbers)
    print(result)


if __name__ == "__main__":
    main()
