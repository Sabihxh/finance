import os

from pandas_datareader import DataReader


def get_stock_codes():
	result = []
	stock_codes_fp = './data_codes/scraped_ftse350_stock_codes.txt'
	with open(stock_codes_fp) as f:
		data = f.read()
		for code in data.split('\n'):
			result.append(code)
	return result


def yahoo_stock_codes(stock_codes):
	result = []
	for code in stock_codes:
		code = code.strip('.').replace('.', '-') + '.L'
		result.append(code)
	return result


# Parameters for DataReader
access_key = None
data_source = 'yahoo'
start_date = '2014-01-01'
output_dir = './data_stocks'


def download_stocks_data():
	stock_codes = get_stock_codes()
	stock_codes = yahoo_stock_codes(stock_codes)

	for code in stock_codes:
		print('Fetching data from yahoo: {}'.format(code))
		output_fp = os.path.join(output_dir, code + '.csv')
		if os.path.exists(output_fp):
			print('File already exists: {}'.format(output_fp))
			continue
		df = DataReader(name=code, data_source=data_source, start=start_date, access_key=access_key)
		df.to_csv(output_fp)
		print('Successfully Downloaded {}'.format(code))
		print('*'*20)

download_stocks_data()
























