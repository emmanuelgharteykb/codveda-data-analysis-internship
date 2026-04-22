import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# 1. Loading and preparing the time series data
df = pd.read_csv('stock_prices_dataset.csv', parse_dates=['date'], index_col='date')

# 2. Resample to Monthly frequency. This takes average stock price for each month.
# This is important because stock prices can be very volatile on a daily basis, and resampling helps to smooth out the data and reveal underlying trends.
# This then removes daily noise so we can see the bigger picture of how the stock price is changing over time.
monthly_df = df['close'].resample('ME').mean()

# 3. Calculate a rolling average (mean) for a 3 month window. This helps to further smooth the data and identify trends.
# This helps visualise the direction the price is "rolling" towards, and can help identify support and resistance levels in the stock price.
rolling_mean = monthly_df.rolling(window=3).mean()

# 4. Seasonal Decomposition: This breaks down the time series into its components: trend, seasonality, and residuals.
# This helps to understand the underlying patterns in the data, such as whether there are regular seasonal fluctuations in the stock price, and to identify any long-term trends.
# This breaks the data into: Trend, Seasonality, and Residuals (noise).
decomposition = seasonal_decompose(monthly_df, model='additive')

# 5. Plotting the results
plt.figure(figsize=(12, 8))

# Subplot 1: Original Time Series vs Rolling Mean
plt.subplot(211)
plt.plot(monthly_df, label='Monthly Average Price', color='blue', alpha=0.5)
plt.plot(rolling_mean, label='3-Month Rolling Mean', color='red', linewidth=2)
plt.title('Stock Price Over Time with Rolling Mean')
plt.legend()

# Subplot 2: The Trend Component from Seasonal Decomposition
plt.subplot(212)
plt.plot(decomposition.trend, color='green')
plt.title('Isolated Trend Component from Seasonal Decomposition')

plt.tight_layout()
plt.show()
