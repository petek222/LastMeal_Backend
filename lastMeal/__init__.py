import os

from flask import Flask
from lastMeal.models.user import User

from flask_jwt_extended import JWTManager


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    app.config["JWT_SECRET_KEY"] = "changemeplease"
    jwt = JWTManager(app)

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from lastMeal.api.v1 import auth
    app.register_blueprint(auth.bp)

    from lastMeal.api.v1 import pantry
    app.register_blueprint(pantry.bp)

    from lastMeal.api.v1 import photos
    app.register_blueprint(photos.bp)

    from lastMeal.api.v1 import exp
    app.register_blueprint(exp.bp)

    from lastMeal.api.v1 import recipe
    app.register_blueprint(recipe.bp)

    return app
