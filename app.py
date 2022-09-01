from flask import Flask, render_template, redirect, url_for, request
from flask_mysqldb import MySQL


app = Flask(__name__)



@app.route('/')
def home():
    return"Hello Admin!"


@app.route('/adlogin', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['ausername'] == 'lanson ' or request.form['apassword'] == 'Lanson10':
            return redirect(url_for('addstyle'))
        else:
            error = 'Invalid Credentials. Please try again.'
    return render_template('adlogin.html', error=error)



if __name__ =='__main__':
    app.debug = True
    app.run()