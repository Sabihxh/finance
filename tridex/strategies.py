import os
import numpy as np
import pandas as pd


"""
#### Largest gap between long term moving average and very short term moving average

Long term MA = 200 days<br>
Short term MA = 5 days

There is bound to be a pull back or short term price reversal when the gap between MA 200 and MA 5 is large.

Strategy is to itterate through all stocks and find the ones with the largest gap between the two moving averages.

The gap needs to be in percentage, so that we can compare the gap between different stocks.<br>
Example:

	symbol: LLOY.L
	date: 28/12/2018
	MA 200 = 61.01 
	MA 5 = 50.94
	gap = 16.5%
	calculation: (61.01 - 50.94)/61.01

"""

def moving_average_diff(df, days_1=5, days_2=200):
	"""
	Takes dataframe with 'Close' column	
	(close price of stock) and returns the 
	percentage difference between 5 and 200 day
	moving average.

	Psuedo code:
		- Get 200 day mean
		- Get 5 day mean
		- Calculate difference
		- Calculate difference in percent relative to 200 day mean

	Note: Can use any number of days
	"""
	if days_1 > days_2:
		days_2, days_1 = days_1, days_2

	mean_1, mean_2 = df.iloc[-days_1:]['Close'].mean(), df.iloc[-days_2:]['Close'].mean()
	return ((mean_2 - mean_1) / mean_2) * 100


# test_df = pd.DataFrame({'Close': [3,2,2,2,2]})
# print(moving_average_diff(test_df, days_1=2, days_2=5))


def highest_moving_average_diff(symbols):
	"""
	Takes stock symbols and uses moving_average_diff
	function to rank the stocks.

	Returns dataframe ranked in descending order of
	percentage difference.

	"""
	
	return
	result = pd.DataFrame()
	for symbol, df in get_dfs(stocks_csv_files).items():
		mean_200, mean_5 = df.iloc[-200:]['Close'].mean(), df.iloc[-5:]['Close'].mean()
		means_diff_percent = ((mean_200 - mean_5) / mean_200) * 100
		
		# Skip the stocks whose mean percentage diference is negative
		if means_diff_percent < 0:
			continue
			
		df = df.iloc[-1:].copy()
		df['symbol'] = symbol
		df['means_diff_percent'] = means_diff_percent
		result = pd.concat([result, df])
	
	result = result.sort_values(by='means_diff_percent')
	return result


highest_moving_average_diff(['BARC.L'])



