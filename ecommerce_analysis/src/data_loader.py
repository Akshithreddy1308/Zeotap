# src/data_loader.py
import pandas as pd
from pathlib import Path
import os

class DataLoader:
    def __init__(self, data_dir='data'):
        # Get the current file's directory
        current_dir = Path(os.getcwd())
        
        # If we're in the notebooks directory, go up one level
        if current_dir.name == 'notebooks':
            current_dir = current_dir.parent
            
        self.data_dir = current_dir / data_dir
        
    def load_all_data(self):
        """Load all datasets"""
        # Print the path being used for debugging
        print(f"Looking for data files in: {self.data_dir}")
        
        try:
            customers = pd.read_csv(self.data_dir / 'Customers.csv')
            products = pd.read_csv(self.data_dir / 'Products.csv')
            transactions = pd.read_csv(self.data_dir / 'Transactions.csv')
            
            # Convert date columns
            customers['SignupDate'] = pd.to_datetime(customers['SignupDate'])
            transactions['TransactionDate'] = pd.to_datetime(transactions['TransactionDate'])
            
            return customers, products, transactions
        except FileNotFoundError as e:
            print(f"Error: Could not find data files in {self.data_dir}")
            print("Please ensure you have run generate_sample_data.py first")
            raise e