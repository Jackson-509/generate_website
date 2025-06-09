import os
from pathlib import Path

def create_project(nom_site, slug, couleur="#00838f"):
    base = Path(slug)
    folders = [
        base / "templates",
        base / "static" / "css",
        base / "static" / "img",
        base / "instance"
    ]

    for folder in folders:
        folder.mkdir(parents=True, exist_ok=True)

    # app.py
    (base / "app.py").write_text(f"""from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html', nom_site="{nom_site}")

@app.route('/cgu')
def cgu():
    return render_template('cgu.html', nom_site="{nom_site}")

@app.route('/mentions-legales')
def mentions_legales():
    return render_template('mentions-legales.html', nom_site="{nom_site}")

@app.route('/politique-confidentialite')
def politique_confidentialite():
    return render_template('politique-confidentialite.html', nom_site="{nom_site}")

@app.route('/parametres-cookies')
def parametres_cookies():
    return render_template('parametres-cookies.html', nom_site="{nom_site}")

if __name__ == '__main__':
    app.run(debug=True)
""")

    # index.html
    (base / "templates" / "index.html").write_text(f"""<!DOCTYPE html>
<html>
<head>
    <title>{nom_site}</title>
    <link rel="stylesheet" href="{{{{ url_for('static', filename='css/style.css') }}}}">
</head>
<body>
    <header>
        <img src="{{{{ url_for('static', filename='img/logo.png') }}}}" alt="Logo" height="60">
        <h1>Bienvenue sur {nom_site}</h1>
    </header>
    <section>
        <img src="{{{{ url_for('static', filename='img/banner.jpg') }}}}" alt="Bannière" width="100%">
        <p>Nos services :</p>
        <div>
            <img src="{{{{ url_for('static', filename='img/service1.jpg') }}}}" width="150">
            <img src="{{{{ url_for('static', filename='img/service2.jpg') }}}}" width="150">
        </div>
    </section>
</body>
</html>
""")

    # style.css
    (base / "static" / "css" / "style.css").write_text(f"""body {{ font-family: Arial; margin: 0; padding: 0; }}
header {{ background-color: {couleur}; color: white; padding: 10px 20px; display: flex; align-items: center; gap: 20px; }}
""")

    # README.md
    (base / "README.md").write_text(f"# {nom_site}\n\nCe site est généré automatiquement.\n\n- Couleur principale : {couleur}\n- Dossier : {slug}\n")

    # .gitignore, Procfile, requirements.txt
    (base / "requirements.txt").write_text("Flask")
    (base / "Procfile").write_text("web: gunicorn app:app")
    (base / ".gitignore").write_text("instance/\n*.db\n__pycache__/\n.env")

    # Images vides
    for img in ["logo.png", "banner.jpg", "service1.jpg", "service2.jpg"]:
        (base / "static" / "img" / img).touch()

    # Pages légales HTML
    legal_pages = {
        "cgu.html": f"<h1>Conditions Générales d'Utilisation</h1>\n<p>Bienvenue sur le site {nom_site}. Les présentes conditions régissent l'utilisation du service proposé.</p>",
        "mentions-legales.html": f"<h1>Mentions légales</h1>\n<p><strong>Nom du site :</strong> {nom_site}</p>\n<p><strong>Email :</strong> contact@exemple.com</p>",
        "politique-confidentialite.html": f"<h1>Politique de confidentialité</h1>\n<p>Cette politique explique comment {nom_site} collecte et utilise vos données personnelles.</p>",
        "parametres-cookies.html": f"<h1>Paramètres des cookies</h1>\n<p>Ce site utilise des cookies pour améliorer votre expérience.</p>"
    }

    for filename, html in legal_pages.items():
        (base / "templates" / filename).write_text(html)

    # Footer dans toutes les pages HTML
    footer_html = """
<footer>
    <p>&copy; {{ nom_site }} - Tous droits réservés</p>
    <nav>
        <a href="{{ url_for('cgu') }}">CGU</a> |
        <a href="{{ url_for('mentions_legales') }}">Mentions légales</a> |
        <a href="{{ url_for('politique_confidentialite') }}">Confidentialité</a> |
        <a href="{{ url_for('parametres_cookies') }}">Cookies</a>
    </nav>
</footer>
"""
    for html_file in ["index.html", "cgu.html", "mentions-legales.html", "politique-confidentialite.html", "parametres-cookies.html"]:
        html_path = base / "templates" / html_file
        if html_path.exists():
            with open(html_path, "a", encoding="utf-8") as f:
                f.write(footer_html.strip())

    print(f"✅ Projet '{slug}' généré avec succès.")

if __name__ == "__main__":
    nom_site = input("Nom du site : ")
    slug = input("Nom du dossier (slug) : ")
    couleur = input("Couleur principale (hex) [#00838f] : ") or "#00838f"
    create_project(nom_site, slug, couleur)
