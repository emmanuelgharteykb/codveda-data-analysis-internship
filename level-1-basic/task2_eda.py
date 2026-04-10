import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Load the perfectly cleaned data from your screenshot
df = pd.read_csv('cleaned_house_data.csv')

# Step 2: Summary Statistics
print("\n--- OBJECTIVE 1: SUMMARY STATISTICS ---")
print(df.describe())

# Step 3: Distribution Plot (Histograms)
print("\n--- OBJECTIVE 2: VISUALIZING DISTRIBUTIONS ---")
plt.figure(figsize=(10, 6))
sns.histplot(df['PRICE'], kde=True, color='blue')
plt.title('Distribution of House Prices')
plt.xlabel('Price ($1000s)')
plt.ylabel('Number of Houses')
plt.savefig('price_distribution.png')
print("Saved: price_distribution.png")

# Step 4: Correlation Matrix (Find Patterns)
print("\n--- OBJECTIVE 3: FINDING CORRELATIONS ---")
plt.figure(figsize=(12, 10))
# Calculate the relationship between all columns
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Feature Correlation Heatmap')
plt.savefig('correlation_heatmap.png')
print("Saved: correlation_heatmap.png")

print("\n✅ Task 2 EDA Script finished successfully!")
