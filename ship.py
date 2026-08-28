import pygame
from settings import Settings
class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load("images/ship.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.move_direction = 0
        self.settings=Settings()
        
    def blitme(self):
        if (self.rect.right < self.screen_rect.right and self.move_direction == 1) or (self.rect.left > self.screen_rect.left and self.move_direction == -1):
            self.rect.x += self.move_direction * self.settings.ship_speed 
        self.screen.blit(self.image, self.rect)
