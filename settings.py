import pygame
class Settings():
    def __init__(self):
        self.bg_color=(117, 33, 255)
        self.screen_width=None
        self.screen_height=None
        self.bullet_color=( 104 , 212 , 0 )
        self.bullet_width=20
        self.bullet_height=20
        self.num_aliens=11
        self.alien_speed=0.4
        self.bullet_speed=7
        self.button_height=60
        self.button_width=250
        self.btn_play_color = (255, 0, 3)
        self.btn_play_text_color=(255,255,255)
        self.border_color=(139, 28, 0)
        self.ship_speed=5
        self.loose_sound = pygame.mixer.Sound("sounds/Game-Over.ogg")
        self.loose_sound.set_volume(0.8)
        self.attack_sound = pygame.mixer.Sound("sounds/alert.ogg")
        self.attack_sound.set_volume(0.5)
        self.wall_sound = pygame.mixer.Sound("sounds/wall.ogg")
        self.wall_sound.set_volume(0.2)
        
        
