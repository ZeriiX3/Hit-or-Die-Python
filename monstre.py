import pygame



# MONSTRES

class Monstre(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.hp = 100
        self.hp_max = 100
        self.damage = 10
        # Charger l'image des monstres + position
        self.image = pygame.image.load("assets/pieuvre.png")
        self.rect = self.image.get_rect()
        self.rect.x = 800
        self.rect.y = 190
