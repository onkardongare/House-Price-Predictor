import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from data_loader import load_data
from preprocessing import preprocess_data
from model import train_model, evaluate_model


def main():
    print("=== House Price Predictor MVP ===\n")
    
    print("Loading data...")
    housing = load_data()
    if housing is None:
        return
    
    print(f"Dataset shape: {housing.shape}")
    
    print("Preprocessing data...")
    housing_processed = preprocess_data(housing)
    
    X = housing_processed.drop('median_house_value', axis=1)
    y = housing_processed['median_house_value']
    
    print("Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    print("Scaling features...")
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    print("Training model...")
    model = train_model(X_train_scaled, y_train)
    
    rmse, mae = evaluate_model(model, X_test_scaled, y_test)
    
    print("\nSaving model and scaler...")
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/house_price_model.pkl")
    joblib.dump(scaler, "models/scaler.pkl")
    
    feature_importance = pd.DataFrame({
        'feature': X.columns,
        'importance': model.feature_importances_
    }).sort_values('importance', ascending=False)
    
    print("\n=== Top 5 Important Features ===")
    print(feature_importance.head(5).to_string(index=False))
    
    print("\n=== Done! Model saved to models/ directory ===")


if __name__ == "__main__":
    main()
