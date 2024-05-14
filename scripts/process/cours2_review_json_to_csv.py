import csv
import json

"""
Convertit un fichier JSON contenant des commentaires et des évaluations en un fichier CSV 
avec des colonnes 'commentaire' et 'classe' pour les commentaires et leurs classes respectives.
"""

# Lire le fichier JSON
with open("../../data/raw/reviews_with_ratings.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Créer et écrire dans le fichier CSV
with open("../../data/clean/reviews_with_ratings.csv", "w", newline="", encoding="utf-8") as csvfile:
    # Définir les noms de colonnes du fichier CSV
    fieldnames = ["commentaire", "classe"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Écrire les commentaires négatifs
    for dico in data:
        comment = list(dico.keys())[0]
        rating = int(list(dico.values())[0])

        if rating in [1, 2, 3, 4, 5]:
            writer.writerow({"commentaire": comment, "classe": "negatif"})

    # Écrire les commentaires positifs
    for dico in data:
        comment = list(dico.keys())[0]
        rating = int(list(dico.values())[0])

        if rating in [6, 7, 8, 9, 10]:
            writer.writerow({"commentaire": comment, "classe": "positif"})
