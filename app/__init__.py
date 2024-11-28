from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Register routes
    from .routes import webhook
    app.register_blueprint(webhook)

    return app
