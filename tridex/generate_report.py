from datetime import datetime
import sys

from utils import yahoo_symbols, merge_company_names
from strategies import highest_percentage_difference

def export_report(strategy_function, index='ftse100'):
	date_now = datetime.now().strftime('%Y-%m-%d')

	if index == 'ftse100':
		ftse100_symbols = yahoo_symbols('../data/symbols/FTSE 100.txt')
		df = strategy_function(ftse100_symbols)
		df = merge_company_names(df)
		df.to_excel('../data/aggregated/FTSE100_report_{}.xlsx'.format(date_now), index=False)

	if index == 'ftse250':
		ftse250_symbols = yahoo_symbols('../data/symbols/FTSE 250.txt')
		df = strategy_function(ftse250_symbols)
		df = merge_company_names(df)
		df.to_excel('../data/aggregated/FTSE250_report_{}.xlsx'.format(date_now), index=False)


if __name__ == '__main__':
	# index = sys.argv[1]
	# if index in ['ftse100', 'ftse250']:
	export_report(highest_percentage_difference, 'ftse100')