import pandas as pd
import plotly.express as px


def choropleth():
    df = pd.read_csv("Choropleth.csv")
    fig = px.choropleth(df, locations='Country name', locationmode='country names', color='Happiness Value',
                        range_color=(2, 8))
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return fig

