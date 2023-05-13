import pygame
import numpy



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

        # Si les munitions sortent de la fenêtre
        if self.rect.x > 1200:
            self.joueur.all_bullets.remove(self)
            print("La munition a été supprimé")



class Bullet_courbe(pygame.sprite.Sprite):     # Munitions avec trajectoire

    def __init__(self, joueur):
        super().__init__()

        # Statistiques des munitions
        self.vitesse = 5
        self.angle = 45
        self.time = 0
        # Charger l'image des munitions
        self.image = pygame.image.load("assets/bombe.png")
        self.image = pygame.transform.scale(self.image, (37, 37))
        self.rect = self.image.get_rect()
        # Positions
        self.rect.x = joueur.rect.x + 108
        self.rect.y = joueur.rect.y - 6

        self.joueur = joueur  # Pour pourvoir utiliser la class joueur dans la fonction mouvement_courbe()


    # Fonctions

    def mouvement_courbe(self):
        # Convertir l'angle en radians
        theta = numpy.radians(self.angle)
        # Accélération due à la gravité (en m/s^2)
        g = -9.81
        # Augmenter le temps
        self.time += 0.1
        # Mettre à jour les coordonnées x et y
        self.rect.x = self.vitesse * self.time * numpy.cos(theta) + 100
        self.rect.y = self.vitesse * self.time * numpy.sin(theta) - 0.5 * g * self.time ** 2 + 200

        # Si les munitions sortent de la fenêtre
        if self.rect.x > 1200 or self.rect.y > 800:
            self.joueur.all_bullets_courbe.remove(self)
            print("La munition courbe a été supprimé")
