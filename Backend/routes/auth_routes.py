from flask import Blueprint, request, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token
from models import db, User

auth_bp = Blueprint("auth", __name__)
bcrypt = Bcrypt()


# ---------- REGISTER ----------
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    if not data:
        return jsonify({"msg": "Missing JSON data"}), 400

    required_fields = ["full_name", "email", "password"]
    for field in required_fields:
        if field not in data:
            return jsonify({"msg": f"Missing field: {field}"}), 400

    if User.query.filter_by(email=data.get("email")).first():
        return jsonify({"msg": "Email already registered"}), 409

    hashed_pw = bcrypt.generate_password_hash(data["password"]).decode("utf-8")

    new_user = User(
        full_name=data.get("full_name"),
        email=data.get("email"),
        password=hashed_pw,
        profile_picture=data.get("profile_picture"),
        university=data.get("university"),
        course=data.get("course"),
        year_of_study=data.get("year_of_study"),
        student_id=data.get("student_id"),
        career_interests=data.get("career_interests"),
        linkedin_profile=data.get("linkedin_profile"),
        skills=data.get("skills"),
        phone_number=data.get("phone_number"),
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "User registered!"}), 201


# ---------- LOGIN ----------
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data:
        return jsonify({"msg": "Missing JSON data"}), 400

    user = User.query.filter_by(email=data.get("email")).first()
    if user and bcrypt.check_password_hash(user.password, data.get("password")):
        token = create_access_token(identity=user.id)
        return jsonify({"token": token, "msg": "Login successful"})

    return jsonify({"msg": "Invalid credentials"}), 401
