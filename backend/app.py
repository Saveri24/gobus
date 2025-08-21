import os
from flask import Flask
from backend.extensions import db
from flask_cors import CORS


def create_app():
    app = Flask(__name__)

    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'gobus.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    CORS(app)

    # Import and register blueprints here to avoid circular imports
    from backend.routes.bus_routes import bus_bp
    from backend.routes.schedule_routes import schedule_bp
    app.register_blueprint(bus_bp)
    app.register_blueprint(schedule_bp)

    @app.route("/")
    def home():
        return "GoBus Backend is running"

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
