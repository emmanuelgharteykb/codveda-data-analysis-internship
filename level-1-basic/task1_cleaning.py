import pandas as pd

# ASSUMPTION: Based on the 14-column structure and 'House Prediction' context, 
# I am treating this as the Boston Housing Dataset and applying standard headers.

# Step A: Creating a list of names for the columns
names_list = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'PRICE']

# Step B: Opening the file and telling Python "Use these names!"
# I used 'header=None' because the file doesn't have its own titles.
df = pd.read_csv('house_prediction.csv', header=None, names=names_list)

# Step C: Showing the first 5 rows on the screen so I can see the titles
print("Look! Now the numbers have titles at the top:")
print(df.head())

# Step D: Saving this as a NEW, clean file
df.to_csv('cleaned_house_data.csv', index=False)
print("\nDone! You now have a file called 'cleaned_house_data.csv' that makes sense.")