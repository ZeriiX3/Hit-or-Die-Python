import pygame
import numpy
import math



# Munitions

class Bullet(pygame.sprite.Sprite):     # Munitions sans trajectoire

    def __init__(self, joueur, jeu):
        super().__init__()

        # Statistiques des munitions
        self.vitesse = 5
        # Charger l'image des munitions
        self.image = pygame.image.load("assets/bullet.png")
        self.image = pygame.transform.scale(self.image, (35, 35))
        self.rect = self.image.get_rect()
        # Positions
        self.rect.x = joueur.rect.x + 108
        self.rect.y = joueur.rect.y - 6

        self.joueur = joueur    # Pour pourvoir utiliser la class joueur dans la fonction mouvement()
        self.jeu = jeu    # Pour pourvoir utiliser la class jeu dans la fonction mouvement()


    # Fonctions

    def mouvement(self):

        # Les munitions sont en mouvement s'il n'y a pas de collision
        if not self.jeu.check_collision(self, self.jeu.all_monstres):
            self.rect.x += self.vitesse

        if self.jeu.check_collision(self, self.jeu.all_monstres):
            self.joueur.all_bullets.remove(self)

        # Si les munitions sortent de la fenêtre
        if self.rect.x > 1200:
            self.joueur.all_bullets.remove(self)
            print("La munition a été supprimé")



class Bombe(pygame.sprite.Sprite):
    # Munitions avec trajectoire


    def __init__(self, joueur, jeu):
        super().__init__()

        # Statistiques des munitions
        self.vitesse = 8
        self.angle = 60
        self.time = -5
        self.gravity =0.02# Gravité pour la trajectoire courbe

        # Charger l'image des munitions
        self.image = pygame.image.load("assets/bombe.png")
        self.image = pygame.transform.scale(self.image, (37, 37))
        self.rect = self.image.get_rect()
        self.rect.x = joueur.rect.x + 108
        self.rect.y = joueur.rect.y - 6

        self.joueur = joueur  # Pour pouvoir utiliser la classe joueur dans la fonction mouvement()
        self.jeu = jeu  # Pour pouvoir utiliser la classe jeu dans la fonction mouvement()

    def mouvement(self):
        self.rect.x += self.vitesse

        # Si la bombe sort de l'écran, la détruire
        if self.rect.y > self.jeu.hauteur_ecran or self.rect.x > self.jeu.largeur_ecran:
            self.kill()

    def mouvement_courbe(self):
        self.time += 1
        # Calculer la position en fonction du temps et de l'angle
        radian_angle = math.radians(self.angle)
        self.rect.x += int(self.vitesse * math.cos(radian_angle))
        self.rect.y -= int(self.vitesse * math.sin(radian_angle) - 0.5 * self.gravity * self.time ** 2)

        # Si la bombe sort de l'écran, la détruire
        if self.rect.y > self.jeu.hauteur_ecran or self.rect.x > self.jeu.largeur_ecran:
            self.kill()
        """
        # Convertir l'angle en radians
        theta = numpy.radians(self.angle)
        # Accélération due à la gravité (en m/s^2)
        g = -9.81
        # Augmenter le temps
        self.time += 0.1
        # Mettre à jour les coordonnées x et y
        self.rect.x = self.vitesse * self.time * numpy.cos(theta) + 100
        self.rect.y = self.vitesse * self.time * numpy.sin(theta) - 0.5 * g * self.time ** 2 + 200"""

        if not self.jeu.check_collision(self, self.jeu.all_monstres):
            self.rect.x += self.vitesse

        if self.jeu.check_collision(self, self.jeu.all_monstres):
            self.joueur.all_bombe.remove(self)

        # Si les munitions sortent de la fenêtre
        if self.rect.x > 1200 or self.rect.y > 800:
            self.joueur.all_bombe.remove(self)
            print("La munition courbe a été supprimé")
