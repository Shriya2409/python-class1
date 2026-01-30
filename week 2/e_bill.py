def main():
    units=int(input("Enter units of electricity consumed: "))
    if units<=100:
        bill=1*units
        print("Bill is: ", bill)
    elif units>100 and units<=200:
        bill=100+(2*(units-100))
        print("Bill is: ", bill)
    elif units>200:
        bill=300+(3*(units-200))
        print("Bill is: ", bill)


if __name__ == "__main__":
    main()