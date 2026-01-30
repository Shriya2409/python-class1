"""
5. Sum of Tuples
Problem:
Given a list of tuples containing two integers each, return a list of their sums.
Input:
[(1, 2), (3, 4), (5, 6)]
Output:
[3, 7, 11]
"""

def sum_of_tuples(tuples_list):
    result = []
    for item in tuples_list:
        result.append(item[0] + item[1])
    return result


def main():
    data = [(1, 2), (3, 4), (5, 6)]
    result = sum_of_tuples(data)
    print(result)


if __name__ == "__main__":
    main()
