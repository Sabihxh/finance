import os

import requests
from lxml import html

from globals import base_index_url, index_url_suffix


def scrape_stock_symbols(index):
	"""
	Scrapes stock codes from london stock exchange website
	and returns list of codes
	"""
	result = []
	url_suffix = index_url_suffix[index][0]
	last_page_no = index_url_suffix[index][1]

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
	for index in index_url_suffix.keys():
		print('\n--- {} ---'.format(index))
		stock_codes = scrape_stock_symbols(index)
		fp = os.path.join(symbols_output_dir, '{}.txt'.format(index))
		with open(fp, 'w') as f:
			f.write('\n'.join(stock_codes))

