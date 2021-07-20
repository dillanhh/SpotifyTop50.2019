import pandas as pd
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

Spotify_top50 = pd.read_csv("top50.csv")

plt.ylabel("Beats.Per.Minute")
plt.xlabel("Track.Name")

y=Spotify_top50['Beats.Per.Minute'].head(3 )
x=Spotify_top50['Track.Name'].head(3)
plt.bar(x,y)
plt.show()