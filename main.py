import pygame
import joueur
from jeu import Jeu

pygame.init() # Initialiser pygame


############################################### Fenêtre ###############################################

# Générer la fenêtre du jeu
pygame.display.set_caption("Hit or Die")

# Taille de la fenêtre
screen = pygame.display.set_mode((1200, 800))

# Chargement de l'image de fond
background = pygame.image.load("fond_ecran1.png")


# Chargement du jeu à partir de la class Jeu
jeu = Jeu()


########################################## Boucle principale ##########################################

game_running = True
print("Le jeu commence")


while game_running:

    # Si le joueur appuie sur UP
    if jeu.key_pressed.get(pygame.K_UP) and jeu.joueur.rect.y > 0:
        jeu.joueur.move_top()

    # Si le joueur appuie sur DOWN
    elif jeu.key_pressed.get(pygame.K_DOWN)  and jeu.joueur.rect.y < 700:
        jeu.joueur.move_bot()


    ############# AFFICHAGE #############

    # Affichage du background
    screen.blit(background, (0, 0))

    # Afficher l'image du joueur
    screen.blit(jeu.joueur.image, jeu.joueur.rect)

    # Afficher les images des munitions
    for bullet in jeu.joueur.all_bullets:   # Munitions avec trajectoire
        bullet.mouvement()
    jeu.joueur.all_bullets.draw(screen)

    for bullet_courbe in jeu.joueur.all_bombe:   # Munitions sans trajectoire
        bullet_courbe.mouvement_courbe()
    jeu.joueur.all_bombe.draw(screen)

    # Afficher l'image des monstres
    for monstre in jeu.all_monstres:
        monstre.check_hp(screen)
        monstre.mouvement()
    jeu.all_monstres.draw(screen)

    for boss in jeu.all_boss:
        boss.check_hp(screen)
        boss.mouvement()
    jeu.all_boss.draw(screen)

    # Mise à jour de l'écran
    pygame.display.flip()

    ################## Evenement pygame ##################

    for event in pygame.event.get():
        # Fermeture du jeu
        if event.type == pygame.QUIT:
            game_running = False
            pygame.quit()
            print("Vous avez fermé le jeu")

        # Si le joueur appuie sur une touche
        elif event.type == pygame.KEYDOWN:
            jeu.key_pressed[event.key] = True
            # Si le joueur appuie sur ESP
            if event.key == pygame.K_SPACE:
                jeu.joueur.lancement(jeu)
            # Si le joueur appuie sur ENTER
            elif event.key == pygame.K_RETURN:
                jeu.joueur.lancement_bombe(jeu)

        elif event.type == pygame.KEYUP:
            jeu.key_pressed[event.key] = False

