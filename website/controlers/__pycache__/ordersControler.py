
from .. import dataBase
from ...models import User,Transaction,Order,productsModel
from sqlalchemy import text

def getAllOrders():
    return dataBase.session.execute(text('SELECT * FROM Order'))

def getorderid():
    return dataBase.session.execute(text('SELECT * FROM Order WHERE id = order_id'))

def TestData():
    new_Order = Order(       order_id = '1234',
                               tracking_num = '12121212',
                               order_date = '2022-12-27',
                               arrival_date = '2022-15-27',
                               address_line_1 = 'barceloneta Puerto Rico ',
                               address_line_2 = 'barceloneta Puerto Rico',
                               total = 400,
                               amount = '400',
                               payment_method = 'Visa',
                               status = 'Pending',
                               order_prods = 1)
    dataBase.session.add(new_Order)
    dataBase.session.commit()