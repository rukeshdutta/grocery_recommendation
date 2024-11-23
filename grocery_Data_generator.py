import pandas as pd
import random

# Generate synthetic customer data
def generate_synthetic_data(num_customers=1000, num_products=20):
    random.seed(42)
    
    # Product catalog
    products = [f"Product_{i}" for i in range(1, num_products + 1)]
    
    # Generate customers
    customer_ids = [f"Customer_{i}" for i in range(1, num_customers + 1)]
    
    # Generate transaction data
    data = []
    for customer in customer_ids:
        # Randomly decide how many products a customer buys
        num_purchases = random.randint(1, 10)
        purchased_products = random.sample(products, num_purchases)
        for product in purchased_products:
            data.append({"CustomerID": customer, "Product": product})
    
    # Convert to DataFrame
    transactions = pd.DataFrame(data)
    return transactions

# Generate and save data
synthetic_data = generate_synthetic_data()
synthetic_data.to_csv("synthetic_grocery_data.csv", index=False)
print("Synthetic Data Sample:")
print(synthetic_data.head())
