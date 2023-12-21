import pygame

from .config import HEIGHT, WIDTH

class Player:
    PLAYER_WIDTH = 50
    PLAYER_HEIGHT = 50
    PLAYER_VELLOCITY = 5

    def __init__(self):
        self.image = pygame.image.load("./assets/player.jpg")
        self.image = pygame.transform.scale(self.image, (self.PLAYER_WIDTH, self.PLAYER_HEIGHT))
        self.rect = self.image.get_rect(center=(WIDTH / 2, HEIGHT / 2))

    def handle_movement(self, keys):
        if keys[pygame.K_LEFT] and self.rect.x - self.PLAYER_VELLOCITY >= 0:
            self.rect.x -= self.PLAYER_VELLOCITY
        if keys[pygame.K_RIGHT] and self.rect.x + self.PLAYER_VELLOCITY + self.rect.width <= WIDTH:
            self.rect.x += self.PLAYER_VELLOCITY
        if keys[pygame.K_UP] and self.rect.y - self.PLAYER_VELLOCITY >= 0:
            self.rect.y -= self.PLAYER_VELLOCITY
        if keys[pygame.K_DOWN] and self.rect.y + self.PLAYER_VELLOCITY + self.rect.height <= HEIGHT:
            self.rect.y += self.PLAYER_VELLOCITY

    def draw_player(self, screen):  
        screen.blit(self.image, self.rect)