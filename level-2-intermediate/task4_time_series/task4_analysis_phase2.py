import pandas as pd
from statsmodels.tsa.stattools import adfuller

def check_stationarity(timeseries):
    """
    Performs the Augmented Dickey-Fuller test to check for stationarity.
    """
    print("--- Results of Dickey-Fuller Test ---")
    result = adfuller(timeseries, autolag='AIC')
    
    # Organising results into a readable format
    stats = pd.Series(result[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
    for key, value in result[4].items():
        stats[f'Critical Value ({key})'] = value
        
    print(stats)
    
    if result[1] <= 0.05:
        print("\nConclusion: Data is Stationary (Reject Null Hypothesis)")
    else:
        print("\nConclusion: Data is Non-Stationary (Trending Series)")

# 1. Load data with lowercase names
df = pd.read_csv('stock_prices_dataset.csv', parse_dates=['date'], index_col='date')

# 2. Resample to Monthly End ('ME') for stability
monthly_df = df['close'].resample('ME').mean()

# 3. Call the function on our resampled data
check_stationarity(monthly_df)