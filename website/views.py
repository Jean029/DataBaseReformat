from flask import Blueprint, render_template
from flask_login import current_user, login_required
from .controlers.usercontroler import *
from .controlers.productsControler import *
from .controlers.ordersControler import *
from .controlers.cartcontroler import *

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
    cart = None
    cart_items = None
    total_items = None
    
    if current_user.is_authenticated:
        cart = getCart()
        cart_items = json.dumps(cart.items)
        if cart_items == "NULL":
            cart_items = []
        total_items = len(cart_items)
    
    return render_template('shop.html', user = current_user, 
                           telescopes = telescopes,
                           brands = brands,
                           Lens = lens,
                           amount = amount,
                           focal_distance = focal_distance,
                           aperture = aperture,
                           mount = mount,
                           cart = cart,
                           items = cart_items,
                           total_items = total_items)

@views.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user = current_user)

@views.route('/orders', methods = ['GET', 'POST'])
@login_required
def orders():
    return render_template('orders.html', user = current_user)
     

@views.route('/checkout')
@login_required
def checkout():
    return render_template('checkout.html', user = current_user)