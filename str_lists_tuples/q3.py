"""
3. Tuple to Dictionary
Problem:
Given a tuple of (key, value) pairs, convert it into a dictionary.
Input:
(("a", 1), ("b", 2))
Output:
{"a": 1, "b": 2}
"""

def tuple_to_dictionary(tuples):
    result_dict = {}  
    for item in tuples:
        key = item[0]
        value = item[1]
        result_dict[key] = value

    return result_dict


def main():
    data = (("a", 1), ("b", 2))
    result = tuple_to_dictionary(data)
    print("Dictionary:", result)


if __name__ == "__main__":
    main()
