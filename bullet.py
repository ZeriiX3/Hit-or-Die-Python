import pygame



# Munitions

class Bullet(pygame.sprite.Sprite):     # Munitions sans trajectoire

    def __init__(self, joueur):
        super().__init__()

        # Statistiques des munitions
        self.vitesse = 5
        # Charger l'image des munitions
        self.image = pygame.image.load("assets/bullet.png")
        self.image = pygame.transform.scale(self.image, (35, 35))
        self.rect = self.image.get_rect()
        # Positions
        self.rect.x = joueur.rect.x + 108
        self.rect.y = joueur.rect.y - 6

        self.joueur = joueur    # Pour pourvoir utiliser la class joueur dans la fonction mouvement()


    # Fonctions

    def mouvement(self):
        self.rect.x += self.vitesse
        # Si les munitions sortent de la fenêtre
        if self.rect.x > 1200:
            self.joueur.all_bullets.remove(self)
            print("La munition a été supprimé")



class Bullet_courbe(pygame.sprite.Sprite):     # Munitions avec trajectoire

    def __init__(self, joueur):
        super().__init__()

        # Statistiques des munitions
        self.vitesse = 5
        # Charger l'image des munitions
        self.image = pygame.image.load("assets/sniper_bullet.png")
        self.image = pygame.transform.scale(self.image, (35, 35))
        self.rect = self.image.get_rect()
        # Positions
        self.rect.x = joueur.rect.x + 108
        self.rect.y = joueur.rect.y - 6

        self.joueur = joueur  # Pour pourvoir utiliser la class joueur dans la fonction mouvement_courbe()


    # Fonctions

    def mouvement_courbe(self):
        self.rect.y += self.vitesse
        # Si les munitions sortent de la fenêtre
        if self.rect.x > 1200 or self.rect.y > 800:
            self.joueur.all_bullets_courbe.remove(self)
            print("La munition courbe a été supprimé")
