import pygame
from bullet import Bullet
from bullet import Bombe

# JOUEUR

class Joueur(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        # Statistiques du joueur
        self.hp = 100
        self.hp_max = 100
        self.vitesse = 3
        # Charger l'image du joueur + position
        self.image = pygame.image.load("assets/joueur.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 200

        self.all_bullets = pygame.sprite.Group()
        self.all_bombe = pygame.sprite.Group()


    # Fonctions

    def move_top(self):
        self.rect.y -= self.vitesse

    def move_bot(self):
        self.rect.y += self.vitesse

    def lancement(self, jeu):
        bullet = Bullet(self, jeu)
        self.all_bullets.add(bullet)

    def lancement_bombe(self, jeu):
        bombe = Bombe(self, jeu)
        self.all_bombe.add(bombe)
