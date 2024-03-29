# AICoinPost ₿₿₿₿₿

## I - Configuration du Projet

### 1. Installer Ollama

- Exécutez cette commande dans votre invite de commandes Ubuntu (disponible sur Windows via une VM) : curl https://ollama.ai/install.sh | sh

Cela installera Ollama sur votre ordinateur.

- Une fois l'installation terminée, sur la même invite de commande, entrez : ollama serve

- Enfin, exécutez la commande :
ollama run Vicuna

Le LLM Vicuna sera alors en cours d'exécution, et vous pourrez interagir avec lui.

### 2. Installer les Librairies

- Ouvrez l'invite de commandes, localisez-vous dans le dossier du projet et entrez cette commande :
pip install -r requirements.txt

### 3. Installer SQLite3 pour le Stockage des Articles

- Téléchargez le fichier précompilé de SQLite pour Windows depuis le site officiel SQLite : [SQLite Download](https://www.sqlite.org/download.html)

- Ajoutez une nouvelle variable d'environnement dans le PATH de Windows. Elle devrait pointer vers le dossier sqlite-tools-win-x64 🚀

## II - Voir les Résumés dans la Base de Données

1. Entrez la commande qui vous permettra d'interagir avec la base crée:
sqlite3 articles.db

2. Vous pouvez maintenant naviguer dans votre base de données en entrant des requêtes SQL.
- Exemple :
  ```
  select * from articles where id=0;
  ```
  Pour sélectionner l'article 0.

Profitez de l'exploration d'AICoinPost ! 📰🤖
