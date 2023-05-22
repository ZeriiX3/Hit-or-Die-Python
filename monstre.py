################# IMPORT #################
import pygame
import random as rd
##########################################



# MONSTRES

class Monstre(pygame.sprite.Sprite):
    def __init__(self, jeu):
        super().__init__()
        self.hp = 100
        self.hp_max = 100
        self.speed = 3
        # Charger l'image des monstres + position
        self.image = pygame.image.load("images/pieuvre.png")
        self.rect = self.image.get_rect()
        # Afficher les monstres à une position aléatoire
        self.rect.x = 800 + rd.randint(-300, 300)
        self.rect.y = 190 + rd.randint(-100, 300)
        # Liste vide pour les directions aléatoires
        self.direction = []

        self.jeu = jeu  # Pour pourvoir utiliser la class jeu dans la fonction damage()


    # Fonctions

    # Affichage de la barre de vie
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


    # Perte de points de vie en fonction des dégats
    def damage(self, damage):
        self.hp -= damage

        # Si le monstre n'a plus de vie
        if self.hp <= 0:
            # Informe le jeu que le monstre a bien été tué
            self.jeu.monster_killed()
            self.kill()
            print("Vous avez tué le monstre")

            # Mise a jour du score
            self.jeu.score += 100
            self.jeu.timer += 8


    ############################# MOUVEMENT #############################


    # Focntion permettant les mouvements aléatoires du monstre
    def mouvement(self):
        if rd.random() < 0.05:  #
            self.direction = rd.choice(['up', 'down', 'left', 'right'])

        if self.direction == 'up':
            self.rect.y -= self.speed
        elif self.direction == 'down':
            self.rect.y += self.speed
        elif self.direction == 'left':
            self.rect.x -= self.speed
        elif self.direction == 'right':
            self.rect.x += self.speed

        if self.rect.x < 350:
            self.direction = rd.choice(['up', 'down', 'right'])
        elif self.rect.x > 1000 :
            self.direction = rd.choice(['up', 'down', 'left'])
        if self.rect.y < 10:
            self.direction = rd.choice(['down', 'left', 'right'])
        elif self.rect.y > 700:
            self.direction = rd.choice(['up', 'left', 'right'])


# BOSS

class Boss(pygame.sprite.Sprite):
    def __init__(self, jeu):
        super().__init__()
        self.jeu = jeu
        self.hp = 350
        self.hp_max = 350
        self.speed = 7
        self.original_speed = self.speed

        # Charger l'image des monstres + position
        self.boss_image = pygame.image.load("images/poulpe.png")
        self.boss_image_redimensionnee = pygame.transform.scale(self.boss_image, (200, 200))
        self.image = self.boss_image_redimensionnee

        # Position aléatoire du boss
        self.rect = self.image.get_rect()
        self.rect.x = 800 + rd.randint(-300, 300)
        self.rect.y = 190 + rd.randint(-100, 300)
        self.direction = []

    # Fonctions

    # Affichage de la barre de vie
    def check_hp(self, rectangle):

        # Couleur du fond de la barre de vie du monstre
        hp_bar_bg_color = (88, 24, 69)  # Gris foncé
        # Position du fond de la barre de vie
        hp_bar_bg_position = [self.rect.x - 60, self.rect.y - 15, self.hp_max, 6]
        # Afficher l'image fond de la barre de vie
        pygame.draw.rect(rectangle, hp_bar_bg_color, hp_bar_bg_position)

        # Couleur de la barre de vie du monstre
        hp_bar_color = (255, 0, 0)  # Rouge
        # Position de la barre de vie
        hp_bar_position = [self.rect.x - 60, self.rect.y - 15, self.hp, 6]
        # Afficher l'image de la barre de vie
        pygame.draw.rect(rectangle, hp_bar_color, hp_bar_position)

    # Perte de points de vie en fonction des dégats
    def damage(self, damage):
        self.hp -= damage
        # Si le boss n'a plus de points de vie
        if self.hp <= 0:
            self.jeu.kill_boss()  # Ici on appelle kill_boss au lieu de boss_killed
            self.kill()
            print("Vous avez tué le monstre")

            # Mise à jour du score
            self.jeu.score += 500
            self.jeu.timer += 12


    ############################# MOUVEMENT #############################

    # Fonction permettant les mouvements aléatoires du boss
    def mouvement(self):
        if rd.random() < 0.05:  #
            self.direction = rd.choice(['up', 'down', 'left', 'right'])

        # Permet de doubler la vitesse si les points du vie du boss atteint la moitié
        if self.hp <= self.hp_max / 2:
            self.speed = self.original_speed * 1.5

        if self.direction == 'up':
            self.rect.y -= self.speed
        elif self.direction == 'down':
            self.rect.y += self.speed
        elif self.direction == 'left':
            self.rect.x -= self.speed
        elif self.direction == 'right':
            self.rect.x += self.speed

        if self.rect.x < 350:
            self.direction = rd.choice(['up', 'down', 'right'])
        elif self.rect.x > 1000:
            self.direction = rd.choice(['up', 'down', 'left'])
        if self.rect.y < 30:
            self.direction = rd.choice(['down', 'left', 'right'])
        elif self.rect.y > 600:
            self.direction = rd.choice(['up', 'left', 'right'])
