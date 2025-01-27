# src/eda_utils.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class EDAAnalyzer:
    def __init__(self, customers_df, products_df, transactions_df):
        self.customers_df = customers_df
        self.products_df = products_df
        self.transactions_df = transactions_df
    
    def get_basic_stats(self):
        """Calculate basic statistics"""
        stats = {
            'customer_count': len(self.customers_df),
            'product_count': len(self.products_df),
            'transaction_count': len(self.transactions_df),
            'total_revenue': self.transactions_df['TotalValue'].sum(),
            'avg_transaction_value': self.transactions_df['TotalValue'].mean()
        }
        return stats
    
    def analyze_customer_behavior(self):
        """Analyze customer purchasing patterns"""
        customer_metrics = self.transactions_df.groupby('CustomerID').agg({
            'TransactionID': 'count',
            'TotalValue': ['sum', 'mean'],
            'Quantity': 'sum'
        }).reset_index()
        return customer_metrics