################# IMPORT #################
import pygame
import joueur
from jeu import Jeu
##########################################

# Initialiser pygame
pygame.init()


############################################### Fenêtre ###############################################

# Générer la fenêtre du jeu
pygame.display.set_caption("Hit or Die")

# Taille de la fenêtre
screen = pygame.display.set_mode((1200, 800))


##### AFFICHAGE #####
# Chargement de l'image de fond
background = pygame.image.load("images/fond_ecran1.png")
# Chargement du logo
logo = pygame.image.load("images/logo.png")
# Chargement de logo PLAY
bouton_play = pygame.image.load("images/bouton_play.png")
bouton_play_rect = bouton_play.get_rect()
bouton_play_rect.x = 490
bouton_play_rect.y = 500
# Chargement de l'image de GAME OVER
bg_gameover = pygame.image.load("images/game_over.png")
bg_gameover = pygame.transform.scale(bg_gameover, (1200, 800))
# Chargement de l'image YOU WIN
bg_youwin = pygame.image.load("images/you_win.jpg")
bg_youwin = pygame.transform.scale(bg_youwin, (1200, 800))


# Chargement du jeu à partir de la class Jeu
jeu = Jeu()


########################################## Boucle principale ##########################################

game_running = True
print("Le jeu commence")


while game_running:


    ########################## AFFICHAGE ##########################

    # Affichage du background de base
    screen.blit(background, (0, 0))


    # Si le joueur lance le jeu
    if jeu.in_game:

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
        # Afficher l'image des boss
        for boss in jeu.all_boss:
            boss.check_hp(screen)
            boss.mouvement()
        jeu.all_boss.draw(screen)

       # Afficher l'image de la bombe nucléaire
        for nb in jeu.nuclear_bomb:
            nb.trajectoire()
        jeu.nuclear_bomb.draw(screen)


        # Affichage du score
        jeu.update_score(screen)

        jeu.update_timer(screen)
        jeu.decompte_timer()


    # Sinon on affiche l'écran d'accueil
    else:
        # Affichage de la bannière
        screen.blit(logo, (380,200))
        # Affichage du bouton PLAY
        screen.blit(bouton_play, bouton_play_rect)
        # Si le joueur a perdu
        if jeu.game_out:
            screen.blit(bg_gameover, (0,0))
        # Si le joueur gagne
        elif jeu.win:
            screen.blit(bg_youwin, (0,0))



    ################## Evenement pygame ##################

    # Si le joueur appuie sur UP
    if jeu.key_pressed.get(pygame.K_z) and jeu.joueur.rect.y > 0:
        jeu.joueur.move_top()

    # Si le joueur appuie sur DOWN
    elif jeu.key_pressed.get(pygame.K_s) and jeu.joueur.rect.y < 700:
        jeu.joueur.move_bot()


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

        # Si la touche est relachée
        elif event.type == pygame.KEYUP:
            jeu.key_pressed[event.key] = False

        # Si le bouton de la souris est apuuyé
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Permet de vérifier si la souris est sur les coordonnées du bouton PLAY
            if bouton_play_rect.collidepoint(event.pos):
                # Mise à jour de in_game en True
                jeu.in_game = True

    # Mise à jour de l'écran
    pygame.display.flip()