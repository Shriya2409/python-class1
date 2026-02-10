from functools import reduce

# (1) Convert numbers to characters using map
def num_to_char(num):
    return chr(num)

def convert_numbers_to_chars():
    numbers = [72, 69, 76, 76, 79]
    characters = map(num_to_char, numbers)
    print(list(characters))   # ['H', 'E', 'L', 'L', 'O']


# (2) Get ASCII values of characters using map
def char_to_ascii(ch):
    return ord(ch)

def ascii_values():
    characters = ['A', 'B', 'C', 'D']
    ascii_val = map(char_to_ascii, characters)
    print(list(ascii_val))    # [65, 66, 67, 68]


# (3) Square all numbers in a list using map
def square_num(num):
    return num ** 2

def square_list():
    nums = [2, 4, 6, 8]
    squares = map(square_num, nums)
    print(list(squares))      # [4, 16, 36, 64]


# (4) Filter and print only vowels using filter
def is_vowel(ch):
    return ch in ['a', 'e', 'i', 'o', 'u']

def filter_vowels():
    letters = ['a', 'b', 'c', 'd', 'e']
    vowels = filter(is_vowel, letters)
    for v in vowels:
        print(v)


# (5) Filter even and odd numbers using filter and lambda
def filter_even_odd():
    mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    even = list(filter(lambda n: n % 2 == 0, mylist))
    odd = list(filter(lambda n: n % 2 != 0, mylist))
    print(even)   # [2, 4, 6, 8]
    print(odd)    # [1, 3, 5, 7, 9]


# (6) Factorial using reduce
def factorial(n):
    if n == 0:
        return 1
    return reduce(lambda x, y: x * y, range(1, n + 1))

def factorial_demo():
    print(factorial(3))   # 6


# (7-i) Convert lowercase city names to uppercase using map and lambda
def city_uppercase():
    city = ['mumbai', 'delhi', 'kolkata']
    upper = list(map(lambda x: x.upper(), city))
    print(upper)          # ['MUMBAI', 'DELHI', 'KOLKATA']


# (7-ii) Sum of all numbers using reduce and lambda
def sum_list():
    numbers = [1, 3, 7, 8, 10]
    total = reduce(lambda a, b: a + b, numbers)
    print("Sum:", total)  # 29


# (7-iii) Maximum number using reduce and lambda
def max_list():
    numbers = [1, 3, 7, 8, 10]
    maximum = reduce(lambda a, b: a if a > b else b, numbers)
    print("The maximum is:", maximum)  # 10


# -------- MAIN PROGRAM --------
if __name__ == "__main__":
    convert_numbers_to_chars()
    ascii_values()
    square_list()
    filter_vowels()
    filter_even_odd()
    factorial_demo()
    city_uppercase()
    sum_list()
    max_list()
