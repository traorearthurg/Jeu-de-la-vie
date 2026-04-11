import random
import time

class JeuDeLaVie:
    # 1. Le Constructeur (Initialisation de l'objet)
    def __init__(self, lignes, colonnes):
        """Cette méthode est appelée automatiquement quand on crée un nouveau jeu."""
        # 'self' représente l'objet lui-même.
        # On stocke les dimensions à l'intérieur de l'objet.
        self.lignes = lignes
        self.colonnes = colonnes

        # On crée la grille dès la naissance de l'objet en appelant notre propre méthode
        self.grille = self._creer_grille_initiale()

    # 2. Les Méthodes (Les actions que l'objet peut faire)
    def _creer_grille_initiale(self):
        """Génère et retourne une liste de listes (la grille)."""

        grille_principale =[]
        for i in range(self.lignes):
            nouvelle_ligne = []
            for j in range (self.colonnes):
                r = random.randint(0,1)
                nouvelle_ligne.append(r)
            grille_principale.append(nouvelle_ligne)
        return grille_principale

    def compter_voisins(self, ligne, colonne):
        """Compte les voisins directs de chaques célulles ( + diagonales)"""
        compteur = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == 0 and j == 0:
                    continue
                if ligne+i <0 or ligne+i == self.lignes:
                    continue
                if colonne+j <0 or colonne+j ==self.colonnes:
                    continue
                if self.grille[ligne+i][colonne+j] == 1:
                    compteur+=1
        return compteur



    def generation_suivante(self):
        """ Mets à jour la grille selon les règles de Conway"""
        nouvelle_grille = []

        for i in range(self.lignes):
            nouvelle_ligne = []
            for j in range (self.colonnes):
                nb_voisins = self.compter_voisins(i,j)
                if self.grille[i][j]==1:
                    if nb_voisins < 2:
                        nouvelle_ligne.append(0)
                    elif nb_voisins == 2 or nb_voisins == 3:
                        nouvelle_ligne.append(1)
                    elif nb_voisins > 3:
                        nouvelle_ligne.append(0)
                else:
                    if nb_voisins ==3:
                        nouvelle_ligne.append(1)
                    else:
                        nouvelle_ligne.append(0)

            nouvelle_grille.append(nouvelle_ligne)
        self.grille = nouvelle_grille

    def afficher_console(self):
        """Affiche la grille dans le terminal pour tester."""
        print("--- État actuel de la grille ---")
        for ligne in self.grille:
            print(ligne)


# --- Zone de Test ---
if __name__ == "__main__":
    # On crée une "instance"
    mon_jeu = JeuDeLaVie(10, 10)
    # On va faire évoluer la grille 5 fois de suite
    for tour in range(5):
        print(f"\n--- Génération {tour} ---")
        mon_jeu.afficher_console()
        mon_jeu.generation_suivante()
        time.sleep(1)  # Fait une pause d'1 seconde pour qu'on ait le temps de lire