# import the Flask class from the flask module
from flask import Flask, render_template
import pandas as pd 
import os
import csv


# create the application object
app = Flask(__name__)

@app.route('/')
@app.route('/about')
def about():
    return render_template('home.html')  # render a template


@app.route('/Comparison')
def Comparison():
    return render_template('comparison.html') 



@app.route('/Data')
def Data(): 
    data = pd.read_csv('/Users/seve/Desktop/Web-Design-Challenge/Resources/cities.csv')
    table = data.to_html
    return render_template('Data.html',tables=table)


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
    TEMPLATES_AUTO_RELOAD = True
    app.secret_key = 'super_secret_key'
    