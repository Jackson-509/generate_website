# -*- coding: utf-8 -*-
"""Fonctions utilitaires pour la génération de sites."""

import csv
from flask_mail import Mail, Message

mail = Mail()


def enregistrer_csv(row, fichier="instance/reservations.csv"):
    """Enregistre une ligne dans un fichier CSV."""
    with open(fichier, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(row)


def init_mail(app):
    """Initialise l'extension Flask-Mail avec l'application donnée."""
    mail.init_app(app)


def envoyer_mail(prenom, dest, service, date, heure):
    """Envoie un e-mail de confirmation simple."""
    msg = Message(
        subject=f"Confirmation de rendez-vous pour {service}",
        recipients=[dest],
        body=(
            f"Bonjour {prenom},\n\n"
            f"Votre demande de rendez-vous pour '{service}' le {date} à {heure} "
            "a bien été reçue.\n"
        ),
    )
    mail.send(msg)
