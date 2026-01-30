"""
1. Count Elements
Problem:
Given a list of integers, return a dictionary with each number and its count.
Input:
[1, 2, 2, 3, 3, 3]
Output:
{1: 1, 2: 2, 3: 3}
"""
def count_elements(numbers):
    count_dict = {}  

    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1  # increase count if number exists
        else:
            count_dict[num] = 1   # add number with count 1

    return count_dict


def main():
    numbers = [1, 2, 2, 3, 3, 3]
    result = count_elements(numbers)
    print("Element count:", result)


if __name__ == "__main__":
    main()