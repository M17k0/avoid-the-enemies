import pygame
import time

from src.player import Player
from src.enemy import Enemy
from src.config import WIDTH, HEIGHT, GAME_NAME, FPS
from src.config import BACKGROUND_IMAGE, MUSIC

pygame.init()
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(GAME_NAME)

BACKGROUND = pygame.image.load(BACKGROUND_IMAGE)
FONT = pygame.font.SysFont("arial", 30)

pygame.mixer.music.load(MUSIC)
pygame.mixer.music.play(loops=-1, start=0)

def draw(player, elapsed_time, enemies):
    WINDOW.blit(BACKGROUND, (0, 0))

    time_text = FONT.render(f"Time:{round(elapsed_time)}s", 1, "white")
    WINDOW.blit(time_text, (10, 10))

    player.draw_player(WINDOW)

    for enemy in enemies:
        enemy.draw_enemy(WINDOW)

    pygame.display.update()

def main():
    run = True
    player = Player()

    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    add_enemy_after = 2000
    time_after_last_enemy = 0
    enemies = []
    hit = False

    time_to_speed_up = 0
    while run:
        milliseconds = clock.tick(FPS)
        time_after_last_enemy += milliseconds
        time_to_speed_up += milliseconds

        elapsed_time = time.time() - start_time

        if time_to_speed_up >= 15_000:
            player.speed_up()
            time_to_speed_up = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        player.handle_movement(keys)

        if time_after_last_enemy > add_enemy_after:
            Enemy.add_enemies(enemies)
            time_after_last_enemy = 0
            add_enemy_after = max(350, add_enemy_after - 50)

        hit = Enemy.move_enemies(enemies, player)

        if hit:
            text = FONT.render("You lose", 1, "white")
            WINDOW.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
            pygame.display.update()
            pygame.time.delay(5_000)
            break

        draw(player, elapsed_time, enemies)

    pygame.quit()

if __name__ == "__main__":
    main()