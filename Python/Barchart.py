import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
import matplotlib.pyplot as plt

# Load CSV file from Datasets folder
df = pd.read_csv('/UNCC/Spring2021/ITSC-3155/Final/3155Final/Python/cFreedom.csv', nrows=10)

# Preparing data
data = [go.Bar(x=df['Country name'], y=df['Freedom to make life choices'])]

# Preparing layout
layout = go.Layout(title='Freedom to Make Life Choices', xaxis_title="Country",
                   yaxis_title="Perception of Freedom")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='barchart.html')
fig.write_image("barChart.jpeg")