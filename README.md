# outils_de_traitement_de_corpus

- la tâche à réaliser

Image Classification

- un corpus qui répond à cette tâche: 

le Datasets "Visual_Emotional_Analysis" : https://huggingface.co/datasets/FastJobs/Visual_Emotional_Analysis

- à quel type de prédiction peut servir ce corpus

donner les émotions des gens selon leurs images

- à quel modèle il a servi

emotion_classfication

- Apprenez moi des choses sur un corpus

Ce Dataset est en anglais. 
8 classes ont été définies : anger(0), contempt(1), disgust(2), fear(3), happy(4), neutral(5), sad(6), surprise(7). 

Size Categories : 10K < n < 100k

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
