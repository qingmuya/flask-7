from flask import Flask,render_template,Blueprint
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config
from . import views,errors,main

main = Blueprint('main',__name__)

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    @main.app_errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'),404
    
    @main.app.errorhandler(500)
    def internal_server_error(e):
        return render_template('500.html'),500

    return app