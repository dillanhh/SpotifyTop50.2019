import pandas as pd

import numpy as np

file_location="./top50.csv"


pd.options.display.max_columns = None
pd.options.display.max_rows = None
pd.set_option('display.max_colwidth', None)

df = pd.read_csv(file_location)
print (df)