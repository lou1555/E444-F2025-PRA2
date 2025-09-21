from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config["YOUR_NAME"] = "Louis"  # <- change your name here

    from .routes import bp
    app.register_blueprint(bp)
    return app
