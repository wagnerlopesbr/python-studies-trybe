from flask import Flask
from controllers.jokes_controller import jokes_controller
from os import environ
from waitress import serve


app = Flask(__name__)
app.register_blueprint(jokes_controller, url_prefix="/jokes")


def start_server(host: str = "0.0.0.0", port: int = 8000):  # debug=True enables auto-reloading
    if environ.get("FLASK_ENV") == "dev":  # Use Flask's built-in server if in development
        app.run(debug=True, host=host, port=port)
    else:
        serve(app, host=host, port=port)  # Use Waitress server in production


if __name__ == "__main__":
    start_server()
