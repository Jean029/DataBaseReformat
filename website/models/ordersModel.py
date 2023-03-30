from .. import dataBase
from sqlalchemy.sql import func
from datetime import datetime


class Order(dataBase.Model):
    __tablename__ = 'orders'
    order_id = dataBase.Column(dataBase.Integer, primary_key=True, autoincrement=True)
    tracking_num = dataBase.Column(dataBase.Integer, primary_key=False, autoincrement=True)
    order_date = dataBase.Column(dataBase.DateTime(timezone=True), default=func.now(), nullable=False)
    arrival_date = dataBase.Column(dataBase.DateTime(timezone=True), default=func.now(), nullable=False)
    address_line_1 = dataBase.Column(dataBase.String(150), nullable=True)
    address_line_2 = dataBase.Column(dataBase.String(150), nullable=True)
    total = dataBase.Column(dataBase.Integer, nullable=False)
    amount = dataBase.Column(dataBase.Integer, nullable=False)
    payment_method = dataBase.Column(dataBase.String(150), nullable=False)
    status = dataBase.Column(dataBase.String(150), nullable=False, default='Pending')
    order_prods = dataBase.Column(dataBase.Integer, nullable=False)


class Transaction(dataBase.Model):
    __tablename__ = 'transactions'
    id = dataBase.Column(dataBase.Integer, primary_key=True)
    order_id = dataBase.Column(dataBase.Integer, dataBase.ForeignKey('orders.id'))
    amount = dataBase.Column(dataBase.Float)
    date = dataBase.Column(dataBase.DateTime, default=datetime.utcnow)
    quantity = dataBase.Column(dataBase.Integer,nullable=False)
    