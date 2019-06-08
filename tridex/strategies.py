import os
import numpy as np
import pandas as pd

from download_data import download_data
from utils import index_symbol_map, yahoo_symbols


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

def percentage_difference(df, days_1=5, days_2=200):
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
# print(percentage_difference(test_df, days_1=2, days_2=5))


def highest_percentage_difference(symbols):
	"""
	Takes stock symbols and uses percentage_difference
	function to rank the stocks.

	Returns dataframe ranked in descending order of
	percentage difference.

	"""
	result = pd.DataFrame()
	base_data_dir = '../data/stocks/'
	index_map = index_symbol_map()

	for symbol in symbols:
		print(symbol)
		market_index = index_map.get(symbol, [''])[0]
		if not market_index:
			print('Warning: {} does not have a market...')
			continue

		fp = os.path.join(base_data_dir, market_index, symbol + '.csv')
		if not os.path.exists(fp):
			download_data([symbol])

		df = pd.read_csv(fp)
		
		means_diff_percent = percentage_difference(df, days_1=5, days_2=200)
			
		df = df.iloc[-1:]
		df['symbol'] = symbol
		df['means_diff_percent'] = means_diff_percent
		result = pd.concat([result, df])
	
	result = result.sort_values(by='means_diff_percent', ascending=False)
	return result


# highest_percentage_difference(['BARC.L', 'SPX.L', 'SVS.L', 'YOU.L'])

ftse100_symbols = yahoo_symbols('../data/symbols/FTSE 100.txt')
ftse250_symbols = yahoo_symbols('../data/symbols/FTSE 250.txt')

highest_percentage_difference(ftse100_symbols).to_excel('../data/aggregated/FTSE100_report_08June2019.xlsx')
highest_percentage_difference(ftse250_symbols).to_excel('../data/aggregated/FTSE250_report_08June2019.xlsx')












