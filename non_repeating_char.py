"""in a given string, find the first non repeating char"""
def first_non_repeating(s: str) -> str | None:
    char_count: dict[str, int] = {}

    # Count frequency
    for ch in s:
        if ch in char_count:
            char_count[ch] += 1
        else:
            char_count[ch] = 1

    # Find first non-repeating
    for ch in s:
        if char_count[ch] == 1:
            return ch

    return None


def main() -> None:
    s: str = input("Enter a string: ")

    result = first_non_repeating(s)

    if result:
        print("First non-repeating character:", result)
    else:
        print("No non-repeating character found.")


if __name__ == "__main__":
    main()