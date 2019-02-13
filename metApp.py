# I give credit to the github/blogs at https://sarahleejane.github.io/learning/python/2015/08/09/simple-tables-in-webapps-using-flask-and-pandas-with-python.html and https://github.com/Layla-ElAsri/flask-app for giving me a starting point to develop this app.

from flask import Flask, render_template, request, redirect
import requests
import simplejson as json
import pandas as pd
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html, components

app = Flask(__name__)

@app.route('/')
def main():
    return redirect('/index')

@app.route('/index')
def index():
    return render_template('form.html', message = "")

@app.route('/getting_form', methods=['POST', 'GET'])
def geting_form():
    department = request.form['Department']
    start_year = int(request.form['Start_Year'])
    end_year = int(request.form['End_Year'])
    n_entries = request.form['Number_Entries']
    #return department, start_year, end_year, n_entries
    return get_form(department, start_year, end_year, n_entries)

@app.route('/get_form')
def get_form(department, start_year, end_year, n_entries):
   data=pd.read_csv('https://media.githubusercontent.com/media/metmuseum/openaccess/master/MetObjects.csv', low_memory=False)
   if end_year <= start_year:
       return render_template('form.html', message = "Please select an end year later than the start year.")
   df_show=data[(data['Object Begin Date']>=start_year) & (data['Object Begin Date']<=end_year)]
   if department == "All":
       pass
   else:
       df_show=data[(data['Department']==department)]
   
   if n_entries=='All':
       return render_template('view.html', tables = [df_show.to_html(classes='opt2')], titles=['Art Collection1'])  
   else:
       return render_template('view.html',tables=[df_show.head(int(float(n_entries))).to_html(classes='opt2')], titles=['Art Collection1'])  
   

if __name__ == '__main__':
	app.run(port=5000, debug=False)
