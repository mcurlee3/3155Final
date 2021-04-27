from flask import Flask, render_template, request, redirect, url_for, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm, Form
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
import plotly.express as px
import plotly
import numpy as np
from PIL import Image 
import PIL 
import json
def Important(important):
    df_main = pd.read_csv("Data - General Data.csv", delimiter=",")
    df_main = df_main.sort_values('Country name')
    sumColumns = 1
    if "happiness" in important:
        sumColumns += df_main['Happiness Value']
    if "gdp" in important:
        sumColumns += df_main['Logged GDP per capita']
    if "socialSupport" in important:
        sumColumns += df_main['Social support']
    if "lifeExpectancy" in important:
        sumColumns += df_main['Healthy life expectancy']
    if "freedom" in important:
        sumColumns += df_main['Freedom to make life choices']
    if "generosity" in important:
        sumColumns += df_main['Generosity']
    if "corruption" in important:
        sumColumns -= df_main['Perceptions of corruption']
    df_main['totals'] = sumColumns
    df_main = df_main.sort_values('totals', ascending=False)
    file = open('totals.csv', 'w')
    file.write(df_main.to_csv())
    file.close()

    df_totals = pd.read_csv('totals.csv', nrows = 10)
    fig = px.pie(df_totals, values='totals', names='Country name', title='Your Best Matches')
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return df_totals