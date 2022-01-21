import csv
import numpy as np

def getDataSource(data_path):
    sizeOfTV=[]
    averageTimeSpent=[]
    with open(data_path) as csv_file:
        csvReader = csv.DictReader(csv_file)
        for row in csvReader:
            sizeOfTV.append(float(row["Size of TV"]))
            averageTimeSpent.append(float(row["\tAverage time spent watching TV in a week (hours)"]))
    return {"x": sizeOfTV, "y": averageTimeSpent}

def findCorrelation(data_source):
    correlation=np.corrcoef(data_source["x"], data_source["y"])
    print("Correlation: ", correlation[0, 1])

def setUp():
    data_path="TV.csv"
    data_source=getDataSource(data_path)
    findCorrelation(data_source)

setUp()