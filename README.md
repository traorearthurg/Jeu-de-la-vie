📝 Feuille de Route : Projet Jeu de la Vie (Python + Pygame + DevOps)
Phase 1 : Environnement & Setup (Le socle)

    [ ] Dossier : Créer le dossier du projet.

    [ ] Git : Initialiser le dépôt avec git init.

    [ ] Venv : Créer un environnement virtuel (python -m venv venv) et l'activer.

    [ ] Gitignore : Créer un fichier .gitignore (pour exclure venv/, __pycache__/, etc.).

    [ ] Requirements : Créer requirements.txt et y ajouter pygame.

    💡 Commit suggéré : chore: initialisation du projet et environnement

Phase 2 : Le Moteur Logique (Algorithme pur)

    Objectif : Faire tourner le jeu de la vie dans le terminal ou via des tests sans interface.

    [ ] Initialisation : Créer une grille (liste de listes) remplie de 0 et 1.

    [ ] Voisinage : Coder la fonction qui compte les 8 voisins d'une cellule.

    [ ] Règles : Coder la fonction evolution() qui applique les 4 règles de Conway.

    💡 Commits suggérés :

        feat: structure de la grille de jeu

        feat: logique de comptage des voisins

        feat: application des règles de Conway

Phase 3 : Interface Graphique (Pygame)

    Objectif : Transformer tes 0 et 1 en carrés noirs et blancs.

    [ ] Fenêtre : Initialiser Pygame et ouvrir une fenêtre.

    [ ] Rendu : Créer la boucle qui dessine chaque cellule de ta grille sur l'écran.

    [ ] Horloge : Gérer les FPS (images par seconde) pour que l'évolution ne soit pas trop rapide.

    💡 Commits suggérés :

        feat: initialisation de la fenêtre Pygame

        feat: rendu graphique de la grille

Phase 4 : Interactions & Contrôles

    [ ] Souris : Permettre d'activer/désactiver une cellule en cliquant dessus.

    [ ] Clavier : Utiliser Espace pour mettre le jeu en Pause/Play.

    [ ] Reset : Ajouter une touche pour vider la grille ou la remplir aléatoirement.

    💡 Commits suggérés :

        feat: ajout des contrôles souris pour dessiner

        feat: gestion de la pause et des raccourcis clavier

Phase 5 : DevOps & Automatisation

    [ ] Docker : Créer un Dockerfile pour conteneuriser ton projet.

    [ ] CI/CD : Créer un dossier .github/workflows/ pour automatiser les tests ou la vérification du code à chaque push.

    [ ] Readme : Rédiger un README.md propre (titre, installation, utilisation).

    💡 Commits suggérés :

        feat: conteneurisation avec Docker

        ci: ajout du workflow de test GitHub Actions