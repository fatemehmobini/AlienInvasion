import pygame
from pygame.sprite import Sprite
import random  
class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.images = ["images/alien1.png","images/alien2.png","images/alien3.png","images/alien4 .png","images/alien5.png"]
        selected_image = random.choice(self.images)
        self.image = pygame.image.load(selected_image)
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = ai_game.last_alien_x
        ai_game.last_alien_x += (self.rect.width + 20)
        self.rect.y = 20
        self.position = 0
        self.in_screen = True

    def blitme(self):
        if self.rect.y > self.settings.screen_height:
            self.in_screen = False
        self.position += self.settings.alien_speed
        self.rect.y = self.position
        self.screen.blit(self.image, self.rect)
        


