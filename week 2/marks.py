def main():
    marks=[23, 65, 85, 29, 78, 66, 93, 42, 79]
    A=[] #above 80
    B=[] #50-80
    C=[] #below 50

    for i in marks:
        if i>80:
            A.append(i)
        elif i>=50 and i<80:
            B.append(i)
        else:
            C.append(i)

    print("A grade: ", A)
    print("B grade: ", B)
    print("C grade: ", C)

if __name__ == "__main__":
    main()


