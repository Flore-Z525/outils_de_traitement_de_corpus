import pandas as pd
from scipy.stats import spearmanr

"""
Cours 5.2

Augmenter la p-value en éliminant les données abérrantes. 
"""

df = pd.read_csv('../../data/clean/reviews_with_ratings.csv')

# Ajouter une colonne 'great_count' pour représenter le nombre d'occurrences du mot "great" dans chaque commentaire
df['great_count'] = df['commentaire'].apply(lambda x: x.lower().count('great'))

# Calculer les quartiles et l'IQR
Q1 = df['great_count'].quantile(0.25)
Q3 = df['great_count'].quantile(0.75)
IQR = Q3 - Q1

# Définir les limites des valeurs aberrantes
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Supprimer les valeurs aberrantes
# Ajouter .copy() pour spécifier explicitement qu'il s'agit d'une copie
df_clean = df[(df['great_count'] >= lower_bound) & (df['great_count'] <= upper_bound)].copy()

# Convertir la classe de sentiment en données numériques
df_clean['sentiment'] = df_clean['classe'].map({'positif': 1, 'negatif': 0})

# Calculer le coefficient de corrélation de Spearman et la p-valeur
correlation, p_value = spearmanr(df_clean['sentiment'], df_clean['great_count'])

print(f"p-value après élimination des données abérrantes: {p_value}")
