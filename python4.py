import pandas as pd

import numpy as np


Spotify_top50 = pd.read_csv("top50.csv")
pd.options.display.max_columns = None
pd.options.display.max_rows = None
pd.set_option('display.max_colwidth', None)

#Count the missing data
missing_values_count = Spotify_top50.isnull().sum()
#Print columns missing data from 0 to 12.
print(missing_values_count[0:50])
droprows= Spotify_top50.dropna()
print(Spotify_top50.shape,droprows.shape)
dropcolumns = Spotify_top50.dropna(axis=1)
print(Spotify_top50.shape,dropcolumns.shape)
cleaned_data = Spotify_top50.fillna(0)
cleaned_data = Spotify_top50.fillna(method='bfill', axis=0).fillna(0)
drop_duplicates= Spotify_top50.drop_duplicates()
print(Spotify_top50.shape,drop_duplicates.shape)

# finding total number of null values
print(Spotify_top50 .isnull().sum())
