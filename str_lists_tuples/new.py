def countlist():
    #1. Count List Elements
    inp = [1,2,2,3,3]
    out = {}
    for i in inp:
        if i in out:
            out[i] += 1
        else:
            out[i] = 1
    print(out,"\n")

def dictkeycheck():
    #2. Dictionary Key Check
    inp = {"a": 1, "b": 2}
    key = input("Enter key to search: ")
    if key in inp:
        print("Found\n")
    else:
        print("Not Found\n")

def tupletodict():
    #3. Tuple to Dictionary
    inp = (("a", 1), ("b", 2))
    out = dict(inp)
    print(out,"\n")

def revwords():
    #4. Reverse Words in a String
    inp = "data science is fun"
    out = inp.split()[::-1]
    print(out,"\n")

def sumoftuples():
    #5. Sum of Tuples
    inp = [(1, 2), (3, 4), (5, 6)]
    out = [sum(t) for t in inp]
    print(out,"\n")

def strlen():
    #6. String Length Dictionary
    inp = ["python", "ml", "ai"]
    out = {s: len(s) for s in inp}
    print(out,"\n")

def unique():
    #7. Unique Characters in a String
    inp = input("Enter a string: ")
    seen = set()
    out = []
    for char in inp:
        if char not in seen:
            seen.add(char)
            out.append(char)
    print(tuple(out),"\n")

def even():
    #8. Even Numbers from List
    inp = [1, 2, 3, 4, 5, 6]
    out = [num for num in inp if num % 2 == 0]
    print(out,"\n")

def stdavg():
    #9. Student Average Score
    inp = [("Alice", [80, 90]), ("Bob", [70, 85, 90])]
    out = {name.lower(): round(sum(marks)/len(marks), 2) for name, marks in inp}
    print(out,"\n")

def wordfreq():
    #10. Word Frequency Counter
    inp = "Python is great and Python is easy"
    words = inp.lower().split()
    out = {}
    for word in words:
        word = word.strip('.,!?";:')
        if word in out:
            out[word] += 1
        else:
            out[word] = 1
    print(out,"\n")

def highestsell():
    #11. Highest Selling Product
    inp = [("Pen", 10), ("Pencil", 25), ("Pen", 15)]
    sales = {}
    for product, qty in inp:
        if product in sales:
            sales[product] += qty
        else:
            sales[product] = qty
    out = max(sales, key=sales.get)
    print(out,"\n")

def uniquevaluesextractor():
    inp = {"a": [1, 2, 3], "b": [3, 4], "c": [2, 5]}
    unique = set()
    for values in inp.values():
        unique.update(values)
    out = sorted(unique)
    print(out,"\n")

def attendancepercentage():
    inp = {"Ravi": ["P","P","A"], "Neha": ["P","P","P"]}
    out = {}
    for name, attendance in inp.items():
        percentage = (attendance.count("P") / len(attendance)) * 100
        out[name] = round(percentage, 2)
    print(out,"\n")

def charindex():
    inp = "banana"
    out = {}
    for index, char in enumerate(inp):
        if char in out:
            out[char] += (index,)
        else:
            out[char] = (index,)
    print(out,"\n")

def dictvaluemerger():
    inp = [{"a": 2, "b": 3}, {"a": 4, "c": 1}]
    out = {}
    for d in inp:
        for key, value in d.items():
            if key in out:
                out[key] += value
            else:
                out[key] = value
    print(out,"\n")

def main():
    countlist()
    dictkeycheck()
    tupletodict()
    revwords()
    sumoftuples()
    strlen()
    unique()
    even()
    stdavg()
    wordfreq()
    highestsell()
    uniquevaluesextractor()
    attendancepercentage()
    charindex()
    dictvaluemerger()

if __name__ == "__main__":
    main()
