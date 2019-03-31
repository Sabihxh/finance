import requests
from lxml import html

"""
If this file is run directly then saves ftse350 stock codes in 
a file. 
Note: This will override the existing file
"""

def ftse350_stock_codes():
	"""
	Scrapes stock codes from london stock exchange website
	and returns list of codes
	"""
	stock_codes = []
	base_url = "https://www.londonstockexchange.com/exchange/prices-and-markets/stocks/indices/summary/summary-indices-constituents.html?index=NMX&page={}"
	for x in range(1, 19):
		url = base_url.format(x)
		print('Scraping: {}'.format(url))
		page = requests.get(url)
		tree = html.fromstring(page.content)
		codes = tree.xpath('//td[@scope="row" and @class="name"]/text()')
		stock_codes.extend(codes)
	return stock_codes


def ftse100_stock_codes():
	"""
	Scrapes stock codes from london stock exchange website
	and returns list of codes
	"""
	stock_codes = []
	base_url = "https://www.londonstockexchange.com/exchange/prices-and-markets/stocks/indices/summary/summary-indices-constituents.html?index=UKX&page={}"
	for x in range(1, 7):
		url = base_url.format(x)
		print('Scraping: {}'.format(url))
		page = requests.get(url)
		tree = html.fromstring(page.content)
		codes = tree.xpath('//td[@scope="row" and @class="name"]/text()')
		stock_codes.extend(codes)
	return stock_codes



if __name__ == '__main__':
	stock_codes = ftse350_stock_codes()
	fp = './data_codes/lse_ftse350_stock_codes_scraped_html.txt'
	with open(fp, 'w') as f:
		f.write('\n'.join(stock_codes))

	stock_codes = ftse100_stock_codes()
	fp = './data_codes/lse_ftse100_stock_codes_scraped_html.txt'
	with open(fp, 'w') as f:
		f.write('\n'.join(stock_codes))









