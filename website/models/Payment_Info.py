from .. import dataBase
from sqlalchemy.sql import func


    
class payment(dataBase.Model):
    User_Id = dataBase.Column(dataBase.Integer, primary_key=True)
    Card_Name = dataBase.Column(dataBase.String(20), nullable=False)
    Card_Type = dataBase.Column(dataBase.String(20), nullable=False)
    Card_Number = dataBase.Column(dataBase.Integer, nullable=False)
    Card_Month = dataBase.Column(dataBase.Integer, nullable=False)
    Card_Year = dataBase.Column(dataBase.Integer, nullable=False)





    
