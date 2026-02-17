"""
1. Total Revenue from Active Customers
Problem Statement
You are given a list of customer dictionaries.
Each customer has:
• name
• purchases → list of purchase amounts
• active → boolean
Calculate the total revenue generated only by active customers, but:
• Ignore purchase amounts less than 100
• Apply a 10% tax to each valid purchase before summing

customers = [
    {"name": "A", "purchases": [50, 200, 300], "active": True},
    {"name": "B", "purchases": [500, 20], "active": False},
    {"name": "C", "purchases": [150, 250], "active": True}
]
Output
990.0

2. Problem Statement
You are given a list of products as tuples:

Task:
• Keep only products in category "Electronics"
• Apply a 20% discount
• Return the total discounted price
Input
products = [
    ("Laptop", "Electronics", 1000),
    ("Shirt", "Clothing", 50),
    ("Phone", "Electronics", 500)
]
Output:
1200.0

3. Student Weighted Score Calculator
Problem Statement
You are given a list of students:

Task:
• Keep students whose average is ≥ 60
• Increase each mark by 5 grace marks
• Compute the total of all updated marks
Input
students = [
    {"name": "A", "marks": [50, 60, 70]},
    {"name": "B", "marks": [30, 40]},
    {"name": "C", "marks": [80, 90]}
]

Output: 
375

"""

# -----------------------------------------
# 1. Total Revenue from Active Customers
# -----------------------------------------

def calculate_total_revenue(customers):
    total = 0

    for customer in customers:
        if customer["active"]:   # Only active customers
            for amount in customer["purchases"]:
                if amount >= 100:   # Ignore purchases less than 100
                    amount_with_tax = amount * 1.10   # Add 10% tax
                    total += amount_with_tax

    return total


# -----------------------------------------
# 2. Total Discounted Price (Electronics)
# -----------------------------------------

def calculate_discounted_total(products):
    total = 0

    for product in products:
        name, category, price = product

        if category == "Electronics":   # Keep only Electronics
            discounted_price = price * 0.80   # Apply 20% discount
            total += discounted_price

    return total


# -----------------------------------------
# 3. Student Weighted Score Calculator
# -----------------------------------------

def calculate_total_updated_marks(students):
    total = 0

    for student in students:
        marks = student["marks"]
        average = sum(marks) / len(marks)

        if average >= 60:   # Keep students with average >= 60
            for mark in marks:
                updated_mark = mark + 5   # Add 5 grace marks
                total += updated_mark

    return total


# -----------------------------------------
# Main Program (Testing All Functions)
# -----------------------------------------

if __name__ == "__main__":

    # Problem 1
    customers = [
        {"name": "A", "purchases": [50, 200, 300], "active": True},
        {"name": "B", "purchases": [500, 20], "active": False},
        {"name": "C", "purchases": [150, 250], "active": True}
    ]

    print("Total Revenue:", calculate_total_revenue(customers))  
    # Expected Output: 990.0


    # Problem 2
    products = [
        ("Laptop", "Electronics", 1000),
        ("Shirt", "Clothing", 50),
        ("Phone", "Electronics", 500)
    ]

    print("Total Discounted Price:", calculate_discounted_total(products))  
    # Expected Output: 1200.0


    # Problem 3
    students = [
        {"name": "A", "marks": [50, 60, 70]},
        {"name": "B", "marks": [30, 40]},
        {"name": "C", "marks": [80, 90]}
    ]

    print("Total Updated Marks:", calculate_total_updated_marks(students))  
    # Expected Output: 375
