import pygame
import sys
from main import JeuDeLaVie

# On démarre le moteur interne de Pygame
pygame.init()
pygame.font.init()  # On allume le moteur de texte

# On prépare nos polices d'écriture
police_titre = pygame.font.SysFont("Arial", 50, bold=True)
police_bouton = pygame.font.SysFont("Arial", 30, bold=True)

LIGNES = 30
COLONNES = 40
TAILLE_CELLULE = 20

LARGEUR = COLONNES * TAILLE_CELLULE
HAUTEUR = LIGNES * TAILLE_CELLULE

ecran = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Le Jeu de la Vie")
horloge = pygame.time.Clock()

mon_jeu = JeuDeLaVie(LIGNES, COLONNES)

# ==========================================
# --- VARIABLES D'ÉTAT ET DE MENU ---
# ==========================================
etat = "MENU"
couleur_vivante = (255, 255, 255)  # Blanc par défaut
couleur_morte = (0, 0, 0)  # Noir par défaut

# Palettes (Couleurs et Boîtes de clic)
PALETTE_VIVANTE = [(255, 255, 255), (255, 80, 80), (80, 255, 80), (255, 255, 80)]
BOITES_VIVANTES = [
    pygame.Rect(LARGEUR // 2 - 100, 250, 40, 40),
    pygame.Rect(LARGEUR // 2 - 40, 250, 40, 40),
    pygame.Rect(LARGEUR // 2 + 20, 250, 40, 40),
    pygame.Rect(LARGEUR // 2 + 80, 250, 40, 40)
]

PALETTE_MORTE = [(0, 0, 0), (0, 0, 40), (40, 0, 40), (40, 40, 40)]
BOITES_MORTES = [
    pygame.Rect(LARGEUR // 2 - 100, 350, 40, 40),
    pygame.Rect(LARGEUR // 2 - 40, 350, 40, 40),
    pygame.Rect(LARGEUR // 2 + 20, 350, 40, 40),
    pygame.Rect(LARGEUR // 2 + 80, 350, 40, 40)
]

# ==========================================
# --- LA BOUCLE INFINIE ---
# ==========================================
en_cours = True
pause = False

while en_cours:

    # A. ÉCOUTER LES ÉVÉNEMENTS
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            en_cours = False

            # --- ÉVÉNEMENTS DU MENU ---
        if etat == "MENU":
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if evenement.button == 1:
                    pos_souris = pygame.mouse.get_pos()

                    # 1. Vérification du bouton Démarrer
                    rect_bouton_start = pygame.Rect(0, 0, 200, 60)
                    rect_bouton_start.center = (LARGEUR // 2, HAUTEUR - 100)
                    if rect_bouton_start.collidepoint(pos_souris):
                        etat = "JEU"

                    # 2. Vérification de la palette Vivante
                    for i in range(4):
                        if BOITES_VIVANTES[i].collidepoint(pos_souris):
                            couleur_vivante = PALETTE_VIVANTE[i]

                    # 3. Vérification de la palette Morte
                    for i in range(4):
                        if BOITES_MORTES[i].collidepoint(pos_souris):
                            couleur_morte = PALETTE_MORTE[i]

        # --- ÉVÉNEMENTS DU JEU ---
        elif etat == "JEU":
            if evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_SPACE:
                    pause = not pause

    # B & C. LOGIQUE ET DESSIN
    if etat == "MENU":
        ecran.fill((40, 40, 50))

        # Titre
        texte_titre = police_titre.render("LE JEU DE LA VIE", True, (255, 255, 255))
        rect_titre = texte_titre.get_rect(center=(LARGEUR // 2, HAUTEUR // 6))
        ecran.blit(texte_titre, rect_titre)

        # Bouton Démarrer
        rect_bouton_start = pygame.Rect(0, 0, 200, 60)
        rect_bouton_start.center = (LARGEUR // 2, HAUTEUR - 100)
        pygame.draw.rect(ecran, (100, 200, 100), rect_bouton_start, border_radius=10)
        texte_bouton = police_bouton.render("DÉMARRER", True, (255, 255, 255))
        rect_texte = texte_bouton.get_rect(center=rect_bouton_start.center)
        ecran.blit(texte_bouton, rect_texte)

        # Palette Vivante
        texte_c_vivante = police_bouton.render("Couleur des cellules :", True, (200, 200, 200))
        rect_texte_cv = texte_c_vivante.get_rect(center=(LARGEUR // 2, 210))
        ecran.blit(texte_c_vivante, rect_texte_cv)

        for i in range(4):
            pygame.draw.rect(ecran, PALETTE_VIVANTE[i], BOITES_VIVANTES[i])
            if couleur_vivante == PALETTE_VIVANTE[i]:
                pygame.draw.rect(ecran, (0, 255, 255), BOITES_VIVANTES[i], 4)

        # Palette Morte
        texte_c_morte = police_bouton.render("Couleur du fond :", True, (200, 200, 200))
        rect_texte_cm = texte_c_morte.get_rect(center=(LARGEUR // 2, 320))
        ecran.blit(texte_c_morte, rect_texte_cm)

        for i in range(4):
            pygame.draw.rect(ecran, PALETTE_MORTE[i], BOITES_MORTES[i])
            if couleur_morte == PALETTE_MORTE[i]:
                pygame.draw.rect(ecran, (0, 255, 255), BOITES_MORTES[i], 4)

    elif etat == "JEU":
        if not pause:
            mon_jeu.generation_suivante()

        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            colonne = pos[0] // TAILLE_CELLULE
            ligne = pos[1] // TAILLE_CELLULE
            if 0 <= ligne < LIGNES and 0 <= colonne < COLONNES:
                mon_jeu.grille[ligne][colonne] = 1

        # On peint le fond avec la couleur choisie dans le menu
        ecran.fill(couleur_morte)

        for ligne in range(mon_jeu.lignes):
            for colonne in range(mon_jeu.colonnes):
                if mon_jeu.grille[ligne][colonne] == 1:
                    x = colonne * TAILLE_CELLULE
                    y = ligne * TAILLE_CELLULE
                    # On peint les cases avec la couleur choisie dans le menu
                    pygame.draw.rect(ecran, couleur_vivante, (x, y, TAILLE_CELLULE, TAILLE_CELLULE))

    pygame.display.flip()
    horloge.tick(10)

pygame.quit()
sys.exit()