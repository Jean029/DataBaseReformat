from flask import Blueprint, render_template, request, flash
from .controlers.productsControler import *

views = Blueprint('views', __name__, template_folder='templates/client/')

@views.route('/')
@views.route('/shop', methods = ['GET', 'POST'])
def shop():
    telescopes = getAllTelescopes()
    brands = getAllBrands()
    lens = getAllLensType()
    focal_distance = [1,2]
    aperture = [1,2]
    mount = ['a', 'b']
    amount = 1
    total = 1
    
    return render_template('shop.html', 
                           telescopes = telescopes,
                           brands = brands,
                           Lens = lens,
                           amount = amount,
                           total = total,
                           focal_distance = focal_distance,
                           aperture = aperture,
                           mount = mount)

@views.route('/profile')
def profile():
    return render_template('profile.html')

@views.route('/orders')
def orders():
    return render_template('orders.html')

@views.route('/checkout')
def checkout():
    return render_template('checkout.html')