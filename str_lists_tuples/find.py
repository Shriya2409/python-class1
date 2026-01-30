"""
2. Dictionary Key Check
Problem:
Given a dictionary and a key, return "Found" if the key exists, otherwise return "Not Found".
Input:
{"a": 1, "b": 2}, key = "b"
Output:
"Found"

"""
def check_key(my_dict, key):
    if key in my_dict:
        return "Found"
    else:
        return "Not Found"


def main():
    my_dict = {"a": 1, "b": 2}
    key = "b"
    result = check_key(my_dict, key)
    print(result)

if __name__ == "__main__":
    main()
