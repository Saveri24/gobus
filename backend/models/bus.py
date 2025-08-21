from backend.extensions import db

class Bus(db.Model):
    __tablename__ = 'buses'

    id = db.Column(db.Integer, primary_key=True)
    bus_name = db.Column(db.String(100), nullable=False)
    total_seats = db.Column(db.Integer, nullable=False)
