import pandas as pd
import joblib
import os
from data_loader import load_data
from preprocessing import preprocess_data


def predict_price(features_dict):
    if not os.path.exists("models/house_price_model.pkl"):
        print("Model not found. Please train the model first.")
        return
    
    model = joblib.load("models/house_price_model.pkl")
    scaler = joblib.load("models/scaler.pkl")
    
    housing = load_data()
    housing_processed = preprocess_data(housing)
    feature_columns = housing_processed.drop('median_house_value', axis=1).columns
    
    input_df = pd.DataFrame([features_dict])
    input_df = pd.get_dummies(input_df, columns=['ocean_proximity'], drop_first=True)
    
    for col in feature_columns:
        if col not in input_df.columns:
            input_df[col] = 0
    
    input_df = input_df[feature_columns]
    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)[0]
    
    print(f"\n=== Prediction ===")
    print(f"Estimated House Price: ${prediction:,.2f}")
    
    return prediction
