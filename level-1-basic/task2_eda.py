import pandas as pd

# Load the cleaned data from Task 1
try:
    df = pd.read_csv('cleaned_house_data.csv')
    print("✅ Data loaded successfully!\n")
    
    # Objective 1: Summary Statistics
    print("--- Summary Statistics ---")
    # This gives us mean, std, min, 25%, 50% (median), 75%, and max
    stats = df.describe()
    print(stats)
    
    # Let's also find the Mode specifically
    print("\n--- Mode of Price ---")
    print(df['PRICE'].mode()[0])

except FileNotFoundError:
    print("❌ Error: 'cleaned_house_data.csv' not found. Make sure it's in this folder!")
