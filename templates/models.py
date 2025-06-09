from flask_sqlalchemy import SQLAlchemy

# Instance de la base de données
# Elle sera initialisée par l'application Flask

db = SQLAlchemy()


class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(120), nullable=False)
    prenom = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    service = db.Column(db.String(255), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    heure = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Reservation {self.nom} {self.prenom} - {self.service}>"
