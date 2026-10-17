import pandas as pd
import os


def load_data():
    data_path = os.path.join("data", "01", "housing.csv")
    if not os.path.exists(data_path):
        print("Data file not found. Please download the data first.")
        return None
    return pd.read_csv(data_path)
