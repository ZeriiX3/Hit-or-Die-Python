################# IMPORT #################
import pygame
import numpy
import math
##########################################



# Munitions

class Bullet(pygame.sprite.Sprite):     # Munitions sans trajectoire

    def __init__(self, joueur, jeu):
        super().__init__()

        # Statistiques des munitions
        self.vitesse = 5
        # Charger l'image des munitions
        self.image = pygame.image.load("images/bullet.png")
        self.image = pygame.transform.scale(self.image, (35, 35))
        self.rect = self.image.get_rect()
        # Positions
        self.rect.x = joueur.rect.x + 108
        self.rect.y = joueur.rect.y - 6

        self.joueur = joueur    # Pour pourvoir utiliser la class joueur dans la fonction mouvement()
        self.jeu = jeu    # Pour pourvoir utiliser la class jeu dans la fonction mouvement()


    # Fonctions

    # Mouvement de la munition de fusil
    def mouvement(self):
        # Les munitions sont en mouvement s'il n'y a pas de collision
        if not self.jeu.check_collision(self, self.jeu.all_monstres) and not self.jeu.check_collision(self, self.jeu.all_boss):
            self.rect.x += self.vitesse

        # Si il y a collision entre les munitions et les monstres
        for monster in self.jeu.check_collision(self, self.jeu.all_monstres):
            self.joueur.all_bullets.remove(self)
            # Dégats infligés aux monstres
            monster.damage(6)

        # Si il y a collision entre les munitions et les boss
        for boss in self.jeu.check_collision(self, self.jeu.all_boss):
            self.joueur.all_bullets.remove(self)
            boss.damage(6)

        # Si les munitions sortent de la fenêtre
        if self.rect.x > 1200:
            # On supprime la munition
            self.joueur.all_bullets.remove(self)
            print("La munition a été supprimé")



class Bombe(pygame.sprite.Sprite):     # Munitions avec trajectoire

    def __init__(self, joueur, jeu):
        super().__init__()

        # Statistiques des munitions
        self.vitesse = 8
        self.angle = 60
        self.time = -5
        self.gravity = 0.02  # Gravité pour la trajectoire courbe

        # Charger l'image des munitions selon la position
        self.image = pygame.image.load("images/bombe.png")
        self.image = pygame.transform.scale(self.image, (37, 37))
        self.rect = self.image.get_rect()
        self.rect.x = joueur.rect.x + 108
        self.rect.y = joueur.rect.y - 6

        self.joueur = joueur  # Pour pourvoir utiliser la class joueur dans la fonction mouvement()
        self.jeu = jeu  # Pour pourvoir utiliser la class jeu dans la fonction mouvement()


    # Fonctions

    # Mouvement de la bombe (en courbe)
    def mouvement_courbe(self):
        self.time += 1
        # Calculer la position en fonction du temps et de l'angle
        radian_angle = math.radians(self.angle)
        self.rect.x += int(self.vitesse * math.cos(radian_angle))
        self.rect.y -= int(self.vitesse * math.sin(radian_angle) - 0.5 * self.gravity * self.time ** 2)

        # Vérification des collisions
        if not self.jeu.check_collision(self, self.jeu.all_monstres) and not self.jeu.check_collision(self, self.jeu.all_boss):
            self.rect.x += self.vitesse
        # Si il y a collision entre les bombes et les monstres
        for monster in self.jeu.check_collision(self, self.jeu.all_monstres):
            self.joueur.all_bombe.remove(self)
            monster.damage(18)
        # Si il y a collision entre les bombes et les boss
        for boss in self.jeu.check_collision(self, self.jeu.all_boss):
            self.joueur.all_bombe.remove(self)
            boss.damage(18)

        # Si les munitions sortent de la fenêtre
        if self.rect.x > 1200 or self.rect.y > 800:
            self.joueur.all_bombe.remove(self)
            print("La munition courbe a été supprimé")


############################################################################

class Apocalypse(pygame.sprite.Sprite):     # APOCALYPSE !!!

    # Sprite d'une bombe nucléaire qui va tuer le joueur s'il perd

    def __init__(self, joueur, jeu):
        super().__init__()

        # Caractéristique de la bombe nucléaire
        self.vitesse = 5
        # Chargement de l'image selon la position
        self.image = pygame.image.load("images/missile.png")
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 20

        # Pour pouvoir les utiliser dans les fonctions
        self.joueur = joueur
        self.jeu = jeu

    # Mouvement de la bombe nucléaire
    def trajectoire(self):
        if not self.joueur.is_alive():
            return

        # Faire descendre la bombe vers le bas jusqu'à ce qu'elle touche le joueur
        self.rect.y += self.vitesse * 0.9

        # Vérifier la collision avec le joueur
        if pygame.sprite.collide_rect(self, self.joueur):
            self.joueur.damage(100)
            print("La bombe a touché le joueur. Le jeu se termine.")
