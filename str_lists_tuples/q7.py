"""
7. Unique Characters
Problem:
Given a string, return a tuple of unique characters in the order they appear.
Input:
"programming"
Output:
("p", "r", "o", "g", "a", "m", "i", "n")
"""

def unique_characters(text):
    result = []
    for ch in text:
        if ch not in result:
            result.append(ch)
    return tuple(result)


def main():
    text = "programming"
    result = unique_characters(text)
    print(result)


if __name__ == "__main__":
    main()
