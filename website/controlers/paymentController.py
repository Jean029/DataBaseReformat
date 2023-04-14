from ..models.ordersModel import payment
from .. import dataBase
from sqlalchemy import text

def getPaymentInfo():
    return dataBase.session.execute(text('SELECT * FROM payment'))