from flask_sqlalchemy import SQLAlchemy

# Initialisation du moteur SQLAlchemy
db = SQLAlchemy()

# Modèle de table Reservation
class Reservation(db.Model):
    __tablename__ = 'reservations'

    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    prenom = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    service = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    heure = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"<Reservation {self.nom} {self.date} {self.heure}>"
