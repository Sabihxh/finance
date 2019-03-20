import os

import numpy as np
import pandas as pd


data_dir = './data_stocks'
stocks_csv_files = os.listdir(data_dir)

BARC = os.path.join(data_dir, 'BARC.L.csv')

df = pd.read_csv(BARC)

print(df.head())
