from ..models.ordersModel import Orders
from .. import dataBase
from sqlalchemy import text

def getAllOrders():
    return dataBase.session.execute(text('SELECT * FROM Orders'))

def getorderid():
    return dataBase.session.execute(text('SELECT DISTINCT order_id FROM Orders'))

# SQL para cambiar el total de la orden usando el id de la orden
def uptd_ordert():
    return dataBase.session.execute(text('UPDATE Orders SET c_total = total_c WHERE id = order_id'))
                                         
# Escoger una orden especifico de un usuario
def sel_user_Ord():
    return dataBase.session.execute(text('SELECT * FROM Orders where user_id = user_id')) #Añadir el user que se quieren ver las ordenes

# Escoger Ordenes dentro un rango de tiempo
def esp_range_orders():
    return dataBase.session.execute(text('SELECT * FROM Orders WHERE order_date BETWEEN date1 AND date2')) 
# Anadir los ranges a los cuales se les quiere buscar tales ordenes

def get_trackingnum():
    return dataBase.session.execute(text('SELECT DISTINCT tracking_num FROM Orders')) 

def testdata():
    new_Order = Orders(         order_id = '1234',
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
    print(new_Order)
    dataBase.session.commit()





