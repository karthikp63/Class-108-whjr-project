import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd
import csv

df = pd.read_csv("data2.csv")

fig = ff.create_distplot([df["Average Rating"].toList()], ["Avg Rating"], show_hist = false)