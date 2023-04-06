from .. import dataBase
from sqlalchemy import text
from flask_login import login_user
from ..models.usermodel import User

def checkForCustomer(email):
    user = dataBase.session.execute(text(f'SELECT IIF(EXISTS (SELECT Email FROM user WHERE Email = "{email}"), TRUE, FALSE)'))
    user = user.fetchone()
    print(user)
    return user

def getUser(email):
    user = dataBase.session.execute(text(f'SELECT * FROM User WHERE Email = "{email}" LIMIT 1'))
    return user.fetchone()

def setLoginUser(user):
    login_user(User.query.filter_by(id = user.id).first())