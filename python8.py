import pandas as pd
import numpy as np

from matplotlib import pyplot as plt

Spotify_top50 = pd.read_csv("top50.csv")

def Energy_rating_per_Genre(list, title):

    list.sort_values(by="Energy",ascending=False).set_index("Genre").head(10).plot.bar(figsize=(9,6))
    plt.yticks(rotation=75, fontsize=7)
    plt.xticks(rotation=75, fontsize=7)
    plt.title(title, fontsize=6)
    plt.legend(handlelength=7, fontsize  = 8)
    plt.show()

list = Spotify_top50[["Energy","Genre"]].sort_values(by="Energy",ascending=True).drop_duplicates("Genre",keep="last")
title = "\nEnergy rating per Genre\n"
Energy_rating_per_Genre(list, title)