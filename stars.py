import pandas as pd
import csv

df = pd.read_csv("final.csv")

del df["luminosity"]
del df["Nun"]

            }, axis='columns')

df.to_csv('main.csv') 