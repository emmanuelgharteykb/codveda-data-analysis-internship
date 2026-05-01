import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report, confusion_matrix

# 1. Load datasets
train_df = pd.read_csv('churn-bigml-80.csv')
test_df = pd.read_csv('churn-bigml-20.csv')

X_train = train_df.drop('Churn', axis=1)
y_train = train_df['Churn'].astype(int)
X_test = test_df.drop('Churn', axis=1)
y_test = test_df['Churn'].astype(int)

# 2. Preprocessing Setup
cat_cols = X_train.select_dtypes(include=['object']).columns.tolist()
num_cols = X_train.select_dtypes(include=['int64', 'float64']).columns.tolist()

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), num_cols),
        ('cat', OneHotEncoder(handle_unknown='ignore'), cat_cols)
    ])

# 3. Create Pipeline with a placeholder for Random Forest
full_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(random_state=42))
])

# 4. Define the Grid of Parameters to test
# We are testing different 'depths' of trees and different 'number of trees'
param_grid = {
    'classifier__n_estimators': [100, 200],
    'classifier__max_depth': [None, 10, 20],
    'classifier__min_samples_split': [2, 5]
}

# 5. Set up Grid Search
# 'cv=3' means it will cross-validate (test on itself) 3 times for each setting
grid_search = GridSearchCV(full_pipeline, param_grid, cv=3, scoring='f1', n_jobs=-1)

print("--- Starting Hyperparameter Tuning (This may take a moment) ---")
grid_search.fit(X_train, y_train)

# 6. Evaluate the Best Model
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)

print("\n--- Phase 2: Optimized Random Forest Results ---")
print(f"Best Parameters found: {grid_search.best_params_}")
print("\nFinal Classification Report:")
print(classification_report(y_test, y_pred))


# 1. Get the predictions (0 or 1)
predictions = best_model.predict(X_test)

# 2. Add the predictions back to the original test dataframe
# This creates a new column called 'Predicted_Churn'
results_df = test_df.copy()
results_df['Predicted_Churn'] = predictions

# 3. Filter the list to show ONLY the customers the model flagged as 1 (Churn)
at_risk_customers = results_df[results_df['Predicted_Churn'] == 1]

# 4. Show the "High-Risk" list
print("\n--- IDENTIFIED HIGH-RISK CUSTOMERS ---")
# If your dataset has a phone number or ID column, include it here
print(at_risk_customers.head(10)) 

# 5. Export this to a CSV for the "Marketing Team"
at_risk_customers.to_csv('high_risk_customers.csv', index=False)
print(f"\nSuccessfully identified {len(at_risk_customers)} customers at risk. File saved!")