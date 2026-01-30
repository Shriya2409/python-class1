def main():
    numbers = [3, 5, 3, 2, 5, 1, 2, 5, 7, 7, 7]

    for n in numbers[:]:        
        if numbers.count(n) > 1:
            numbers.remove(n)   

    print(numbers)

if __name__ == "__main__":
    main()
