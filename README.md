# 🦠 Le Jeu de la Vie (Conway's Game of Life)

Une implémentation interactive en Python et Pygame du célèbre automate cellulaire inventé par le mathématicien John Horton Conway. 

Ce projet a été développé avec une architecture propre, séparant le moteur logique de l'interface graphique.

## ✨ Fonctionnalités

* **Menu d'accueil interactif :** Personnalisez l'esthétique de la simulation en choisissant la couleur des cellules vivantes et du fond parmi une palette.
* **Dessin à la volée :** Utilisez la souris comme un pinceau pour donner vie à de nouvelles cellules directement sur la grille.
* **Contrôle du temps :** Figez la simulation à tout moment pour dessiner des structures complexes (vaisseaux, oscillateurs, etc.).
* **Architecture modulaire :** Séparation stricte entre la logique mathématique (`main.py`) et l'affichage graphique (`interface.py`).

## 🛠️ Prérequis

Pour lancer ce projet, vous devez avoir Python installé sur votre machine, ainsi que la bibliothèque graphique Pygame.

```bash
pip install pygame