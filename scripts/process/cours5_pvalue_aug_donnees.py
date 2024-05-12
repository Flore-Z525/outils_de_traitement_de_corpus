import pandas as pd
from scipy.stats import spearmanr
import random

df = pd.read_csv('../../data/clean/reviews_with_ratings.csv')

# calculer le nombre d'occurrences de "great"
def count_great(text):
    return text.lower().count('great')

# insérer, échanger ou supprimer aléatoirement des mots
def augment_text(text):
    words = text.split()
    if len(words) > 1:
        if random.random() < 0.33:
            # supprimer un mot aléatoire
            del words[random.randint(0, len(words) - 1)]
        elif random.random() < 0.33:
            # échanger les positions de deux mots aléatoires
            idx1 = random.randint(0, len(words) - 1)
            idx2 = random.randint(0, len(words) - 1)
            words[idx1], words[idx2] = words[idx2], words[idx1]
        else:
            # insérer un "great" (ou un autre mot) à une position aléatoire
            insert_idx = random.randint(0, len(words))
            words.insert(insert_idx, "great")
    return ' '.join(words)

# p-value originale
original_great_count = df['commentaire'].apply(count_great)
original_pvalue = spearmanr(df['classe'].map({'positif': 1, 'negatif': 0}), original_great_count)[1]

# augmenter les données
df['augmented_commentaire'] = df['commentaire'].apply(augment_text)
enhanced_great_count = df['augmented_commentaire'].apply(count_great)

# p-value des données augmentées
enhanced_pvalue = spearmanr(df['classe'].map({'positif': 1, 'negatif': 0}), enhanced_great_count)[1]

print(f"Original p-value: {original_pvalue}")
print(f"Enhanced p-value: {enhanced_pvalue}")