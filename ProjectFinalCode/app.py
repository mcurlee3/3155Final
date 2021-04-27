import os 
from flask import Flask, render_template, request, redirect, url_for, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm, Form
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from important import Important
from hyper import Hyper
import plotly
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
import numpy as np
import json
from multiline import ML
s = "nothing"


app = Flask(__name__)
app.config['SECRET_KEY'] = '3155Final'
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('/about.html')


@app.route('/products')
def data():
    return render_template('/products.html')


@app.route('/happyForm', methods=['POST', 'GET'])
def happyform():
    if request.method == 'POST':
        important = request.form.getlist('important')
        df_totals  = Important(important)
        link = Hyper(df_totals)
        df_totals = pd.read_csv('totals.csv', nrows = 10)
        fig = px.pie(df_totals, values='totals', names='Country name', title='Your Best Matches')
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return render_template('/totals.html', plot=graphJSON, links=link)
    return render_template('/HappyForm.html')


@app.route('/map')
def map():
    return render_template('/Happiness.html')
    
@app.route('/multiLine')
def multiLine():
    ##fig holds the plotly plot information. Used normally to display the plot.
    fig = ML()
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('/ml.html', plot = graphJSON)

if __name__ == "__main__":
    app.run(debug=True)

