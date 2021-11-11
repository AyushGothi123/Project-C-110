import statistics
import csv
import random
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("medium_data.csv")
data = df["claps"].tolist()
population_mean = statistics.mean(data)
print("Population mean is  ",population_mean)

def random_set_of_mean(counter):
  dataset = []
  for i in range(0,counter):
    random_index = random.randint(0,len(data))
    value = data[random_index]
    dataset.append(value)
  
  mean = statistics.mean(dataset)
  return mean

def show_fig(mean_list):
  df = mean_list
  mean = statistics.mean(df)
  fig = ff.create_distplot([df],["Claps"],show_hist = False)
  fig.add_trace(go.Scatter(x = [mean,mean],y = [0,1],mode = "lines"))
  fig.show()

def setup():
  mean_list = []
  for i in range(0,100):
    set_of_mean = random_set_of_mean(30)
    mean_list.append(set_of_mean)

  show_fig(mean_list)
  print("Mean of sample distribution",statistics.mean(mean_list))
  print("Stdev of sample distribution",statistics.stdev(mean_list))
  print("Stdev of normal distribution",statistics.stdev(data))


setup()