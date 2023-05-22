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

        # Lance le jeu avec un seul monstre
        self.spawn_monstre(1)

        # Touches
        self.key_pressed = {}

        # ajoute 3 monstres une fois que tous les autres sont morts
        self.monster_multiplier = 3

        # Conteur de monstres tués
        self.monsters_killed = 0

        # Nombre de monstres tués avant que le boss n'apparaissent
        self.kills_for_boss = 10

        # Score à 0
        self.score = 0

        self.boss_killed = 0
        self.spawned_after_boss = False

        self.start_time = pygame.time.get_ticks()
        self.timer = 40



    # Fonctions

    def spawn_monstre(self, count):
        self.joueur.clear_bullets()
        for _ in range(count):
            monstre = Monstre(self)
            self.all_monstres.add(monstre)

    def spawn_boss(self):
        self.joueur.clear_bullets()
        boss = Boss(self)
        self.all_boss.add(boss)

    # Gestion des collisions
    def check_collision(self, element, group_element):
        return pygame.sprite.spritecollide(element, group_element, False, pygame.sprite.collide_mask)

    # Affichage du score
    def update_score(self, screen):
        font = pygame.font.SysFont("monospace", 16)
        score_text = font.render(f"Score : {self.score}", 1, (255, 255, 255))
        screen.blit(score_text, (20, 20))

    def update_timer(self, screen):
        font = pygame.font.SysFont("monospace", 16)
        score_text = font.render(f"Time left : {self.timer}", 1, (255, 255, 255))
        screen.blit(score_text, (950, 20))

    def decompte_timer(self):
        current_time = pygame.time.get_ticks()  # Temps écoulé depuis le début du jeu en millisecondes

        if current_time - self.start_time >= 1000:  # Ajouter un délai d'une seconde
            self.start_time = current_time  # Mettre à jour le temps de référence
            if self.timer > 0:
                self.timer -= 1
            else:
                print("Time's up!")

# Conteur permettant de faire spawn 1 monstre, puis 3, puis 6, puis 9, et enfin le boss

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



    def kill_boss(self):  # Renommé de boss_killed à kill_boss
        self.boss_killed += 1
        if not self.spawned_after_boss:
            self.spawned_after_boss = True
            self.spawn_monstre(3)
            self.spawn_boss()
