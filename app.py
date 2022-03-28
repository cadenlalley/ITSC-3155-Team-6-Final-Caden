from flask import Flask, abort, redirect, render_template, request, flash, url_for
from forms import SignupForm, LoginForm

app = Flask(__name__)

# protects against modifying cookies and crosssite request forgery attacks
app.config['SECRET_KEY'] = '3b05adb71fc2d58cb11457a257f37b35'

@app.get('/')
def index():
    return render_template('index.html')

@app.get('/faq')
def faq():
    return render_template('faq.html')

@app.route('/signup', methods=['GET','POST'])
def signup():
    form = SignupForm()
    # displays a message if data was sent
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('index'))
    return render_template('signup.html', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # test data 
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('index'))
        else: 
            flash('Login failed, please try again', 'danger')
    return render_template('login.html', form=form)
