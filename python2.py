import pandas as pd

import numpy as np

Spotify_top50 = pd.read_csv("top50.csv", index_col = 0)
pd.options.display.max_columns = None
pd.options.display.max_rows = None
pd.set_option('display.max_colwidth', None)

print(Spotify_top50)


print(Spotify_top50.head())


print(Spotify_top50.shape)


print(Spotify_top50.columns)