# 1. Average Salary Excluding Min and Max

def average_salary_excluding_min_max():
    
    employees = [
        {"name": "A", "salary": 30000},
        {"name": "B", "salary": 50000},
        {"name": "C", "salary": 40000},
        {"name": "D", "salary": 60000}
    ]

    salaries = list(map(lambda e: e["salary"], employees))
    min_salary, max_salary = min(salaries), max(salaries)

    filtered_salaries = list(
        filter(lambda s: s != min_salary and s != max_salary, salaries)
    )

    return sum(filtered_salaries) / len(filtered_salaries)


# 2. Filter Valid Email Domains

def valid_usernames():
    emails = ["alice@gmail.com", "bob@yahoo.com", "carol@gmail.com"]
    allowed_domains = {"gmail.com"}
    valid_emails = filter(
        lambda e: e.split("@")[1] in allowed_domains,
        emails
    )
    return list(map(lambda e: e.split("@")[0], valid_emails))


# 3. Students Passed All Subjects

def students_passed_all():
    students = {
        "Alice": [45, 50, 60],
        "Bob": [35, 55, 65],
        "Charlie": [40, 40, 40]
    }
    passed_students = filter(
        lambda item: all(mark >= 40 for mark in item[1]),
        students.items()
    )
    return list(map(lambda item: item[0], passed_students))


# 4. Convert & Filter Product Prices

def expensive_products_in_inr(rate=83):
    products = [
        ("Pen", 10),
        ("Bag", 50),
        ("Shoes", 60)
    ]

    converted_prices = map(
        lambda p: (p[0], p[1] * rate),
        products
    )
    return list(filter(lambda p: p[1] > 3000, converted_prices))


# 5. Active Users with Prime IDs

def is_prime(n):
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))


def active_users_with_prime_ids():
    users = [
    {"name": "A", "user_id": 2, "active": True},
    {"name": "B", "user_id": 4, "active": True},
    {"name": "C", "user_id": 5, "active": False},
    {"name": "D", "user_id": 7, "active": True}
]
    filtered_users = filter(
        lambda u: u["active"] and is_prime(u["user_id"]),
        users
    )
    return list(map(lambda u: u["name"], filtered_users))


# 6. Normalize and Filter Strings

def normalize_and_filter():
    words = ["  Python ", " AI ", "Machine ", " Data "]
    normalized = map(lambda w: w.strip().lower(), words)
    return list(filter(lambda w: len(w) >= 5, normalized))


if __name__ == "__main__":
    print(average_salary_excluding_min_max())
    print(valid_usernames())
    print(students_passed_all())
    print(expensive_products_in_inr())
    print(active_users_with_prime_ids())
    print(normalize_and_filter())
