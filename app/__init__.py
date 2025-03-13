from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#This method is automatically called
def create_app():
    app = Flask(__name__) #Initializes the app
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///quiz_master.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    
    return app