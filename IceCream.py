import plotly_express as px
import csv

with open("IceCream.csv") as csv_file:
    df=csv.DictReader(csv_file)
    fig=px.scatter(df, x="Temperature", y="Ice-cream Sales")
    fig.show()