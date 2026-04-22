import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Loadng the same clean data from my level 1 basic tasks. 
# I firstly copied the dataset from the level-1-basic directory just so there wont be any issues with running the Python script
df = pd.read_csv('cleaned_house_data.csv')

# 2. Define Features (X) and Target (y)
X = df.drop('PRICE', axis=1)
y = df['PRICE']

# 3. Split the data: 80% for learning, 20% for the "final exam"
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Train the "Brain" (The Linear Regression Model)
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Test the Model
y_pred = model.predict(X_test)

# 6. View Results
print("--- LEVEL 2: TASK 3 MODEL RESULTS ---")
print(f"R-squared Score: {r2_score(y_test, y_pred):.4f}")
print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred):.4f}")

# Compare a real world example
print(f"\nFirst test house:")
print(f"Actual Price: ${y_test.iloc[0]*1000:,.2f}")
print(f"Predicted Price: ${y_pred[0]*1000:,.2f}")
