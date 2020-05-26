import pygame 
import time
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class to manage bullets fired from the ship"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0,0) and then set correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        self.shoot_date = time.time()

        #Store the bullet's position as a decimal value
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen"""
        # Update the decimal pos
        self.y -= self.settings.bullet_speed

        # Update the rect pos
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)