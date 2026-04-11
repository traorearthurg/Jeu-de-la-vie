import random


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




    def afficher_console(self):
        """Affiche la grille dans le terminal pour tester."""
        print("--- État actuel de la grille ---")
        for ligne in self.grille:
            print(ligne)


# --- Zone de Test ---
# Ce code ne s'exécute que si tu lances ce fichier directement
if __name__ == "__main__":
    # On crée une "instance" (un objet physique) à partir de notre plan (la classe)
    mon_jeu = JeuDeLaVie(10, 10)
    # On demande à notre objet de s'afficher
    mon_jeu.afficher_console()

print("Voisins de la case (2,2) :", mon_jeu.compter_voisins(2, 2))
