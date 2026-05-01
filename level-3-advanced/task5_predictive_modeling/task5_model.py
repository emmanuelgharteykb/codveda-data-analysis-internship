import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# 1. Load your datasets
train_df = pd.read_csv('churn-bigml-80.csv')
test_df = pd.read_csv('churn-bigml-20.csv')

# 2. Separate Features and Target
X_train = train_df.drop('Churn', axis=1)
y_train = train_df['Churn'].astype(int) # Convert False/True to 0/1
X_test = test_df.drop('Churn', axis=1)
y_test = test_df['Churn'].astype(int)

# 3. Automatic Column Selection
# Find categorical columns (words) and numerical columns (numbers)
cat_cols = X_train.select_dtypes(include=['object']).columns.tolist()
num_cols = X_train.select_dtypes(include=['int64', 'float64']).columns.tolist()

# 4. Create Preprocessing Pipeline (Standardization and Encoding)
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), num_cols),
        ('cat', OneHotEncoder(handle_unknown='ignore'), cat_cols)
    ])

# 5. Define two models to compare
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42)
}

# 6. Loop through models, train, and evaluate
for name, model in models.items():
    # Create a full pipeline for each model
    pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', model)
    ])
    
    # Train
    pipeline.fit(X_train, y_train)
    
    # Predict
    y_pred = pipeline.predict(X_test)
    
    # Report results
    print(f"\n{'='*30}")
    print(f" MODEL: {name}")
    print(f"{'='*30}")
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
    print("\nDetailed Report:")
    print(classification_report(y_test, y_pred))