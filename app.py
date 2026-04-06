from flask import Flask
from db import db
from config.config import SECRET_KEY, DATABASE
from flask_login import LoginManager
from controllers.homeController import HomeController
from controllers.cadastroController import CadastroController
from controllers.loginController import LoginController
from controllers.principalController import PrincipalController


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
    app.config['SQLALCHEMY_TRACE_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_POOL_RECYCLE'] = 300
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {"pool_pre_ping": True}
    app.secret_key = SECRET_KEY

    db.init_app(app)
    login_manager = LoginManager()
    login_manager.init_app(app)

    controllers = [
        HomeController(),
        LoginController(login_manager),
        CadastroController(),
        PrincipalController()
    ]

    for controller in controllers:
        app.register_blueprint(
            controller.blueprint,
            url_prefix=f"/{controller.blueprint.name}"
        )

    return app