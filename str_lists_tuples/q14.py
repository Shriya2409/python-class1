"""14. Character Index Map
Problem:
Given a string, return a dictionary mapping each character to a tuple of all its indices.
Input:
"banana"
Output:
{"b": (0,), "a": (1,3,5), "n": (2,4)}"""

def character_index_map(text):
    result = {}
    for index, char in enumerate(text):
        result.setdefault(char, []).append(index)
    for char in result:
        result[char] = tuple(result[char])
    return result


def main():
    text = "banana"
    result = character_index_map(text)
    print(result)


if __name__ == "__main__":
    main()
