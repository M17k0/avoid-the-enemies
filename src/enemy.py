import pygame
import random

from .config import WIDTH, HEIGHT

class Enemy:
    WIDTH = 25
    HEIGHT = 25
    VELLOCITY = 5

    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, self.WIDTH, self.HEIGHT)

    def update(self, direction):
        self.rect.y += self.VELLOCITY

    @staticmethod
    def add_enemies(enemies, time_after_last_enemy, add_enemy_after):
        for _ in range(3):
            enemy_x = random.randint(0, WIDTH - Enemy.WIDTH)
            enemy = pygame.Rect(enemy_x, -Enemy.HEIGHT, Enemy.WIDTH, Enemy.HEIGHT)
            enemies.append(enemy)

        add_enemy_after = max(200, add_enemy_after - 50)
        time_after_last_enemy = 0

        return time_after_last_enemy, add_enemy_after