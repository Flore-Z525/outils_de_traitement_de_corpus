import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

"""
Cours 5.5
Évaluer mon corpus avec les métriques
"""

df = pd.read_csv('../../data/clean/reviews_with_ratings.csv')

df['classe'] = df['classe'].map({'positif': 1, 'negatif': 0})

# Séparer le jeu de données en ensembles d'entraînement et de test
# Supposons que df soit le DataFrame contenant les données,
# et 'commentaire' soit la colonne de texte,
# et 'classe' soit la colonne d'étiquettes
X = df['commentaire']
y = df['classe']

# Diviser les données en ensembles d'entraînement et de test de manière aléatoire,
# en spécifiant test_size=0.2 pour indiquer que 20% sont utilisés comme ensemble de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=None)

# Convertir les données textuelles en vecteurs numériques
vectorizer = CountVectorizer()
X_train_vectors = vectorizer.fit_transform(X_train)
X_test_vectors = vectorizer.transform(X_test)

# Utiliser un classifieur bayésien naïf multinomial comme exemple de modèle
model = MultinomialNB()
model.fit(X_train_vectors, y_train)

# Prédire sur l'ensemble de test
y_pred = model.predict(X_test_vectors)

# Évaluation
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, zero_division=0)

print(f"Accuracy: {accuracy}")
print(report)
