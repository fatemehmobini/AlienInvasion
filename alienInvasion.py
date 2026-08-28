import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button
from scoreboard import Scoreboard
class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.bg_color =self.settings.bg_color
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Alien Invasion")
        self.settings=Settings()
        self.settings.screen_width = self.screen.get_width()
        self.settings.screen_height = self.screen.get_height()
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.alien_list = pygame.sprite.Group()
        self.btn_play = Button(self, "Play Game ",position_offset=100)
        self.btn_highscore = Button(self, "High Score", position_offset=300)
        self.show_highscore_button = False
        self.btn_exit = Button(self, "Exit", position_offset=200)   
        self.active_game = False
        self.highest_score = 0  
        self.missed_aliens = 0
        self.score_board = Scoreboard(self)
        self.num_of_shoot_alien = 0
        self.score_board.prep_hearts("images/heartt.png")
        self.show_title = True
        self.show_image = True  
        self.image = pygame.image.load("images/logo.png")  
        self.image = pygame.transform.scale(self.image, (360,490))  
        self.image_rect = self.image.get_rect()
        self.image_rect.center = (self.settings.screen_width // 2, 400)
        self.played_loose_sound = False
        

    def populate_fleet(self):
        self.last_alien_x = 200
        self.last_alien_y = 20
        for index in range(self.settings.num_aliens):
            self.alien_list.add(Alien(self))

    def _reset_game(self):
        self.active_game = True
        self.missed_aliens = 0
        self.num_of_shoot_alien = 0
        self.bullets.empty()
        self.alien_list.empty()
        self.populate_fleet()
        self.score_board.prep_hearts("images/heartt.png")
        self.show_highscore_button = False
        self.btn_play._prep_msg("Play Game :)")
        self.btn_play.button_color = (255, 0, 174)
        self.btn_play.text_color = (0, 255, 204)
        self.settings.loose_sound.stop()
        self.settings.wall_sound.stop() 
        self.settings.wall_sound.play()
        self.played_loose_sound = False

    def _check_play_button(self, mouse_pos):
        if self.btn_play.rect.collidepoint(mouse_pos):
            self.show_image=False
            if not self.active_game:
                self._reset_game()
                self.show_title = False
            return True
        return False


    def _check_highscore_button(self, mouse_pos):
        if self.btn_highscore.rect.collidepoint(mouse_pos):
            self.show_highscore()
            self.show_title = False 
            return True
        return False


    def show_highscore(self):
        self.screen.fill(self.bg_color) 
        font = pygame.font.SysFont(None, 48)
        title = font.render("High Score:", True, ((255, 255, 255)))
        self.screen.blit(title, (self.settings.screen_width // 2 - title.get_width() // 2, 100))
        score_text = font.render(f"{self.highest_score}", True, (255, 255, 255))
        self.screen.blit(score_text, (self.settings.screen_width // 2 - score_text.get_width() // 2, 150))
        pygame.display.flip()
        pygame.time.wait(2000)  


    def draw_title(self):
        if self.show_title:
            font = pygame.font.SysFont(None, 48)
            title = font.render("Alien Invasion", False,( 255,255,255 ))  
            title_rect = title.get_rect(center=(self.settings.screen_width // 2, 30))
            self.screen.blit(title, title_rect)
            
    def draw_image(self):
        if self.show_image:
            self.screen.blit(self.image, self.image_rect)

    def _check_exit_button(self, mouse_pos):
        if self.btn_exit.rect.collidepoint(mouse_pos):
            sys.exit()
            
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.ship.move_direction = 1
                    elif event.key == pygame.K_LEFT:
                        self.ship.move_direction = -1
                    elif event.key == pygame.K_ESCAPE:
                        sys.exit()
                    elif event.key == pygame.K_SPACE:
                        if len(self.bullets) < 8:
                            self.bullets.add(Bullet(self))
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self._check_play_button(mouse_pos):
                        self.active_game = True
                        self.settings.wall_sound.play()
                    elif self._check_highscore_button(mouse_pos):
                        pass
                    elif self._check_exit_button(mouse_pos):  
                        pass
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.ship.move_direction = 0
                    elif event.key == pygame.K_LEFT:
                        self.ship.move_direction = 0
            self.screen.fill(self.settings.bg_color)
            self.draw_image() 
            self.draw_title()
            if self.active_game:
                collide_dict = pygame.sprite.groupcollide(self.bullets, self.alien_list, True, True)
                self.num_of_shoot_alien += len(collide_dict)
                for alien in collide_dict:
                    self.settings.attack_sound.play()
                for alien in self.alien_list.sprites():
                    if not alien.in_screen:
                        self.missed_aliens += 1
                        self.alien_list.remove(alien)
                        self.score_board.update_hearts(self.missed_aliens)  
                    alien.blitme()
                for bullet in self.bullets.sprites():
                    if bullet.in_screen:
                        bullet.draw_bullet()
                    else:
                        self.bullets.remove(bullet)
                self.ship.blitme()
                if len(self.alien_list) <= 9:
                    self.populate_fleet()
                self.score_board.show_score(self.num_of_shoot_alien) 
            else:
                self.btn_play.draw_button()
                if self.show_highscore_button:
                    self.btn_highscore.draw_button()
                self.btn_exit.draw_button()
            if self.missed_aliens >= 3:
                self.active_game = False
                if not self.played_loose_sound:
                    self.settings.loose_sound.play()
                    self.played_loose_sound = True
                self.settings.wall_sound.stop()
                self.show_highscore_button = True
                if self.num_of_shoot_alien > self.highest_score: 
                    self.highest_score = self.num_of_shoot_alien  
                self.btn_play.button_color =self.settings.btn_play_color 
                self.btn_play.text_color =self.settings.btn_play_text_color
                self.btn_play.border_color =self.settings.border_color
                self.btn_play._prep_msg("Play Again")
                self.btn_exit._prep_msg("Exit Game")
                self.image = pygame.image.load("images/logo2.png") 
                self.image = pygame.transform.scale(self.image, (350,480))  
                self.show_image=True
                self.draw_image()

            pygame.display.flip()
ai_game = AlienInvasion()
ai_game.run_game()
