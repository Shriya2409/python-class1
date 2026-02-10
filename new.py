def get_salary(employee):
    return employee["salary"]

def is_middle_salary(salary, min, max):
    return salary!= min and salary!= max

def average(values):
    return sum(values)/len(values) if values else 0

def avg_excluding_min_max(employees):
    salaries=list(map(get_salary, employees))
    min_sal=min(salaries)
    max_sal=max(salaries)

def sal_filter(salary):
    return is_middle_salary(salary, min, max)
    middle_salary = list(filter(sal_filter,salaries))
    return calculate_average(middle_salary)


def main():
    employees = [
    {"name": "A", "salary": 30000},
    {"name": "B", "salary": 50000},
    {"name": "C", "salary": 40000},
    {"name": "D", "salary": 60000}
    ]

    result = avg_excluding_min_max(employees)
    print("Average salary excluding min and max: ", result)

if __name__ == "__main__":
    main()
