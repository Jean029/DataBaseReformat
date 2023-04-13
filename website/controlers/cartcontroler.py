from ..models.usermodel import Cart
from .. import dataBase
from flask_login import current_user
from sqlalchemy import text
import json

def CreateCart():    
    cart = Cart(total = 0, user_id = current_user.id)
    dataBase.session.add(cart)
    dataBase.session.commit()

def getCart():
    cart = dataBase.session.execute(text(f"SELECT * FROM Cart WHERE user_id == {current_user.id}")).fetchone()
    return cart