# src/clustering.py
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import davies_bouldin_score
import matplotlib.pyplot as plt

class CustomerSegmentation:
    def __init__(self, customers_df, products_df, transactions_df):
        self.customers_df = customers_df
        self.products_df = products_df
        self.transactions_df = transactions_df
        
    def prepare_features(self):
        """Prepare features for clustering"""
        # Merge relevant data and create features
        customer_transactions = pd.merge(
            self.transactions_df,
            self.customers_df[['CustomerID', 'Region']],
            on='CustomerID'
        )
        
        # Calculate customer metrics
        customer_features = customer_transactions.groupby('CustomerID').agg({
            'TransactionID': 'count',
            'TotalValue': ['sum', 'mean'],
            'Quantity': 'sum'
        })
        
        return customer_features
    
    def find_optimal_clusters(self, max_clusters=10):
        """Find optimal number of clusters using DB Index"""
        features = self.prepare_features()
        scaler = StandardScaler()
        scaled_features = scaler.fit_transform(features)
        
        db_scores = []
        for k in range(2, max_clusters + 1):
            kmeans = KMeans(n_clusters=k, random_state=42)
            clusters = kmeans.fit_predict(scaled_features)
            db_scores.append(davies_bouldin_score(scaled_features, clusters))
            
        return db_scores