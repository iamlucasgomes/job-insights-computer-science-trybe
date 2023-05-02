from flask import Flask
from . import routes_and_views


def create_app() -> Flask:
    app = Flask(__name__)
    routes_and_views.init_app(app)

    if __name__ == "__main__":
        app.run(host="0.0.0.0")

    return app
