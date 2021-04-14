import plotly.express as px
import pandas as pd
import plotly.graph_objs as go
df = pd.DataFrame(dict(
    r=[1, 5, 2, 2, 3],
    theta=['processing cost','mechanical properties','chemical stability',
           'thermal stability', 'device integration']))

fig = go.line_polar(df, r='r', theta='theta', line_close=True)
px.plot(fig, filename='radarchart.html')