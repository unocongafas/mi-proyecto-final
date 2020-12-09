from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __str__(self):
        return '<User {} {}>'.format(self.first_name, self.email)

    def serialize(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "email": self.email,
            # do not serialize the password, its a security breach
        }