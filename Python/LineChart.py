import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('Data - General Data.csv')

# Preparing data
data = [go.Scatter(x=df['Country name'], y=df['Happiness Value'], mode='lines', name='Happiness Value')]

# Preparing layout
layout = go.Layout(title='Overall World Happiness', xaxis_title="Country",
                   yaxis_title="Happiness")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='linechart.html')