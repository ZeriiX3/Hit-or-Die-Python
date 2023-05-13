import pygame
from bullet import Bullet
from bullet import Bullet_courbe

# JOUEUR

class Joueur(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        # Statistiques du joueur
        self.hp = 100
        self.hp_max = 100
        self.damage = 10
        self.vitesse = 10
        # Charger l'image du joueur + position
        self.image = pygame.image.load("assets/joueur.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 200

        self.all_bullets = pygame.sprite.Group()
        self.all_bullets_courbe = pygame.sprite.Group()


    # Fonctions

    def move_right(self):
        self.rect.x += self.vitesse

    def move_left(self):
        self.rect.x -= self.vitesse

    def lancement(self):
        bullet = Bullet(self)
        self.all_bullets.add(bullet)

    def lancement_courbe(self):
        bullet_courbe = Bullet_courbe(self)
        self.all_bullets_courbe.add(bullet_courbe)
