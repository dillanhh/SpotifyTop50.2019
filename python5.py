import pandas as pd

import numpy as np

Spotify_top50 = pd.read_csv("top50.csv")
pd.options.display.max_columns = None
pd.options.display.max_rows = None
pd.set_option('display.max_colwidth', None)


high_energy=Spotify_top50[Spotify_top50["Energy"]>80]
print(high_energy)