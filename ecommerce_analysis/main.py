# main.py
from src.data_loader import DataLoader
from src.eda_utils import EDAAnalyzer
from src.lookalike_model import LookalikeModel
from src.clustering import CustomerSegmentation

def main():
    # Load data
    loader = DataLoader()
    customers_df, products_df, transactions_df = loader.load_all_data()
    
    # Perform EDA
    analyzer = EDAAnalyzer(customers_df, products_df, transactions_df)
    basic_stats = analyzer.get_basic_stats()
    
    # Generate lookalike recommendations
    model = LookalikeModel(customers_df, products_df, transactions_df)
    target_customers = customers_df['CustomerID'].iloc[:20]
    
    # Perform clustering
    segmentation = CustomerSegmentation(customers_df, products_df, transactions_df)
    optimal_clusters = segmentation.find_optimal_clusters()

if __name__ == "__main__":
    main()