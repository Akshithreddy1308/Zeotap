# src/lookalike_model.py
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity

class LookalikeModel:
    def __init__(self, customers_df, products_df, transactions_df):
        self.customers_df = customers_df
        self.products_df = products_df
        self.transactions_df = transactions_df
        
    def create_customer_features(self):
        """Create feature matrix for customers"""
        # Merge transactions with products to get categories
        transactions_with_categories = pd.merge(
            self.transactions_df,
            self.products_df[['ProductID', 'Category']],
            on='ProductID'
        )
        
        # Create purchase patterns by category
        category_patterns = pd.pivot_table(
            transactions_with_categories,
            values='Quantity',
            index='CustomerID',
            columns='Category',
            aggfunc='sum',
            fill_value=0
        )
        
        return category_patterns
    
    def find_similar_customers(self, customer_id, n=3):
        """Find n most similar customers"""
        features = self.create_customer_features()
        scaler = StandardScaler()
        scaled_features = scaler.fit_transform(features)
        
        similarities = cosine_similarity(scaled_features)
        similar_indices = similarities[features.index.get_loc(customer_id)].argsort()[::-1][1:n+1]
        
        similar_customers = pd.DataFrame({
            'similar_customer_id': features.index[similar_indices],
            'similarity_score': similarities[features.index.get_loc(customer_id)][similar_indices]
        })
        
        return similar_customers