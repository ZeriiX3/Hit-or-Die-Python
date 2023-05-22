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

        # Score à 0
        self.score = 0
        
        
        
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
    
    # Affichage du score
    def update_score(self, screen):
        font = pygame.font.SysFont("monospace", 16)
        score_text = font.render(f"Score : {self.score}", 1, (255, 255, 255 ))
        screen.blit(score_text, (20, 20))
    
