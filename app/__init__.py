from flask import Flask
from app.routes.predict_routes import predict_bp
from app.routes.web_routes import web_bp
from app.routes.feedback_routes import feedback_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(predict_bp)
    app.register_blueprint(web_bp)
    app.register_blueprint(feedback_bp)
    return app

