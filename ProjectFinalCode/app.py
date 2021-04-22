import os 
from flask import Flask, render_template, request, redirect, url_for, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm, Form
from wtforms import StringField, PasswordField, SubmitField, TextAreaField

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
        print()
        return(str(important))
    return render_template('/HappyForm.html')


@app.route('/multiLine')
def multiLine():
    return render_template('/multilinechart2.html')

if __name__ == "__main__":
    app.run(debug=True)

