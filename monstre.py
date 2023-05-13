import pygame
import random as rd



# MONSTRES

class Monstre(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.hp = 100
        self.hp_max = 100
        # Charger l'image des monstres + position
        self.image = pygame.image.load("assets/pieuvre.png")
        self.rect = self.image.get_rect()
        self.rect.x = 800 + rd.randint(-300, 300)
        self.rect.y = 190 + rd.randint(-100, 300)


    # Fonctions

    def check_hp(self, rectangle):

        # Couleur du fond de la barre de vie du monstre
        hp_bar_bg_color = (88, 24, 69)  # Gris foncé
        # Position du fond de la barre de vie
        hp_bar_bg_position = [self.rect.x + 15, self.rect.y - 15, self.hp_max, 6]
        # Afficher l'image fond de la barre de vie
        pygame.draw.rect(rectangle, hp_bar_bg_color, hp_bar_bg_position)

        # Couleur de la barre de vie du monstre
        hp_bar_color = (255, 0, 0) # Rouge
        # Position de la barre de vie
        hp_bar_position = [self.rect.x + 15, self.rect.y - 15, self.hp, 6]
        # Afficher l'image de la barre de vie
        pygame.draw.rect(rectangle, hp_bar_color, hp_bar_position)

    def damage(self, damage):
        # Perte de points de vie en fonction des dégats
        self.hp -= damage

        if self.hp <= 0:
            self.rect.x = 800 + rd.randint(-300, 300)
            self.rect.y = 190 + rd.randint(-100, 300)
            self.hp = self.hp_max
            print("Vous avez tué le monstre")


    ############################# MOUVEMENT #############################

    def mouvement(self):
        if rd.random() < 0.1:  #
            self.direction = rd.choice(['up', 'down', 'left', 'right'])

        if self.direction == 'up':
            self.y -= self.speed
        elif self.direction == 'down':
            self.y += self.speed
        elif self.direction == 'left':
            self.x -= self.speed
        elif self.direction == 'right':
            self.x += self.speed

        if self.x < 300:
            self.direction = rd.choice(['up', 'down', 'right'])
        elif self.x > 800 :
            self.direction = rd.choice(['up', 'down', 'left'])
        if self.y < 0:
            self.direction = rd.choice(['down', 'left', 'right'])
        elif self.y > 1200 - self.height:
            self.direction = rd.choice(['up', 'left', 'right'])