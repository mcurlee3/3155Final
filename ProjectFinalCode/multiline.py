import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

def ML():

    # Load CSV file from Datasets folder
    df = pd.read_csv('/UNCC/Spring2021/ITSC-3155/Final/3155Final/Python/cHappiness.csv', nrows=25)
    # Preparing data
    trace1 = go.Scatter(x=df['Country name'], y=df['Happiness/GDP'], mode='lines', name='Happiness/GDP')
    trace2 = go.Scatter(x=df['Country name'], y=df['Happiness/Life Expetancy'], mode='lines', name='Happiness/Life Expetancy')
    trace3 = go.Scatter(x=df['Country name'], y=df['Happiness/Social Support'], mode='lines', name='Happiness/Social Support')
    trace4 = go.Scatter(x=df['Country name'], y=df['Happiness/Freedom'], mode='lines', name='Happiness/Freedom')
    trace5 = go.Scatter(x=df['Country name'], y=df['Happiness/Generosity'], mode='lines', name='Happiness/Generosity')
    trace6 = go.Scatter(x=df['Country name'], y=df['Happiness/Corruption'], mode='lines', name='Happiness/Corruption')

    data = [trace1,trace2,trace3,trace4,trace5,trace6]


    # Preparing layout
    layout = go.Layout(title='Compare Factors of the Top 25 Happiest Countries', xaxis_title="Country Name",
                    yaxis_title="Score")

    # Plot the figure and saving in a html file
    fig = go.Figure(data=data, layout=layout)
    ##pyo.plot(fig, filename='multilinechart.html')

    return fig