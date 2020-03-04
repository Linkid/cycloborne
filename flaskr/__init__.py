import os

from flask import Flask
from flask import request
from flask import current_app
from flask_babel import Babel
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


babel = Babel()
bootstrap = Bootstrap()
db = SQLAlchemy()
migrate = Migrate()


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        #DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
        SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(app.instance_path, 'flaskr.sqlite'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    # config
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('../config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_object(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #
    # db
    #
    db.init_app(app)
    migrate.init_app(app, db)
    #app.app_context().push()

    #
    # Borne blueprint
    #
    from . import borne
    app.register_blueprint(borne.bp)
    #app.add_url_rule('/', endpoint='index')

    # bootstrap
    bootstrap.init_app(app)
    # i18n
    babel.init_app(app)

    return app


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(current_app.config['LANGUAGES'])


from flaskr import models
