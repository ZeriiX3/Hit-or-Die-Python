import pygame

pygame.init() # Initialiser



################################################ CLASS ################################################


# JOUEUR

class Joueur(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        # Statistiques du joueur
        self.hp = 100
        self.hp_max = 100
        self.damage = 10
        self.image_joueur = pygame.image.load("assets/joueur.png")  # Charger l'image du joueur
        self.rect_joueur = self.image_joueur.get_rect()
        self.rect_joueur.y = 200



############################################### Fenêtre ###############################################

# Générer la fenêtre du jeu
pygame.display.set_caption("Hit or Die")
# Taille de la fenêtre
screen = pygame.display.set_mode((1200, 800))
# Chargement de l'image de fond
background = pygame.image.load("assets/fond_ecran1.png")

# Chargement de la class Joueur
joueur = Joueur()



########################################## Boucle principale ##########################################

game_running = True
print("Le jeu commence")

while game_running:

    # Affichage du background
    screen.blit(background, (0, 0))

    # Afficher l'image du joueur
    screen.blit(joueur.image_joueur, joueur.rect_joueur)

    ###### Mise à jour de l'écran ######
    pygame.display.flip()


    for event in pygame.event.get():    # Fermeture du jeu
        if event.type == pygame.QUIT:
            game_running = False
            pygame.quit()
            print("Vous avez fermé le jeu")
