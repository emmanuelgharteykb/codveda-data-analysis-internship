import pandas as pd

# 1. Load data
names_list = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'PRICE']
df = pd.read_csv('house_prediction.csv', header=None, names=names_list, sep='\s+')

# 2. APPLY REAL-LIFE FORMATTING
# Define which columns get which treatment
int_cols = ['ZN', 'CHAS', 'AGE', 'RAD', 'TAX']
high_prec_cols = ['CRIM', 'NOX']
std_prec_cols = ['INDUS', 'RM', 'DIS', 'PTRATIO', 'B', 'LSTAT', 'PRICE']

# Convert Whole Numbers
for col in int_cols:
    df[col] = df[col].round(0).astype(int)

# Apply Specific Rounding
for col in high_prec_cols:
    df[col] = df[col].round(5)

for col in std_prec_cols:
    df[col] = df[col].round(2)

# 3. VERIFY OUTPUT
print("--- Final Professional Dataset (Task 1 Complete) ---")
# Using to_string() ensures the terminal doesn't hide columns
print(df.head().to_string(index=False))

# 4. SAVE THE CLEAN FILE
df.to_csv('cleaned_house_data.csv', index=False)
