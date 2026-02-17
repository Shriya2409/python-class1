"""Multi-Region Sales Analytics Engine
Problem Statement
You are given a list of regions. Each region contains multiple stores, and each store contains multiple transactions.
Each transaction has:
• amount (float)
• category (string)
• successful (boolean)
Task
• Consider only transactions that:
• Are successful
• Belong to category "Electronics"
• Have amount ≥ 100
Apply:
• 18% GST to each valid transaction
• Then apply an additional 5% regional surcharge
Compute:
• The total revenue per region
• Then return the grand total across all regions

Input: 
regions = [
    {
        "region": "North",
        "stores": [
            {
                "transactions": [
                    {"amount": 200, "category": "Electronics", "successful": True},
                    {"amount": 50, "category": "Electronics", "successful": True},
                    {"amount": 500, "category": "Clothing", "successful": True}
                ]
            }
        ]
    },
    {
        "region": "South",
        "stores": [
            {
                "transactions": [
                    {"amount": 300, "category": "Electronics", "successful": True},
                    {"amount": 150, "category": "Electronics", "successful": False}
                ]
            }
        ]
    }
]

Final output: single float (grand total)


write a simple modular beginner friendly code in python (in 1 file)"""

# Multi-Region Sales Analytics Engine

# Function to calculate GST and regional surcharge for a transaction
def apply_taxes(amount):
    gst = amount * 0.18  # 18% GST
    subtotal = amount + gst
    surcharge = subtotal * 0.05  # 5% regional surcharge
    total = subtotal + surcharge
    return total

# Function to calculate total revenue for a single store
def calculate_store_revenue(store):
    total = 0
    for transaction in store["transactions"]:
        if transaction["successful"] and transaction["category"] == "Electronics" and transaction["amount"] >= 100:
            total += apply_taxes(transaction["amount"])
    return total

# Function to calculate total revenue for a region
def calculate_region_revenue(region):
    total = 0
    for store in region["stores"]:
        total += calculate_store_revenue(store)
    return total

# Function to calculate grand total across all regions
def calculate_grand_total(regions):
    grand_total = 0
    for region in regions:
        region_total = calculate_region_revenue(region)
        print(f"Total revenue for region {region['region']}: {region_total:.2f}")
        grand_total += region_total
    return grand_total

# Input data
regions = [
    {
        "region": "North",
        "stores": [
            {
                "transactions": [
                    {"amount": 200, "category": "Electronics", "successful": True},
                    {"amount": 50, "category": "Electronics", "successful": True},
                    {"amount": 500, "category": "Clothing", "successful": True}
                ]
            }
        ]
    },
    {
        "region": "South",
        "stores": [
            {
                "transactions": [
                    {"amount": 300, "category": "Electronics", "successful": True},
                    {"amount": 150, "category": "Electronics", "successful": False}
                ]
            }
        ]
    }
]

# Calculate grand total
grand_total = calculate_grand_total(regions)
print(f"Grand total revenue: {grand_total:.2f}")



