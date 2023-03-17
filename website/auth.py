from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__, template_folder='templates/client/')

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/change-password')
def changePassword():
    return render_template('change_passLogin.html')

@auth.route('/register')
def register():
    return render_template('register.html')