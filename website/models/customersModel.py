from .. import dataBase
from flask_login import UserMixin

class Customer(dataBase.Model, UserMixin):
    Customer_id = dataBase.Column(dataBase.Integer, primary_key = True, autoincrement=True)
    Customer_Fname = dataBase.Column(dataBase.String(100), nullable = False)
    Customer_Lname = dataBase.Column(dataBase.String(100), nullable = False)
    Customer_Email = dataBase.Column(dataBase.String(150), nullable = False, unique=True)
    Customer_Password = dataBase.Column(dataBase.String(255), nullable = False)
    Customer_Img = dataBase.Column(dataBase.String(255), default='default.png' )
    Customer_Address = dataBase.Column(dataBase.String(255), default = '')
    Customer_ZipCode = dataBase.Column(dataBase.String(255), default = '')
    Customer_Street = dataBase.Column(dataBase.String(255), default='')
    Customer_City = dataBase.Column(dataBase.String(255), default='')
    Customer_State = dataBase.Column(dataBase.String(255), default='')
    Customer_Phone = dataBase.Column(dataBase.Numeric(precision=10), default = 0)
    Customer_Status = dataBase.Column(dataBase.Integer, default=1)