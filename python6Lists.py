import pandas as pd



import numpy as np

Spotify_top50 = pd.read_csv("top50.csv")
thislist = ["Track.Name", "Artist.Name", "Genre"]
print(len(thislist))

print(thislist[0])

print(thislist[-1])