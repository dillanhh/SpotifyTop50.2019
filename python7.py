import pandas as pd
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

Spotify_top50 = pd.read_csv("top50.csv")

plt.xlabel("Track.Name")
plt.ylabel("Danceability")

x=Spotify_top50['Track.Name'].head(4 )
y=Spotify_top50['Danceability'].head(4)
plt.plot(x,y)
plt.show()