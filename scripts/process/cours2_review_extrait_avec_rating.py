import requests
from bs4 import BeautifulSoup
import os
import json

"""
Extraire les commentaires depuis les urls, avec leurs ratings. 
Sauvegarder les commentaires et leurs ratings dans un fichier json 
(pour faciliter plus tard la conversion en csv). 
"""

save_dir = os.path.abspath(os.path.join(os.getcwd(), "../../data/raw"))

# Liste pour stocker tous les dictionnaires
all_dicos = []

urls = [
    "https://www.imdb.com/title/tt0411195/reviews?ref_=tt_urv",
    "https://www.imdb.com/title/tt0120737/reviews?ref_=tt_urv",
    "https://www.imdb.com/title/tt0167261/reviews?ref_=tt_urv",
    "https://www.imdb.com/title/tt10648342/reviews?ref_=tt_urv",
    "https://www.imdb.com/title/tt9419884/reviews?ref_=tt_urv"
]

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Trouver tous les commentaires et leurs notes
    reviews_with_ratings = soup.find_all("div", class_="lister-item-content")


    for review_with_rating in reviews_with_ratings:
        # Dictionnaire pour stocker un commentaire individuel
        dico = {}
        # Extraction du contenu d'un commentaire
        review_text = review_with_rating.find("div", class_="text show-more__control"
                                                       or "text show-more__control clickable"
                                                       or "text show-more__control custom-cursor-on-hover")
        review = review_text.text
        # Extraction des informations de rating
        rating_tag = review_with_rating.find("span", class_="rating-other-user-rating")
        if rating_tag:
            # On suppose qu'il n'y a qu'un seul <span> contenant les chiffres sous chaque balise de rating
            rating = rating_tag.find("span").text
            dico[review] = rating

            # Ajouter le dictionnaire du commentaire actuel à la liste globale
            all_dicos.append(dico)

# print(all_dicos)

# Chemin du fichier cible
file_path = os.path.join(save_dir, "reviews_with_ratings.json")

# Écrire le contenu de la liste 'all_dicos' dans le fichier JSON
with open(file_path, "w", encoding="utf-8") as file:
    json.dump(all_dicos, file, indent=4, ensure_ascii=False)
