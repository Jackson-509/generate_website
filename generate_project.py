import os
from pathlib import Path

TEMPLATE_DIR = Path(__file__).parent / "generator_templates"

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
    app_src = (TEMPLATE_DIR / "app.py").read_text()
    (base / "app.py").write_text(app_src)

    # index.html
    index_src = (TEMPLATE_DIR / "index.html").read_text()
    (base / "templates" / "index.html").write_text(index_src.format(nom_site=nom_site))

    # style.css
    style_src = (TEMPLATE_DIR / "style.css").read_text()
    (base / "static" / "css" / "style.css").write_text(style_src.format(couleur=couleur))

    # README.md
    readme_src = (TEMPLATE_DIR / "README.md").read_text()
    (base / "README.md").write_text(readme_src.format(nom_site=nom_site, couleur=couleur, slug=slug))

    # .gitignore, Procfile, requirements.txt
    requirements_src = (TEMPLATE_DIR / "requirements.txt").read_text()
    procfile_src = (TEMPLATE_DIR / "Procfile").read_text()
    gitignore_src = (TEMPLATE_DIR / "gitignore").read_text()
    (base / "requirements.txt").write_text(requirements_src)
    (base / "Procfile").write_text(procfile_src)
    (base / ".gitignore").write_text(gitignore_src)

    # Images vides
    for img in ["logo.png", "banner.jpg", "service1.jpg", "service2.jpg"]:
        (base / "static" / "img" / img).touch()

    # Pages légales HTML
    for page in ["cgu.html", "mentions-legales.html", "politique-confidentialite.html", "parametres-cookies.html"]:
        content = (TEMPLATE_DIR / page).read_text().format(nom_site=nom_site)
        (base / "templates" / page).write_text(content)

    footer = (TEMPLATE_DIR / "footer.html").read_text()
    for html_file in ["index.html", "cgu.html", "mentions-legales.html", "politique-confidentialite.html", "parametres-cookies.html"]:
        html_path = base / "templates" / html_file
        if html_path.exists():
            with open(html_path, "a", encoding="utf-8") as f:
                f.write(footer.strip())

    print(f"✅ Projet '{slug}' généré avec succès.")

if __name__ == "__main__":
    nom_site = input("Nom du site : ")
    slug = input("Nom du dossier (slug) : ")
    couleur = input("Couleur principale (hex) [#00838f] : ") or "#00838f"
    create_project(nom_site, slug, couleur)
