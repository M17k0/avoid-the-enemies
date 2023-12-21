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
        if (self.direction == directions[1]): # up
            self.rect.y -= self.VELLOCITY
        elif (self.direction == directions[2]): # down
            self.rect.y += self.VELLOCITY
        elif (self.direction == directions[3]): # right
            self.rect.x += self.VELLOCITY
        elif (self.direction == directions[4]): # left
            self.rect.x -= self.VELLOCITY

    def should_remove(self):
        


        return False

    @staticmethod
    def create_enemy_by_direction(enemy_direction):
        direction = directions[enemy_direction] 
        enemy_x = enemy_y = 0

        if (direction == directions[1]): # up
            enemy_x = random.randint(0, WIDTH - Enemy.WIDTH)
            enemy_y = HEIGHT
        elif (direction == directions[2]): # down
            enemy_x = random.randint(0, WIDTH - Enemy.WIDTH)
            enemy_y = -Enemy.WIDTH
        elif (direction == directions[3]): # right
            enemy_x = -Enemy.WIDTH
            enemy_y = random.randint(0, HEIGHT - Enemy.HEIGHT)
        elif(direction == directions[4]): # left
            enemy_x = WIDTH + Enemy.WIDTH
            enemy_y = random.randint(0, HEIGHT - Enemy.HEIGHT)

        enemy = Enemy(enemy_x, enemy_y, direction)
        return enemy

    @staticmethod
    def add_enemies(enemies, time_after_last_enemy, add_enemy_after):
        for _ in range(3):
            enemy_direction = random.randint(1, 4)
            enemy = Enemy.create_enemy_by_direction(enemy_direction)
            enemies.append(enemy)

        add_enemy_after = max(200, add_enemy_after - 50)
        time_after_last_enemy = 0

        return time_after_last_enemy, add_enemy_after
    
    @staticmethod
    def move_enemies(enemies, player):
        is_hit = False
        for enemy in enemies[:]:
            enemy.update()
            
            if enemy.rect.y > HEIGHT:
                enemies.remove(enemy)
            elif enemy.rect.y + HEIGHT >= player.rect.y and enemy.rect.colliderect(player):
                enemies.remove(enemy)
                is_hit = True
                break
        
        return is_hit