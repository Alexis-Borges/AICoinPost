# AICoinPost

## I - Configuration du Projet

### 1. Installer Ollama

- Exécutez cette commande dans votre invite de commandes Ubuntu (disponible sur Windows via une VM) :
  ```bash
  curl https://ollama.ai/install.sh | sh
  Cela installera Ollama sur votre ordinateur.
  ```

Une fois l'installation terminée, sur la même invite de commande, entrez :

ollama serve
Enfin, exécutez la commande :

ollama run mistral
Le LLM Mistral sera alors en cours d'exécution, et vous pourrez interagir avec lui. 2. Installer les Librairies
Ouvrez l'invite de commandes, localisez-vous dans le dossier du projet et entrez cette commande :

pip install -r requirements.txt 3. Installer SQLite3 pour le Stockage des Articles
Téléchargez le fichier précompilé de SQLite pour Windows depuis le site officiel SQLite : SQLite Download

Ajoutez une nouvelle variable d'environnement système dans le PATH de Windows. Elle devrait pointer vers le dossier sqlite-tools-win-x64 ( !!! le dossier complet, pas un des fichiers .exe contenu dedans !!!)

Vous pouvez désormais lancer le projet dans de bonnes conditions ! 🚀

II - Voir les Résumés dans la Base de Données
Entrez la commande :
sqlite3 articles.db
Vous pouvez maintenant naviguer dans votre base de données en entrant des requêtes SQL.
Exemple :

select \* from articles where id=0;
Pour sélectionner l'article 0.
⚠️ IMPORTANT : Si vous ne parvenez pas à récupérer d'article, c'est probablement parce qu'aucun n'a été publié aujourd'hui. Vous pouvez modifier la date dans le code à la ligne 71.

Profitez de l'exploration d'AICoinPost ! 📰🤖
