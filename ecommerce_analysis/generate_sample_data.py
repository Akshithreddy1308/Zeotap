import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

def generate_sample_data():
    # Create data directory if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')
    
    # Set random seed for reproducibility
    np.random.seed(42)
    
    # Generate Customers data
    n_customers = 200
    customers_data = {
        'CustomerID': [f'C{str(i).zfill(4)}' for i in range(1, n_customers + 1)],
        'CustomerName': [f'Customer {i}' for i in range(1, n_customers + 1)],
        'Region': np.random.choice(['North America', 'Europe', 'Asia', 'South America'], n_customers),
        'SignupDate': [(datetime(2023, 1, 1) + timedelta(days=np.random.randint(0, 365))).strftime('%Y-%m-%d') 
                      for _ in range(n_customers)]
    }
    pd.DataFrame(customers_data).to_csv('data/Customers.csv', index=False)
    
    # Generate Products data
    n_products = 100
    products_data = {
        'ProductID': [f'P{str(i).zfill(4)}' for i in range(1, n_products + 1)],
        'ProductName': [f'Product {i}' for i in range(1, n_products + 1)],
        'Category': np.random.choice(['Electronics', 'Clothing', 'Books', 'Home & Garden'], n_products),
        'Price': np.random.uniform(10, 1000, n_products).round(2)
    }
    pd.DataFrame(products_data).to_csv('data/Products.csv', index=False)
    
    # Generate Transactions data
    n_transactions = 1000
    transactions_data = {
        'TransactionID': [f'T{str(i).zfill(4)}' for i in range(1, n_transactions + 1)],
        'CustomerID': [f'C{str(np.random.randint(1, n_customers + 1)).zfill(4)}' for _ in range(n_transactions)],
        'ProductID': [f'P{str(np.random.randint(1, n_products + 1)).zfill(4)}' for _ in range(n_transactions)],
        'TransactionDate': [(datetime(2023, 1, 1) + timedelta(days=np.random.randint(0, 365))).strftime('%Y-%m-%d') 
                           for _ in range(n_transactions)],
        'Quantity': np.random.randint(1, 10, n_transactions),
        'Price': np.random.uniform(10, 1000, n_transactions).round(2)
    }
    transactions_data['TotalValue'] = np.array(transactions_data['Quantity']) * np.array(transactions_data['Price'])
    pd.DataFrame(transactions_data).to_csv('data/Transactions.csv', index=False)
    
    print("Sample data generated successfully!")

if __name__ == "__main__":
    generate_sample_data()