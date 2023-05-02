from flask import Flask
from . import routes_and_views


def create_app() -> Flask:
    app = Flask(__name__)

    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000, debug=True)

    routes_and_views.init_app(app)

    return app
