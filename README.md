# outils_de_traitement_de_corpus

- la tâche à réaliser

Text Classification

- un corpus qui répond à cette tâche: 

le Datasets "imdb" : 
https://huggingface.co/datasets/imdb

- à quel type de prédiction peut servir ce corpus

classifier les commentaires d'un film en classe positives et classe négative

- à quel modèle il a servi

imdb-sentiment-analysis

- Apprenez moi des choses sur un corpus

Ce Dataset est en anglais (monolingual). 
2 classes ont été définies : neg(0), pos(1). 

Size Categories : 10K < n < 100k

Sub-tasks: sentiment-classification

## présentation de l'arborescence du repo
PROJECT/
<br>├── bin/
<- compiled binaries. 
<br>├── data/ 
<br>│   ├── raw/
<br>│   └── clean/
<br>│
<br>├── figures/        <- figures used in place of a "results" folder. 
<br>├── scripts/
<br>│   ├── process/    <- scripts to maniuplate data between raw, cleaned, final stages.
<br>│   └── plot/	      <- intermediate plotting.
<br>│
<br>├── src
<br>│   ├── model1/     <- various experimental models.
<br>│   ├── model2/
<br>│   └── model3/
<br>│
<br>├── LICENSE
<br>├── Makefile
<br>└── readme.md
