import pygame
import random

from .config import WIDTH, HEIGHT

directions = {1: "up", 2: "down", 3: "right", 4: "left"}

class Enemy:
    WIDTH = 25
    HEIGHT = 25
    VELLOCITY = 5

    def __init__(self, x, y, direction="down"):
        self.rect = pygame.Rect(x, y, self.WIDTH, self.HEIGHT)
        self.direction = direction

    def update(self):
        if (self.direction == "up"):
            self.rect.y -= self.VELLOCITY
        elif (self.direction == "down"):
            self.rect.y += self.VELLOCITY
        elif (self.direction == "right"):
            self.rect.x += self.VELLOCITY
        elif (self.direction == "left"):
            self.rect.x -= self.VELLOCITY

    def should_remove(self):
        if (self.direction == "up"):
            if self.rect.y < 0:
                return True
        elif (self.direction == "down"):
            if self.rect.y > HEIGHT:
                return True
        elif (self.direction == "right"):
            if self.rect.x > WIDTH:
                return True
        elif (self.direction == "left"):
            if self.rect.x < 0:
                return True

        return False

    def hit_player(self, player):
        return self.rect.colliderect(player.rect)

    @staticmethod
    def create_enemy_by_direction(enemy_direction):
        direction = directions[enemy_direction] 
        enemy_x = enemy_y = 0

        if (direction == "up"):
            enemy_x = random.randint(0, WIDTH - Enemy.WIDTH)
            enemy_y = HEIGHT
        elif (direction == "down"):
            enemy_x = random.randint(0, WIDTH - Enemy.WIDTH)
            enemy_y = -Enemy.WIDTH
        elif (direction == "right"):
            enemy_x = -Enemy.WIDTH
            enemy_y = random.randint(0, HEIGHT - Enemy.HEIGHT)
        elif(direction == "left"):
            enemy_x = WIDTH + Enemy.WIDTH
            enemy_y = random.randint(0, HEIGHT - Enemy.HEIGHT)

        enemy = Enemy(enemy_x, enemy_y, direction)
        return enemy

    @staticmethod
    def add_enemies(enemies):
        for _ in range(3):
            enemy_direction = random.randint(1, 4)
            enemy = Enemy.create_enemy_by_direction(enemy_direction)
            enemies.append(enemy)
    
    @staticmethod
    def move_enemies(enemies, player):
        is_hit = False
        for enemy in enemies[:]:
            enemy.update()
            
            if (enemy.should_remove()):
                enemies.remove(enemy)

            if (enemy.hit_player(player)):
                enemies.remove(enemy)
                is_hit = True
                break
        
        return is_hit
    
    def draw_enemy(self, screen):
        pygame.draw.rect(screen, "black", self.rect)