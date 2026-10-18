
from predictor import predict_price


def get_user_input():
    print("\n=== House Price Predictor ===")
    print("Enter the following features:\n")
    
    try:
        longitude = float(input("Longitude (e.g., -122.23): "))
        latitude = float(input("Latitude (e.g., 37.88): "))
        housing_median_age = float(input("Housing Median Age (years): "))
        total_rooms = float(input("Total Rooms: "))
        total_bedrooms = float(input("Total Bedrooms: "))
        population = float(input("Population: "))
        households = float(input("Households: "))
        median_income = float(input("Median Income (in tens of thousands, e.g., 8.3): "))
        ocean_proximity = input("Ocean Proximity (NEAR BAY, <1H OCEAN, INLAND, NEAR OCEAN, ISLAND): ").upper()
        
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
        
        return features
        
    except ValueError as e:
        print(f"\nError: Please enter valid numbers. {e}")
        return None


def main():
    while True:
        features = get_user_input()
        
        if features:
            predict_price(features)
        
        # Ask if user wants to continue
        choice = input("\nPredict another house? (y/n): ").lower()
        if choice != 'y':
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()
