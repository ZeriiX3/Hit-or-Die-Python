################# IMPORT #################
import pygame
from joueur import Joueur
from monstre import Monstre, Boss
from bullet import Apocalypse
##########################################


# JEU

class Jeu:

    def __init__(self):

        # Joueur
        self.joueur = Joueur(self)
        # Définir si le joueur a commencé le jeu
        self.in_game = False
        # Définir si le jeu est fini
        self.game_out = False
        # Définir si le joueur a gagné
        self.win = False

        # Monstres (regroupe les Sprites dans un groupe de Sprite
        self.all_monstres = pygame.sprite.Group()       # Groupe de monstres
        self.all_boss = pygame.sprite.Group()           # Groupe de boss
        self.nuclear_bomb = pygame.sprite.Group()       # Groupe de la bombe nucléaire

        # Touches
        self.key_pressed = {}

        # Ajoute 3 monstres une fois que tous les autres sont morts
        self.monster_multiplier = 3

        # Compteur de monstres tués
        self.monsters_killed = 0

        # Nombre de monstres tués avant que le boss n'apparaissent
        self.kills_for_boss = 10

        # Score à 0
        self.score = 0

        # Nombre de boss tués
        self.boss_killed = 0
        self.spawned_after_boss = False

        # Définition pour le timer
        self.start_time = pygame.time.get_ticks()
        # Timer de départ
        self.timer = 40

        # Lance le jeu avec un seul monstre
        self.spawn_monstre(1)



    # Fonctions


    ################## SPAWN ##################

    # Apparition du monstre
    def spawn_monstre(self, count):
        self.joueur.clear_bullets()
        for _ in range(count):
            monstre = Monstre(self)
            self.all_monstres.add(monstre)

    # Apparition du boss
    def spawn_boss(self):
        self.joueur.clear_bullets()
        boss = Boss(self)
        self.all_boss.add(boss)

    # Gestion des collisions
    def check_collision(self, element, group_element):
        return pygame.sprite.spritecollide(element, group_element, False, pygame.sprite.collide_mask)


    ######### AFFICHAGE ##########
    # Affichage du score
    def update_score(self, screen):
        font = pygame.font.SysFont("monospace", 16)
        score_text = font.render(f"Score : {self.score}", 1, (255, 255, 255))
        screen.blit(score_text, (20, 20))

    # Affichage
    def update_timer(self, screen):
        font = pygame.font.SysFont("monospace", 16)
        score_text = font.render(f"Time left : {self.timer}", 1, (255, 255, 255))
        screen.blit(score_text, (950, 20))

    # Apparition de la bombe nucléaire
    def spawn_nuclear_bomb(self):
        if not self.nuclear_bomb:
            nb = Apocalypse(self.joueur, self)
            self.nuclear_bomb.add(nb)

    # Décompte du temps
    def decompte_timer(self):
        current_time = pygame.time.get_ticks()  # Temps écoulé depuis le début du jeu en millisecondes

        if current_time - self.start_time >= 1000:  # Ajouter un délai d'une seconde
            self.start_time = current_time  # Mettre à jour le temps de référence
            if self.timer > 0:
                self.timer -= 1
            if self.timer == 0:
                self.spawn_nuclear_bomb()


    #### GAME OVER ####

    def game_over(self):
        # Permet de remettre le jeu à 0 (retirer les monstres, les hp du joueur à 100 et in_game = False)
        self.all_monstres = pygame.sprite.Group()
        self.all_boss = pygame.sprite.Group()
        self.joueur.hp = self.joueur.hp_max
        self.in_game = False
        self.game_out = True

    def you_win(self):
        # Permet de remettre le jeu à 0 (retirer les monstres, les hp du joueur à 100 et in_game = False)
        self.all_monstres = pygame.sprite.Group()
        self.all_boss = pygame.sprite.Group()
        self.joueur.hp = self.joueur.hp_max
        self.in_game = False
        self.game_out = False
        self.win = True


# Compteur permettant de faire spawn 1 monstre, puis 3, puis 6, puis 9, et enfin le boss

    def monster_killed(self):
        self.monsters_killed += 1
        if self.monsters_killed == 1:
            self.spawn_monstre(3)
        elif self.monsters_killed == 4:  # 1er monstre + 3
            self.spawn_monstre(6)
        elif self.monsters_killed == 10:  # 1er monstre + 3 + 6
            self.spawn_monstre(9)
        elif self.monsters_killed == 19:  # 1er monstre + 3 + 6 + 9
            self.spawn_boss()
        elif self.monsters_killed == 22 and self.boss_killed == 2:
            self.you_win()


    # Tuer le boss
    def kill_boss(self):  # Renommé de boss_killed à kill_boss
        self.boss_killed += 1
        if not self.spawned_after_boss:
            self.spawned_after_boss = True
            self.spawn_monstre(3)
            self.spawn_boss()
