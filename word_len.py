"""Group words by length"""

def group_by_length(words: list[str]) -> dict[int, list[str]]:
    result: dict[int, list[str]] = {}

    for word in words:
        length = len(word)

        if length not in result:
            result[length] = []

        result[length].append(word)

    return result


def main() -> None:
    user_input: str = input("Enter words separated by space: ")
    words: list[str] = user_input.split()

    grouped = group_by_length(words)

    print("\nGrouped words by length:")
    print(grouped)


if __name__ == "__main__":
    main()