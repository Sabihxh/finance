import os

import requests
from lxml import html

"""
If this file is run directly then saves ftse350 stock codes in 
a file. 
Note: This will override the existing file


Url for any index on lse website is the base_index_url + suffix 

"""
base_index_url = 'https://www.londonstockexchange.com/exchange/prices-and-markets/stocks/indices/summary/summary-indices-constituents.html?index='
suffix_index_urls = {
	'FTSE 100': ('UKX&page=', 6), # (url, no of pages)
	'FTSE 250': ('MCX&page=', 13),
	'FTSE 350': ('NMX&page=', 18),
	'FTSE ALL-SHARE': ('ASX&page=', 32),
	'FTSE AIM UK 50': ('AIM5&page=', 3),
	'FTSE AIM 100': ('AIM1&page=', 6),
	'FTSE AIM ALL-SHARE': ('AXX&page=', 39),
}


def scrape_stock_symbols(index):
	"""
	Scrapes stock codes from london stock exchange website
	and returns list of codes
	"""
	result = []
	url_suffix = suffix_index_urls[index][0]
	last_page_no = suffix_index_urls[index][1]

	for x in range(1, last_page_no + 1):
		url = base_index_url + url_suffix + str(x)
		print('Scraping: {}'.format(url))
		page = requests.get(url)
		tree = html.fromstring(page.content)
		symbols = tree.xpath('//td[@scope="row" and @class="name"]/text()')
		result.extend(symbols)
	return result


if __name__ == '__main__':
	symbols_output_dir = '../data/symbols'
	for index in suffix_index_urls.keys():
		print(index)
		stock_codes = scrape_stock_symbols(index)
		fp = os.path.join(symbols_output_dir, '{}_symbols.txt'.format(index))
		with open(fp, 'w') as f:
			f.write('\n'.join(stock_codes))

