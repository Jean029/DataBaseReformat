from flask import Blueprint, render_template, request, flash

views = Blueprint('views', __name__, template_folder='templates/client/')

@views.route('/')
@views.route('/shop', methods = ['GET', 'POST'])
def shop():
    return render_template('shop.html')

@views.route('/profile')
def profile():
    return render_template('profile.html')

@views.route('/orders')
def orders():
    return render_template('orders.html')

@views.route('/checkout')
def checkout():
    return render_template('checkout.html')