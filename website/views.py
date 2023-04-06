from flask import Blueprint, render_template, request, flash
from flask_login import current_user, login_required
from .controlers.usercontroler import *
from .controlers.productsControler import *
from .controlers.ordersControler import *

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
    
    return render_template('shop.html', user = current_user, 
                           telescopes = telescopes,
                           brands = brands,
                           Lens = lens,
                           amount = amount,
                           total = total,
                           focal_distance = focal_distance,
                           aperture = aperture,
                           mount = mount)

@views.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user = current_user)

@views.route('/orders', methods = ['GET', 'POST'])
@login_required
def orders():

    orders = getAllOrders()

    order_id = getorderid()

    tracking_num = get_trackingnum()

    total = 1

    return render_template('orders.html', user = current_user)
     

@views.route('/checkout')
@login_required
def checkout():
    return render_template('checkout.html', user = current_user)