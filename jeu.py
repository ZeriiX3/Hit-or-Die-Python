import pygame
from joueur import Joueur
from monstre import Monstre, Boss


# JEU

class Jeu:

    def __init__(self):
        # Joueur
        self.joueur = Joueur()


        # Monstres
        self.all_monstres = pygame.sprite.Group()
        self.all_boss = pygame.sprite.Group()

        """self.spawn_monstre()"""
        self.spawn_boss()


        """
        if Monstre.niveau == 1:
            self.spawn_monstre()
        elif Monstre.niveau == 2:
            self.spawn_monstre()
            self.spawn_monstre()
        elif Monstre.niveau == 4 :
            self.spawn_monstre()
            self.spawn_monstre()
            self.spawn_monstre()"""

        # Touches
        self.key_pressed = {}


    # Fonctions

    def spawn_monstre(self):
        monstre = Monstre()
        self.all_monstres.add(monstre)

    def spawn_boss(self):
        boss = Boss()
        self.all_boss.add(boss)


    # Gestion des collisions
    def check_collision(self, element, group_element):
        return pygame.sprite.spritecollide(element, group_element, False, pygame.sprite.collide_mask)