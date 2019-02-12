from flask import Flask
import os
from .api import bp as api_bp

def create_app(test_config=None):
    app = Flask(__name__,instance_relative_config=True)

    #注册模块
    app.register_blueprint(api_bp)

    app.config.from_mapping(SECRET_KEY='dev')

    if test_config is None:
        app.config.from_pyfile('config.py',silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    return app