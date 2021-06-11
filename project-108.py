  
import plotly.figure_factory as ff
import pandas as pd
import csv

df = pd.read_csv("project-108.csv")
fig = ff.create_distplot([df["Avg Rating"].tolist()], ["Avg Rating"])
fig.show()