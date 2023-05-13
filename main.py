import pygame
from jeu import Jeu



pygame.init() # Initialiser pygame



############################################### Fenêtre ###############################################

# Générer la fenêtre du jeu
pygame.display.set_caption("Hit or Die")
# Taille de la fenêtre
screen = pygame.display.set_mode((1200, 800))
# Chargement de l'image de fond
background = pygame.image.load("assets/fond_ecran1.png")

# Chargement du jeu à partir de la class Jeu
jeu = Jeu()


########################################## Boucle principale ##########################################

game_running = True
print("Le jeu commence")


while game_running:

    ############# AFFICHAGE #############

    # Affichage du background
    screen.blit(background, (0, 0))

    # Afficher l'image du joueur
    screen.blit(jeu.joueur.image, jeu.joueur.rect)

    # Afficher les images des munitions
    for bullet in jeu.joueur.all_bullets:   # Munitions avec trajectoire
        bullet.mouvement()
    jeu.joueur.all_bullets.draw(screen)

    for bullet_courbe in jeu.joueur.all_bullets_courbe:   # Munitions sans trajectoire
        bullet_courbe.mouvement_courbe()
    jeu.joueur.all_bullets_courbe.draw(screen)



    ####################################
    ###### Mise à jour de l'écran ######
    pygame.display.flip() ##############
    ####################################


    # Evenement pygame
    for event in pygame.event.get():
        # Fermeture du jeu
        if event.type == pygame.QUIT:
            game_running = False
            pygame.quit()
            print("Vous avez fermé le jeu")

        # Si le joueur appuie sur une touche
        elif event.type == pygame.KEYDOWN:
            # Si le joueur appuie sur D
            if event.key == pygame.K_d and jeu.joueur.rect.x < 1092:
                jeu.joueur.move_right()
                print("Déplacement vers la droite")
            # Si le joueur appuie sur Q
            elif event.key == pygame.K_q and jeu.joueur.rect.x > 0:
                jeu.joueur.move_left()
                print("Déplacement vers la gauche")
            # Si le joueur appuie sur ESP
            elif event.key == pygame.K_SPACE:
                jeu.joueur.lancement()
            # Si le joueur appuie sur ENTER
            elif event.key == pygame.K_RETURN:
                jeu.joueur.lancement_courbe()
