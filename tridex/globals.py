"""
This file contains all types of objects that
need to be used globally, e.g. urls for stock symbols etc
"""


# Url for any index on lse website is the base_index_url + suffix 
base_index_url = 'https://www.londonstockexchange.com/exchange/prices-and-markets/stocks/indices/summary/summary-indices-constituents.html?index='
index_url_suffix = {
	'FTSE 100': ('UKX&page=', 6), # (url suffix, no. of pages)
	'FTSE 250': ('MCX&page=', 13),
	'FTSE 350': ('NMX&page=', 18),
	'FTSE ALL-SHARE': ('ASX&page=', 32),
	'FTSE AIM UK 50': ('AIM5&page=', 3),
	'FTSE AIM 100': ('AIM1&page=', 6),
	'FTSE AIM ALL-SHARE': ('AXX&page=', 39),
}

