import pygame
class Scoreboard:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.text_color =(255,255,255)
        self.font = pygame.font.SysFont(None, 48)
        self.hearts = []  
        self.heart_image = None 
        self.score_image = None
        self.score_rect = pygame.Rect(0, 0, 0, 0)

    def prep_score(self, score):
        score_str = f"score: {score}"
        self.score_image = self.font.render(score_str, False, self.text_color,(255,0,0))
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 35
        self.score_rect.top = 30

    def prep_hearts(self, heart_image_path):
        self.heart_image = pygame.image.load(heart_image_path)
        self.heart_image = pygame.transform.scale(self.heart_image, (30, 30))
        self.hearts = []  
        for i in range(3):  
            rect = self.heart_image.get_rect()
            rect.top = 80  
            rect.right = self.screen_rect.right - (40 + i * (rect.width + 10))  
            self.hearts.append(rect)

    def update_hearts(self, missed_aliens):
        if missed_aliens <= len(self.hearts):  
            del self.hearts[-1] 

    def show_score(self, score):
        self.prep_score(score)
        self.screen.blit(self.score_image, self.score_rect)
        for rect in self.hearts:
            self.screen.blit(self.heart_image, rect)
 
