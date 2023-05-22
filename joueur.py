################# IMPORT #################
import pygame
from bullet import Bullet
from bullet import Bombe
##########################################



# JOUEUR

class Joueur(pygame.sprite.Sprite):

    def __init__(self, jeu):
        super().__init__()

        self.jeu = jeu    # Pour pourvoir utiliser la class jeu dans les fonctions

        # Statistiques du joueur
        self.hp = 100
        self.hp_max = 100
        self.vitesse = 5
        # Charger l'image du joueur + position
        self.image = pygame.image.load("images/joueur.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 200

        # Création des groupes de Sprite
        self.all_bullets = pygame.sprite.Group()
        self.all_bombe = pygame.sprite.Group()

        # Délai entre chaque balles
        self.delai = 200
        self.next_execution_time = 0

    # Dégats sur le joueur
    def damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.rect.x = -1000  # Déplace le sprite hors de l'écran si les points de vie sont épuisés
            self.jeu.game_over()


    ######## Fonctions ########

    # Déplacement vers le haut
    def move_top(self):
        self.rect.y -= self.vitesse
    # Déplacement vers le bas
    def move_bot(self):
        self.rect.y += self.vitesse

    # Lancement de la balle de fusil
    def lancement(self, jeu):
        current_time = pygame.time.get_ticks()
        if current_time >= self.next_execution_time:
            bullet = Bullet(self, jeu)
            self.all_bullets.add(bullet)
            self.next_execution_time = current_time + self.delai

    # Lancement de la bombe
    def lancement_bombe(self, jeu):
        current_time = pygame.time.get_ticks()
        if current_time >= self.next_execution_time:
            bombe = Bombe(self, jeu)
            self.all_bombe.add(bombe)
            self.next_execution_time = current_time + self.delai+800

    # Fonction permettant de clear les groupes de sprite
    def clear_bullets(self):
        self.all_bullets.empty()
        self.all_bombe.empty()

    # Vérifie si le joueur est en vie
    def is_alive(self):
        return self.hp > 0
