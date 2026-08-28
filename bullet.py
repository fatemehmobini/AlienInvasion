import pygame 
class Bullet(pygame.sprite.Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.bullet_color=self.settings.bullet_color
        self.rect=pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.shoot_sound=pygame.mixer.Sound("sounds/shield.ogg")
        self.shoot_sound.set_volume(0.5)
        self.rect.midtop=ai_game.ship.rect.midtop
        self.in_screen=True
        self.shoot_sound.play()
        
    def update(self):
        self.rect.y-=self.settings.bullet_speed

    def draw_bullet(self):
        if self.rect.y<-self.settings.bullet_height:
            self.in_screen=False
        self.update()
        pygame.draw.ellipse(self.screen,self.bullet_color,self.rect)
        


