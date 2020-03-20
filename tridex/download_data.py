from datetime import datetime
import os

import pandas as pd
from pandas_datareader import DataReader


from utils import yahoo_symbols, extract_symbol, index_symbol_map


# Global parameters for DataReader - change if yahoo breaks again
ACCESS_KEY = None
DATA_SOURCE = 'yahoo'
INITIAL_DATE = '2014-01-01'

CURRENT_DATE = datetime.now().strptime

ftse100_symbols = yahoo_symbols('../data/symbols/FTSE 100.txt')
ftse250_symbols = yahoo_symbols('../data/symbols/FTSE 250.txt')


def get_data(symbol):
	"""
	returns df
	"""
	return DataReader(name=symbol, data_source=DATA_SOURCE, start=INITIAL_DATE, access_key=ACCESS_KEY)
	


def data_to_bigquery(symbol):
	"""
	Downloads data and saves in csv format.
	"""
	df = get_data(symbol)
	



def download_data(symbols):
	"""
	Time ~80sec
	Note: This function will download all data and replace the existing csv files.
	
	Parameters:
		symbols (list): List of strings where each string is a 
			yahoo stock symbol e.g. ['BARC.L', 'HSBA.L']

	"""
	# Parameters for DataReader
	base_output_dir = '../data/stocks/{}/'
	total_symbols = len(symbols)
	index_map = index_symbol_map()

	for i, symbol in enumerate(symbols):
		print('Downloading: {}/{} >>> {}'.format(i+1, total_symbols, symbol))

		market = index_map.get(symbol, [''])[0]
		if not market:
			print('Warning: {} does not have a market...')
			continue

		output_dir = base_output_dir.format(market)
		if not os.path.exists(output_dir):
			os.makedirs(output_dir)

		output_fp = os.path.join(output_dir, symbol + '.csv')
		try:
			get_data(symbol).to_csv(output_fp)
		except:
			print('cannot get data...')


def main():
	print('main...')
	download_data(ftse100_symbols)
	download_data(ftse250_symbols)
	# update_data(market='FTSE250')


if __name__ == '__main__':
	main()









