def main():
    numbers = [3, 5, 4, 2, 1]
    result = []
    total = 0

    for i in numbers:
        total = total + i
        result.append(total)

    print(result)

if __name__ == "__main__":
    main()
