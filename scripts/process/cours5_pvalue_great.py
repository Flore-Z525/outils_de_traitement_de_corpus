import pandas as pd
from scipy.stats import spearmanr

"""
Cours 5.1

Mesurer la correlation entre le nombre d'occurrences du mot 'great' et la classification du commentaire.
"""

# Chargement du fichier CSV
df = pd.read_csv('../../data/clean/reviews_with_ratings.csv')

# Définition de la représentation numérique du sentiment, en attribuant 1 à 'positif' et 0 à 'negatif'
df['sentiment'] = df['classe'].map({'positif': 1, 'negatif': 0})

# Calcul du nombre d'occurrences du mot "great" dans chaque commentaire
df['great_count'] = df['commentaire'].apply(lambda x: x.lower().count('great'))

# Calcul du coefficient de corrélation de Spearman entre le sentiment et le nombre d'occurrences du mot "great"
correlation, p_value = spearmanr(df['sentiment'], df['great_count'])

# Affichage du coefficient de corrélation et de la p-value
print(f"Corrélation de Spearman : {correlation}")
print(f"p-value : {p_value}")

"""
Corrélation de Spearman : 0.1958960634263815
p-value : 0.03350599863360888

Le coefficient de corrélation de Spearman obtenu, qui est de 0,1958960634263815,
indique une faible corrélation positive entre l'inclination émotionnelle (positive/négative)
et le nombre de fois où le mot "great" apparaît dans le contenu des critiques de films.

La valeur p de 0,03350599863360888,
qui est inférieure au niveau de significativité courant de 0,05,
signifie que cette corrélation est statistiquement significative.
Cela implique qu'il y a moins de 3,35% de chances que cette corrélation soit due au hasard.
Cependant, l'effet est faible,
ce qui souligne que le mot "great" n'est qu'un facteur mineur dans la prédiction de l'inclination émotionnelle.
"""