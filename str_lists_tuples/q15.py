"""15. Dictionary Value Merger
Problem:
Given a list of dictionaries with integer values, merge them into a single dictionary by summing values of common keys.
Input:
[{"a": 2, "b": 3}, {"a": 4, "c": 1}]
Output:
{"a": 6, "b": 3, "c": 1}"""

def merge_dictionaries(dicts):
    result = {}
    for d in dicts:
        for key, value in d.items():
            result[key] = result.get(key, 0) + value
    return result


def main():
    data = [{"a": 2, "b": 3}, {"a": 4, "c": 1}]
    result = merge_dictionaries(data)
    print(result)


if __name__ == "__main__":
    main()
