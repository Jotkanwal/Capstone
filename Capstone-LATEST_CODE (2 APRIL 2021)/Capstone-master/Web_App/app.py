from flask import Flask, render_template, flash, redirect, url_for, session, request, logging, Response
from flask_mysqldb import MySQL
from flask import Markup
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
import csv
import io
import random
import datetime
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import mpld3 as mpld

#articles=Database()

global temperature
temperature=0

app = Flask(__name__)

#Config flask_MYQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'test'
app.config['MYSQL_PASSWORD'] = 'asdf123'
app.config['MYSQL_DB'] = 'capstone'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

#init MYSQL
mysql = MySQL(app)

# Histogram Generation Functions
def GeneratePlot(numTimeIntervals) :
    data = GetTempHistData(numTimeIntervals)

    if data == -1:
        return "<div><span>Unable to Generate Histogram</span></div>"
    timeData=[]
    tempData=[]
    i=0

    for rowTuple in data:
        timeData.append(rowTuple['time'])
        tempData.append(rowTuple['temp'])
        i=i+1

    figure, graph=plt.subplots()
    graph.plot(timeData, tempData)
    graph.set(xlabel='Date (s)', ylabel='Temperature (C)', title='Temperature')
    graph.grid()

    htmlText = mpld.fig_to_html(figure)
    return htmlText

def GetTempHistData(numTimeIntervals) :
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("SELECT temperature AS temp, time FROM data")
        result = cur.fetchall()
        cur.close()
    return result


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

class RegisterForm(Form):
    name=StringField('Name', [validators.Length(min=1, max=50)])
    username=StringField('Username', [validators.Length(min=4, max=25)])
    password=PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message = 'Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')

class controlForm(Form):
    temp = StringField('Set Temperature: ')
    time = StringField('Time you want to hold this temperature: (in seconds)')

#registeration
@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = (form.password.data)

        #creating cursor here
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(username, password) VALUES(%s, %s)", (username, password))

        #commiting data to db
        mysql.connection.commit()
        cur.close()

        flash("SUCESS, you can log in now.")
        #return redirect(url_for('index'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        #get form fields
        username = request.form['username']
        password_candidate = request.form['password']

        #create DictCursor

        cur = mysql.connection.cursor()

        #get Username

        result = cur.execute("SELECT * FROM users WHERE username = %s", [username])

        if result >0:
            #get stored hash
            data = cur.fetchone()
            password = data['password']

            #compare Passwords

            if password_candidate==password:
                # if this is True
                #session comes from flask
                session['logged_in'] = True
                session['username'] = username

                flash("You are now logged in", 'SUCESS')
                return redirect(url_for("dashboard"))

            else:
                flash("Invalid Login")
                error = "Username not found"
                return render_template('login.html', error=error)
            cur.close()

        else:
            flash("Invalid Login")
            error = "Invalid Login"
            return render_template('login.html', error=error)


    return render_template('login.html')

#authentication for logged in users

def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if('logged_in' in session):
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, please login', 'danger')
            return redirect(url_for('login'))
    return wrap

@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash("You are now logged out","Sucess")
    return redirect(url_for('login'))


@app.route('/clearTable', methods=['GET', 'POST'])
@is_logged_in
def clearTable():
    if request.method == 'POST':

        cur=mysql.connection.cursor()
        cur.execute("truncate table data")
        mysql.connection.commit()
        cur.close()
        mostRecent=[]
        form = controlForm(request.form)

    return redirect(url_for('dashboard'))

    #return render_template('dashboard.html', mostRecent=mostRecent, form = form)


@app.route("/dashboard", methods=['GET', 'POST'])
@is_logged_in
def dashboard():
    histogramHtmlText = Markup(GeneratePlot("3"))

    form = controlForm(request.form)
    if request.method == 'POST' and form.validate():
        temp = form.temp.data
        time = form.time.data


        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO control(temp, time) VALUES(%s, %s)", (temp, time))

        mysql.connection.commit()
        cur.close()


        flash("Temperature set to "+str(temp)+" for "+str(time)+" seconds.")
        return redirect(url_for('dashboard'))

    cur = mysql.connection.cursor()

    cur.execute("SELECT * FROM data WHERE id IN (SELECT MAX(id) FROM data)")
    mostRecent = cur.fetchone()

    result = cur.execute("SELECT * FROM data")
    #print (result)
    articles = cur.fetchall()


    if result>0:
        return render_template('dashboard.html',articles=articles, form=form, mostRecent=mostRecent, histHtml=histogramHtmlText)
    else:
        mostRecent = {'id': 1, 'temperature': '_ ', 'humidity':'_ ' , 'time': datetime.datetime(2021, 4, 4, 13, 29, 14)}
        return render_template('dashboard.html',msg='No entries found', form=form, mostRecent=mostRecent)

    cur.close()

    return render_template('dashboard.html')

class ArticleForm(Form):
    title=StringField('Title', [validators.Length(min=1, max=50)])
    body=TextAreaField('Body', [validators.Length(min=1)])

@app.route('/download_csv', methods = ['GET', 'POST'])
def download():

    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM data")
    articles = cur.fetchall()
    print()

    print()


    File = open('DATA.csv', 'w+')
    Data = csv.writer(File)

    Data.writerow(('Temperature', 'Humidity', 'Time'))

    for article in articles:
        Data.writerow((article['temperature'], article['humidity'], article['time']))

    File.close()
    flash("Data saved to csv file")


    return redirect(url_for('dashboard'))


if __name__ == '__main__':
    app.secret_key='secret_109_'
    app.run(debug=True)
