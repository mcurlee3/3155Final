from flask import Flask, render_template, request, redirect, url_for, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm, Form
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
import pandas as pd
from pandas import DataFrame
import plotly.offline as pyo
import plotly.graph_objs as go
import plotly.express as px
import plotly
import numpy as np
from PIL import Image 
import PIL 
import json

def Hyper(df_totals):
    df_hyper = df_totals['Country name']
    hyper_list = df_hyper.to_list()
    hyper=[]
    links =[]
    for i in hyper_list:
        s = 'https://en.wikipedia.org/wiki/'+i
        hyper.append(s)
    for i in range(10):
        links.append([hyper_list[i],hyper[i]])
    hyper_links = {hyper_list[i]: hyper[i] for i in range(len(hyper_list))}  
    print(hyper_links)
    return hyper_links
