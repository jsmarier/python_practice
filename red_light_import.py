import pandas as pd

test = pd.read_csv("https://opendata.arcgis.com/datasets/b053664e31a846078bea540c5224e34c_0.csv")
average = (test.mean()
           .reset_index()
           .iloc[5:16]
          )
average
