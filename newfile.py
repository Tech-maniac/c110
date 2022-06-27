import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("data.csv")
data = df["temp"].tolist()

#print(data)

# fig = ff.create_distplot([data],["temp"],show_hist=False)
# fig.show()

population_mean = statistics.mean(data)
std_deviation = statistics.stdev(data)

print(" Population Mean : ", population_mean)
print(" Population std_deviation : ", std_deviation)

dataset = []
for i in range(0,1000):
    random_index = random.randint(0,len(data))
    value = data[random_index]
    dataset.append(value)

sample_mean = statistics.mean(dataset)
sample_std_deviation = statistics.stdev(dataset)

print(" Sample Mean : ", sample_mean)
print(" Sample std_deviation : ", sample_std_deviation)
