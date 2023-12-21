import pygame
import time

from src.player import Player
from src.enemy import Enemy
from src.config import WIDTH, HEIGHT, GAME_NAME

pygame.init()
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(GAME_NAME)

BACKGROUND = pygame.image.load("./assets/background.png")
FONT = pygame.font.SysFont("arial", 30)

def draw(player, elapsed_time, enemies):
    WINDOW.blit(BACKGROUND, (0, 0))

    time_text = FONT.render(f"Time:{round(elapsed_time)}s", 1, "white")
    WINDOW.blit(time_text, (10, 10))

    pygame.draw.rect(WINDOW, "red", player)

    for enemy in enemies:
        pygame.draw.rect(WINDOW, "white", enemy)

    pygame.display.update()

def main():
    run = True
    player = Player()

    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    add_enemy_after = 2000 # miliseconds
    time_after_last_enemy = 0
    enemies = []
    hit = False

    while run:
        # clock tick - returns milisocends since the last tick
        time_after_last_enemy += clock.tick(60)
        elapsed_time = time.time() - start_time

        # Add enemies
        if time_after_last_enemy > add_enemy_after:
            time_after_last_enemy, add_enemy_after = Enemy.add_enemies(enemies, time_after_last_enemy, add_enemy_after)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        keys = pygame.key.get_pressed()
        player.handle_movement(keys)

        hit = Enemy.move_enemies(enemies, player)

        if hit:
            text = FONT.render("You lose", 1, (0, 0, 0))
            WINDOW.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
            pygame.display.update()
            pygame.time.delay(5_000)
            break

        draw(player, elapsed_time, enemies)

    pygame.quit()

if __name__ == "__main__":
    main()