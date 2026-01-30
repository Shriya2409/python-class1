"""
6. String Length Map
Problem:
Given a list of strings, return a dictionary with each string and its length.
Input:
["python", "ml", "ai"]
Output:
{"python": 6, "ml": 2, "ai": 2}
"""

def string_length_map(strings):
    result = {}
    for s in strings:
        result[s] = len(s)
    return result


def main():
    data = ["python", "ml", "ai"]
    result = string_length_map(data)
    print(result)


if __name__ == "__main__":
    main()
