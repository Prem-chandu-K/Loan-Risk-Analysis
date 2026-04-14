import pandas as pd

def load_loan_data():
    
    df = pd.read_csv("sample_data/RetailLendingRiskIntelligence.csv")
    print("Dataset Loaded | Shape:", df.shape)
    return df