import os

from pandas_datareader import DataReader


def lse_to_yahoo(symbol):
	"""
	Converts ticker symbol from london stock exhange
	to yahoo finance e.g. BARC >> BARC.L
	"""
	return symbol.strip('.').replace('.', '-') + '.L'


def yahoo_symbols(fp):
	"""
	Reads .txt file with all symbols listed on 
	London Stock Exchange and returns a list
	of yahoo version of those symbols e.g. BARC >> BARC.L
	"""
	result = []
	with open(fp) as f:
		data = f.read()
		for symbol in data.split('\n'):
			symbol = lse_to_yahoo(symbol)
			result.append(symbol)
	return sorted(result)	


def download_ftse100_data():
	"""
	Downloads data for all stocks in FTSE 100.
	Time taken ~80sec
	"""
	# Parameters for DataReader
	access_key = None
	data_source = 'yahoo'
	start_date = '2014-01-01'
	output_dir = './data_stocks/FTSE100/'

	symbols_fp = './data_symbols/ftse100_symbols.txt'
	symbols = yahoo_symbols(symbols_fp)
	total_symbols = len(symbols)

	for i, symbol in enumerate(symbols):
		print('{}/{} >>> {}'.format(i+1, total_symbols, symbol))
		output_fp = os.path.join(output_dir, symbol + '.csv')
		df = DataReader(name=symbol, data_source=data_source, start=start_date, access_key=access_key)
		df.to_csv(output_fp)


if __name__ == '__main__':
	download_ftse100_data()



