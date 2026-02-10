"""
11. Highest Selling Product
Problem:
You are given a list of tuples where each tuple represents (product_name, quantity_sold). Return the product name with the highest total sales.
Input:
[("Pen", 10), ("Pencil", 25), ("Pen", 15)]
Output:
"Pen"
"""

def highest_selling_product(data):
    sales = {}
    for product, quantity in data:
        sales[product] = sales.get(product, 0) + quantity
    return max(sales, key=sales.get)


def main():
    data = [("Pen", 10), ("Pencil", 25), ("Pen", 15)]
    result = highest_selling_product(data)
    print(result)


if __name__ == "__main__":
    main()


