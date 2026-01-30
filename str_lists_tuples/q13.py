"""13. Attendance Percentage
Problem:
Given a dictionary mapping employee names to a list of attendance strings ("P" or "A"), return a dictionary of employee names and their attendance percentage.
Input:
{"Ravi": ["P","P","A"], "Neha": ["P","P","P"]}
Output:
{"Ravi": 66.67, "Neha": 100.0}"""

def attendance_percentage(data):
    result = {}
    for name, records in data.items():
        percentage = (records.count("P") / len(records)) * 100
        result[name] = round(percentage, 2)
    return result


def main():
    data = {"Ravi": ["P", "P", "A"], "Neha": ["P", "P", "P"]}
    result = attendance_percentage(data)
    print(result)


if __name__ == "__main__":
    main()
