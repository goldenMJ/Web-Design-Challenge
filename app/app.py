# import the Flask class from the flask module
from flask import Flask, render_template
import pandas as pd 
import os
import csv


# create the application object
app = Flask(__name__)

@app.route('/')
def about():
    return render_template('home.html')  # render a template


@app.route('/Comparison')
def Comparison():
    return render_template('comparison.html') 

@app.route('/Max')
def Max():
    return render_template('Max.html') 

@app.route('/Hum')
def Hum():
    return render_template('humit.html') 

@app.route('/Cloud')
def Cloud():
    return render_template('Cloud.html') 

@app.route('/Wind')
def Wind():
    return render_template('wind.html') 

@app.route('/Data')
def Data(): 
    data = pd.read_csv('/Users/seve/Desktop/Web-Design-Challenge/Resources/cities.csv')
    table = data.to_html
    return render_template('Data.html',tables=table)

@app.route('/action')
def action(): 
    return render_template('Data.html')


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
    TEMPLATES_AUTO_RELOAD = True
    app.secret_key = 'super_secret_key'
    