import pandas as pd
import plotly.express as px

df = pd.read_csv("Data 4.22.21.csv")
# print(df['latitude'].dtype)
# print(df['Happiness Value'].max())
# print(df['Happiness Value'].min())
fig = px.choropleth(df, locations='Country name',locationmode='country names', color='Happiness Value',
                    range_color=(2, 8))
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()


file = open('Happiness.html', 'w')
file.write(fig.to_html())
file.close()
