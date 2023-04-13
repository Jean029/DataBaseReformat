from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path

dataBase = SQLAlchemy()
DB_NAME = 'NebulaDataBase.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    
    dataBase.init_app(app)
    
    from .views import views
    from .auth import auth
    from .models.usermodel import User
   

    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    create_database(app)
    
    login_manager = LoginManager()
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(Customer_id):
        return User.query.get(int(Customer_id))
    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            dataBase.create_all()
        print('Created Database')