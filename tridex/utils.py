import os

from globals import index_url_suffix


def lse_to_yahoo(symbol):
	"""
	Converts ticker symbol from london stock exhange
	to yahoo finance e.g. BARC >> BARC.L

	"""
	return symbol.strip('.').replace('.', '-') + '.L'


def extract_symbol(fp):
	"""
	Returns yahoo symbol given a filepath with symbol name in it
	e.g. 
	Input: fp = './data_stocks/FTSE100/BARC.L.csv' 
	Output: BARC.L
	"""
	return fp.strip('/').rsplit('/', 1)[1].rsplit('.', 1)[0]


def yahoo_symbols(fp):
	"""
	Takes a filepath with LSE symbols, converts
	the symbols to yahoo symbols and returns a list.

	"""
	result = []
	with open(fp) as f:
		data = f.read()
		for symbol in data.split('\n'):
			symbol = lse_to_yahoo(symbol)
			result.append(symbol)
	return sorted(result)


def index_symbol_map():
	result = {}
	for index in index_url_suffix.keys():
		index_fp = os.path.join('../data/symbols/', index + '.txt')
		with open(index_fp, 'r') as f:
			for symbol in f.readlines():
				symbol = lse_to_yahoo(symbol.strip())
				if symbol not in result:
					result[symbol] = []
				result[symbol].append(index)
	return result









