<<<<<<< Updated upstream
from flask import Blueprint, render_template, request, flash
=======
from flask import Blueprint, redirect, render_template, request, flash, url_for
from .controlers.usercontroler import *
from .controlers.cartcontroler import *
from .controlers.paymentController import *
from werkzeug.security import check_password_hash
from flask_login import login_required, logout_user
>>>>>>> Stashed changes

auth = Blueprint('auth', __name__, template_folder='templates/client/')

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/change-password')
def changePassword():
    return render_template('change_passLogin.html')

@auth.route('/register')
def register():
<<<<<<< Updated upstream
    return render_template('register.html')
=======
    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        pass1 = request.form.get('pass1')
        pass2 = request.form.get('pass2')

        customer = checkForCustomer(email)
        if 1 in customer:
            flash('Email already exist.', category='error')
        elif len(email) < 4:
            flash('Email must be graater than 3 characters.', category='error')
        elif len(fname) < 2:
            flash('fname must be graater than 1 characters.', category='error')
        elif pass1 != pass2:
            flash('passwords don\'t match.', category='error')
        elif len(pass1) < 5:
            flash('password is to short.', category='error')
        else:
            CreateAccount(fname, lname, email, pass1)
            CreateCart()
            CreateCard()
            
            flash('Account created', category='success')
            return redirect(url_for('views.shop'))
    return render_template('register.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
>>>>>>> Stashed changes
