"""Find the longest word in a sentence"""

def longest_word(sentence):
    words = sentence.split()
    if not words:
        return None

    max_word = words[0]
    for word in words:
        if len(word) > len(max_word):
            max_word = word
    return max_word


def main():
    sentence = input("Enter a sentence: ")
    word = longest_word(sentence)

    if word:
        print("Longest word:", word)
    else:
        print("No words found.")


if __name__ == "__main__":
    main()