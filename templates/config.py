# Configuration par défaut du site

SECRET_KEY = "change-this-secret-key"
SQLALCHEMY_DATABASE_URI = "sqlite:///instance/site.db"
ADMIN_USERNAME = "admin"
# Mot de passe haché par werkzeug.security.generate_password_hash("password")
ADMIN_PASSWORD_HASH = "pbkdf2:sha256:260000$changeme$1234567890abcdef"

# Configuration Flask-Mail (serveur local par défaut)
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_DEFAULT_SENDER = 'noreply@example.com'
