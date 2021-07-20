import pandas
from sklearn import linear_model
df = pandas.read_csv("top50.csv")
missing = df.isnull
print(missing)
df[['Energy', 'Popularity']] = df[['Energy', 'Popularity']].fillna(0)
print(df)