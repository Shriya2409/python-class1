"""
9. Student Average Score
Problem:
You are given a list of tuples where each tuple contains a student name and a list of marks. Return a dictionary mapping each student’s name (lowercase) to their average score.
Input:
[("Alice", [80, 90]), ("Bob", [70, 85, 90])]
Output:
{"alice": 85.0, "bob": 81.67}
"""

def student_average_score(data):
    result = {}
    for name, marks in data:
        average = round(sum(marks) / len(marks), 2)
        result[name.lower()] = average
    return result


def main():
    data = [("Alice", [80, 90]), ("Bob", [70, 85, 90])]
    result = student_average_score(data)
    print(result)


if __name__ == "__main__":
    main()
