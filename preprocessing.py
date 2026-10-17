import pandas as pd


def preprocess_data(df):
    df = df.copy()
    df['total_bedrooms'].fillna(df['total_bedrooms'].median(), inplace=True)
    df = pd.get_dummies(df, columns=['ocean_proximity'], drop_first=True)
    return df
