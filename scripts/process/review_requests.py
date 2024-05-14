import requests
from bs4 import BeautifulSoup
import os

"""
Voici un brouillon. Le script final n'a pas utilisé cette version.
Ce script enregistre chaque commentaire extrait depuis l'URL dans un fichier texte individuel. 
Les fichiers seront stockés dans le répertoire '../../data/clean'.
"""

save_dir = os.path.abspath(os.path.join(os.getcwd(), "../../data/clean"))

# n = 0

# Envoyer une requête GET pour obtenir le contenu de la page web
urls = ["https://www.imdb.com/title/tt0411195/reviews?ref_=tt_urv",
        "https://www.imdb.com/title/tt0120737/reviews?ref_=tt_urv",
        "https://www.imdb.com/title/tt0167261/reviews?ref_=tt_urv",
        "https://www.imdb.com/title/tt10648342/reviews?ref_=tt_urv",
        "https://www.imdb.com/title/tt9419884/reviews?ref_=tt_urv"]

file_count = 0

for url in urls:
    response = requests.get(url)

    # Analyser le contenu HTML avec BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Trouver tous les éléments div avec class="text showmore__control"
    reviews = soup.find_all("div", class_="text show-more__control"
                            or "text show-more__control clickable"
                            or "text show-more__control custom-cursor-on-hover")

    # Parcourir chaque commentaire et le sauvegarder dans un fichier txt indépendant
    for review in reviews:
        file_count += 1
        file_path = os.path.join(save_dir, f"review_{file_count}.txt")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(review.text.strip())

print(f'reviews sauvegardés dans le dossier "data/clean"')


