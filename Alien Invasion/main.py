import sys
import pygame
import time

from settings import Settings
from ship import Ship
from bullet import Bullet
from game_stat import GameStats



class alienInvasion:
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")


        # Create  an instance to store game statistics
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._fire = False
        self.bullets.lastShoot = 0
        
    # self._create_fleet()

    
    def runGame(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                # self._update_aliens()

            self._update_screen()

            # Make the most recently drawn screen visible.
            pygame.display.flip()

    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        pass

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # self.aliens.draw(self.screen)

        if not self.stats.game_active:
            # self.play_button.draw(self.screen)
            pass

        pygame.display.flip()

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire = True
            self._fire_bullet()

    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_SPACE:
            self._fire_ = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullet group."""
        currentTime = time.time()
        if self._fire and currentTime - self.bullets.lastShoot > float(self.settings.bullet_delay/1000) and len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.bullets.lastShoot = time.time()
            print(self.settings.bullet_delay)
            print(self.bullets.lastShoot)
            if self._fire:
                self._fire_bullet()
                print(currentTime)
                print(self._fire)

            
            
            

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet pos
        self.bullets.update()

        #Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions"""
        #Remove bullet and alien after hit
        collisions = pygame.sprite.groupcollide(seld.bullet, self.aliens, True, True)

        if not self.aliens:
            #Destroy existing bullets and create new fleet.
            self.bullets.empty()
            # self._create_fleet()
            self.settings.increase_speed()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = alienInvasion()
    ai.runGame()