# Time Series Data Analysis

# Time Series 
# Time series data is one kind of dataset that is especially important. 
# This article delves into the complexities of time series datasets, examining their unique features 
# and how they may be utilized to gain significant insights.

# Time Series Visualization and Analysis
# Time series visualization and analytics empower users to graphically represent time-based data, 
# enabling the identification of trends and the tracking of changes over different periods. 

# Example 1: Stock Market Data - Continuous tracking of stock prices or values throughout trading hours.
# Example 2: Temperature Data: Continuous recordings of temperature at consistent intervals (e.g., hourly or daily measurements).


# Step 1 - Import Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.stattools import adfuller


# Step 2 - reading the dataset using read_csv
df = pd.read_csv("stock_data.csv", 
				parse_dates=True, 
				index_col="Date")

# displaying the first five rows of dataset
df.head()


# Step 3 - Assuming df is your DataFrame
sns.set(style="whitegrid") # Setting the style to whitegrid for a clean background

plt.figure(figsize=(12, 6)) # Setting the figure size
sns.lineplot(data=df, x='Date', y='High', label='High Price', color='blue')

# Adding labels and title
plt.xlabel('Date')
plt.ylabel('High')
plt.title('Share Highest Price Over Time')

plt.show()


# Step 4 - Assuming df is your DataFrame with a datetime index
df_resampled = df.resample('M').mean() # Resampling to monthly frequency, using mean as an aggregation function

sns.set(style="whitegrid") # Setting the style to whitegrid for a clean background

# Plotting the 'high' column with seaborn, setting x as the resampled 'Date'
plt.figure(figsize=(12, 6)) # Setting the figure size
sns.lineplot(data=df_resampled, x=df_resampled.index, y='High', label='Month Wise Average High Price', color='blue')

# Adding labels and title
plt.xlabel('Date (Monthly)')
plt.ylabel('High')
plt.title('Monthly Resampling Highest Price Over Time')

plt.show()


# Step 5 - Differencing
df['high_diff'] = df['High'].diff()

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(df['High'], label='Original High', color='blue')
plt.plot(df['high_diff'], label='Differenced High', linestyle='--', color='green')
plt.legend()
plt.title('Original vs Differenced High')
plt.show()




