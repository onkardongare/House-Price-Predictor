import streamlit as st
import pandas as pd
import joblib
import os
from data_loader import load_data
from preprocessing import preprocess_data


def load_model():
    if not os.path.exists("models/house_price_model.pkl"):
        return None, None
    model = joblib.load("models/house_price_model.pkl")
    scaler = joblib.load("models/scaler.pkl")
    return model, scaler


def get_feature_columns():
    housing = load_data()
    housing_processed = preprocess_data(housing)
    return housing_processed.drop('median_house_value', axis=1).columns


def main():
    st.title("House Price Predictor")
    st.write("Enter house features to predict the price")

    model, scaler = load_model()
    
    if model is None:
        st.error("Model not found. Please train the model first by running: python train.py")
        return

    st.sidebar.header("Input Features")

    longitude = st.sidebar.slider("Longitude", -124.5, -114.3, -122.23)
    latitude = st.sidebar.slider("Latitude", 32.5, 42.0, 37.88)
    housing_median_age = st.sidebar.slider("Housing Median Age", 1, 52, 41)
    total_rooms = st.sidebar.slider("Total Rooms", 2, 40000, 880)
    total_bedrooms = st.sidebar.slider("Total Bedrooms", 1, 6500, 129)
    population = st.sidebar.slider("Population", 3, 36000, 322)
    households = st.sidebar.slider("Households", 1, 6100, 126)
    median_income = st.sidebar.slider("Median Income", 0.5, 15.0, 8.3)
    ocean_proximity = st.sidebar.selectbox("Ocean Proximity", ["NEAR BAY", "<1H OCEAN", "INLAND", "NEAR OCEAN", "ISLAND"])

    features = {
        'longitude': longitude,
        'latitude': latitude,
        'housing_median_age': housing_median_age,
        'total_rooms': total_rooms,
        'total_bedrooms': total_bedrooms,
        'population': population,
        'households': households,
        'median_income': median_income,
        'ocean_proximity': ocean_proximity
    }

    if st.button("Predict Price"):
        input_df = pd.DataFrame([features])
        input_df = pd.get_dummies(input_df, columns=['ocean_proximity'], drop_first=True)
        
        feature_columns = get_feature_columns()
        
        for col in feature_columns:
            if col not in input_df.columns:
                input_df[col] = 0
        
        input_df = input_df[feature_columns]
        input_scaled = scaler.transform(input_df)
        prediction = model.predict(input_scaled)[0]
        
        st.success(f"Estimated House Price: ${prediction:,.2f}")


if __name__ == "__main__":
    main()
