import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# 1. Loadng the same clean data from my level 1 basic tasks
df = pd.read_csv('cleaned_house_data.csv')

# 2. Features and Target
X = df.drop('PRICE', axis=1)
y = df['PRICE']

# 3. Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Train the Random Forest Model
# n_estimators=100 means we are using 100 "decision trees" to vote on the price
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 5. Make Predictions
y_pred = model.predict(X_test)

# 6. Evaluation
print("--- LEVEL 2: RANDOM FOREST RESULTS ---")
print(f"R-squared Score: {r2_score(y_test, y_pred):.4f}")
print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred):.4f}")

# Comparison
print(f"\nFirst test house:")
print(f"Actual Price: ${y_test.iloc[0]*1000:,.2f}")
print(f"Predicted Price: ${y_pred[0]*1000:,.2f}")