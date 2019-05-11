import os

import pandas as pd

def find_empty_csv_files():
	"""
	Loops through all csv files in data_stocks directory and
	returns all csv files that are empty.
	"""
	empty_files = []
	dirs = ['FTSE100', 'FTSE250']
	for _dir in dirs:
		for csv in os.listdir('../data_stocks/{}'.format(_dir)):
			fp = os.path.join('../data_stocks', _dir, csv)
			rows = pd.read_csv(fp).shape[0]
			if rows == 0:
				empty_files.append(csv)
	return empty_files


find_empty_csv_files()