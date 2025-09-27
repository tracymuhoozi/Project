from flask import Flask
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from models import db
from routes.auth_routes import auth_bp

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["JWT_SECRET_KEY"] = "super-secret"
app.config["UPLOAD_FOLDER"] = "uploads"

db.init_app(app)
jwt = JWTManager(app)
CORS(app)

# Register routes
app.register_blueprint(auth_bp, url_prefix="/auth")

# Initialize bcrypt for app context if needed (optional)
bcrypt = Bcrypt(app)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
