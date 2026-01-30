"""
4. Reverse Words
Problem:
Given a string, return a list of words in reverse order.
Input:
"data science is fun"
Output:
["fun", "is", "science", "data"]
"""

def reverse_words(text):
    words = text.split()
    return words[::-1]


def main():
    text = "data science is fun"
    result = reverse_words(text)
    print(result)


if __name__ == "__main__":
    main()
