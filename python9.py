import pandas as pd
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

Spotify_top50 = pd.read_csv("top50.csv")

plt.xlabel("Artist.Name")
plt.ylabel("Liveness")

x=Spotify_top50['Artist.Name'].head(10 )
y=Spotify_top50['Liveness'].head(10)
plt.bar(x,y)
plt.show()