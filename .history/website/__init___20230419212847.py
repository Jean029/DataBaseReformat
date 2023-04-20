from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

dataBase = SQLAlchemy()
DB_NAME = 'NebulaDataBase.db'


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secretkey'
<<<<<<< Updated upstream
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    
=======
    # app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://sql9607914:uWzaFxXgrH@sql9.freemysqlhosting.net:3306/sql9607914"

>>>>>>> Stashed changes
    dataBase.init_app(app)

    from .views import views
    from .auth import auth
<<<<<<< Updated upstream
    
=======
    from .models.usermodel import User

>>>>>>> Stashed changes
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    create_database(app)
<<<<<<< Updated upstream
=======

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(Customer_id):
        return User.query.get(int(Customer_id))
>>>>>>> Stashed changes
    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            dataBase.create_all()
        print('Created Database')
