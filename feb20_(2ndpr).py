"""
user will input 2 strings
find out whether second string is a rotation of first string or not
"""

def is_rotation(a: str, b: str)-> bool:
    if len(a)!= len(b):
        return False
    return b in (a+a)

def main()->None:
    a: str= input("Enter first string: ")
    b: str= input("Enter second string: ")
    if is_rotation(a,b):
        print("String 2 is a rotation of string 1")
    else:
        print("String 2 is not a rotation of string 1")

if __name__=="__main__":
    main()