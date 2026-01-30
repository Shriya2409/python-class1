"""
10. Word Frequency Counter
Problem:
Given a string sentence, return a dictionary containing the frequency of each word, ignoring case and punctuation.
Input:
"Python is great and Python is easy"
Output:
{"python": 2, "is": 2, "great": 1, "and": 1, "easy": 1}
"""

import string

def word_frequency(sentence):
    result = {}
    text = sentence.lower()
    for ch in string.punctuation:
        text = text.replace(ch, "")
    words = text.split()
    for word in words:
        result[word] = result.get(word, 0) + 1
    return result


def main():
    sentence = "Python is great and Python is easy"
    result = word_frequency(sentence)
    print(result)


if __name__ == "__main__":
    main()
