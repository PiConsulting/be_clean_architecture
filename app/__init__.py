from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Import and register blueprints
    from app.api.routers import auth, client, example, external_services
    app.register_blueprint(auth.bp)
    app.register_blueprint(client.bp)
    app.register_blueprint(example.bp)
    app.register_blueprint(external_services.bp)

    return app
