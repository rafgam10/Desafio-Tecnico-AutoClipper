from flask import Flask
from .settings.config import Config
from .settings.extensions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    try:
        from .routes import register_routes
        register_routes(app)
        
        
        from src.routes.youtube_routes import youtube_bp
        app.register_blueprint(youtube_bp)
        
    except Exception:
        pass

    return app
