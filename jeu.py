import pygame
from joueur import Joueur
from monstre import Monstre

# JEU

class Jeu:

    def __init__(self):
        # Joueur
        self.joueur = Joueur()

        # Monstres
        self.all_monstres = pygame.sprite.Group()
        self.spawn_monstre()


    # Fonctions

    def spawn_monstre(self):
        monstre = Monstre()
        self.all_monstres.add(monstre)

    # Gestion des collisions
    def check_collision(self, element, group_element):
        return pygame.sprite.spritecollide(element, group_element, False, pygame.sprite.collide_mask)
