from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    profile_picture = db.Column(db.String(200))  # store filename
    university = db.Column(db.String(100))
    course = db.Column(db.String(100))
    year_of_study = db.Column(db.String(50))
    student_id = db.Column(db.String(50))
    career_interests = db.Column(db.String(200))
    linkedin_profile = db.Column(db.String(200))
    skills = db.Column(db.String(200))
    phone_number = db.Column(db.String(20))
