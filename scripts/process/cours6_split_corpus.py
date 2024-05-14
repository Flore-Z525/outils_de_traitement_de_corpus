import pandas as pd
from sklearn.model_selection import train_test_split

"""
Ce script est utilisé pour diviser le corpus 
en ensembles d'entraînement (train), de développement (dev) et de test, selon un ratio de 8:1:1. 

Chaque division génère aléatoirement des contenus pour l'ensemble de train, de test et de dev. 

Dans chaque division, 20% des échantillons sont classés comme négatifs dans les ensembles de dev et de test.
"""

# Chargement des données
data_path = "../../data/clean/reviews_with_ratings.csv"
df = pd.read_csv(data_path)

# Division du jeu de données
# Division en données de train et données temporaires
train_data, temp_data = train_test_split(df, test_size=0.2, random_state=42)
# Division des données temporaires en données de dev et de test
dev_data, test_data = train_test_split(temp_data, test_size=0.5, random_state=42)

# Assurer que 20% des échantillons dans les ensembles de dev et de test sont classés comme négatifs
negatif_dev_size = int(0.2 * len(dev_data))
negatif_test_size = int(0.2 * len(test_data))

# Obtenir les index des échantillons classés comme négatifs dans les ensembles de dev et de test
negatif_dev_indices = dev_data[dev_data['classe'] == 'negatif'].sample(n=negatif_dev_size, random_state=42).index
negatif_test_indices = test_data[test_data['classe'] == 'negatif'].sample(n=negatif_test_size, random_state=42).index

# Mettre à jour les échantillons dans les ensembles de dev et de test
dev_data.loc[negatif_dev_indices, 'classe'] = 'negatif'
test_data.loc[negatif_test_indices, 'classe'] = 'negatif'

# Sauvegarde des données divisées
train_data.to_csv("../../data/clean/train_data.csv", index=False)
dev_data.to_csv("../../data/clean/dev_data.csv", index=False)
test_data.to_csv("../../data/clean/test_data.csv", index=False)
