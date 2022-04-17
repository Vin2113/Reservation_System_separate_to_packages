from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from Forms import RegistrationForm, LoginForm
from flask_mysqldb import MySQL   #package to connect database with
import pymysql
app = Flask(__name__)
app.config['SECRET_KEY'] = '611d9950d57b916a8a8e4b620b1ef04c'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Vl1021996499.'
app.config['MYSQL_DB'] = 'reservation system'

mysql = MySQL(app)


@app.route('/')

@app.route('/home')
def home():
    return render_template('Layout.html', title='Home')

@app.route('/register', methods=["GET", 'POST'])

def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        # cursor.execute(f'''Insert INTO customer VALUES({form.email.data, form.}''')
        return redirect(url_for('home'))
    return render_template('Register.html', title='Register', form=form)


@app.route('/login',methods=["GET", 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # if for
        flash('You have been logged in!', 'success')
    else:
        flash('Login Unsuccesful', 'danger')
    return render_template('Login.html', title='Login', form=form)

# @app.route('/login_booking_agent',methods=["GET", 'POST'])
# @app.route('/login_staff',methods=["GET", 'POST'])




if __name__ == '__main__':
    app.run(debug=True)
