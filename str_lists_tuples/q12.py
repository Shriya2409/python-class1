"""
12. Unique Values Extractor
Problem:
Given a dictionary where keys are strings and values are lists of integers, return a sorted list of all unique integers across all lists.
Input:
{"a": [1, 2, 3], "b": [3, 4], "c": [2, 5]}
Output:
[1, 2, 3, 4, 5]
"""

def extract_unique_values(data):
    unique_values = set()
    for values in data.values():
        unique_values.update(values)
    return sorted(unique_values)


def main():
    data = {"a": [1, 2, 3], "b": [3, 4], "c": [2, 5]}
    result = extract_unique_values(data)
    print(result)


if __name__ == "__main__":
    main()
