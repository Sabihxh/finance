import os




def lse_to_yahoo(symbol):
	"""
	Converts ticker symbol from london stock exhange
	to yahoo finance e.g. BARC >> BARC.L

	"""
	return symbol.strip('.').replace('.', '-') + '.L'


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


def extract_symbol(fp):
	"""
	Returns yahoo symbol given a filepath with symbol name in it
	e.g. 
	Input: fp = './data_stocks/FTSE100/BARC.L.csv' 
	Output: BARC.L
	"""
	return fp.strip('/').rsplit('/', 1)[1].rsplit('.', 1)[0]

