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
        self.vitesse = 5
        # Charger l'image du joueur + position
        self.image = pygame.image.load("joueur.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 200

        self.all_bullets = pygame.sprite.Group()
        self.all_bombe = pygame.sprite.Group()

        self.delai = 200
        self.next_execution_time = 0





    # Fonctions

    def move_top(self):
        self.rect.y -= self.vitesse

    def move_bot(self):
        self.rect.y += self.vitesse

    def lancement(self, jeu):
        current_time = pygame.time.get_ticks()
        if current_time >= self.next_execution_time:
            bullet = Bullet(self, jeu)
            self.all_bullets.add(bullet)
            self.next_execution_time = current_time + self.delai

    def lancement_bombe(self, jeu):
        current_time = pygame.time.get_ticks()
        if current_time >= self.next_execution_time:
            bombe = Bombe(self, jeu)
            self.all_bombe.add(bombe)
            self.next_execution_time = current_time + self.delai+800