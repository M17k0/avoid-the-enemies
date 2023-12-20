import pygame
import time
import random
pygame.font.init() # initialize the FONT

pygame.init()
WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Avoid the enemies")

BACKGROUND = pygame.image.load("./assets/background.png")

PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_VEL = 5

ENEMY_WIDTH = 25
ENEMY_HEIGHT = 25
ENEMY_VEL = 5

FONT = pygame.font.SysFont("arial", 30)

def draw(player, elapsed_time, enemies):
    WIN.blit(BACKGROUND, (0, 0))

    time_text = FONT.render(f"Time:{round(elapsed_time)}s", 1, (0, 0, 0))
    WIN.blit(time_text, (10, 10))

    pygame.draw.rect(WIN, (255, 0, 0), player)

    for enemy in enemies:
        pygame.draw.rect(WIN, (255, 255, 255), enemy)

    pygame.display.update()

def main():
    run = True

    player = pygame.Rect(WIDTH / 2 - PLAYER_WIDTH / 2, HEIGHT / 2 - PLAYER_HEIGHT / 2, PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    enemy_add_increment = 2000 # miliseconds
    enemy_count = 0
    enemies = []
    hit = False

    while run:
        # clock tick - return miliseconds since the last clock tick
        enemy_count += clock.tick(60) # delay the while loop to run maximum 60fps
        elapsed_time = time.time() - start_time

        # add enemies
        if enemy_count > enemy_add_increment:
            for _ in range(3):
                enemy_x = random.randint(0, WIDTH - ENEMY_WIDTH)
                enemy = pygame.Rect(enemy_x, -ENEMY_HEIGHT, ENEMY_WIDTH, ENEMY_HEIGHT)
                enemies.append(enemy)
            
            enemy_add_increment = max(200, enemy_add_increment - 50)
            enemy_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= (PLAYER_VEL)
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL
        if keys[pygame.K_UP] and player.y - PLAYER_VEL >= 0:
            player.y -= PLAYER_VEL
        if keys[pygame.K_DOWN] and player.y + PLAYER_VEL + player.height <= HEIGHT:
            player.y += PLAYER_VEL

        for enemy in enemies[:]:
            enemy.y += ENEMY_VEL
            if enemy.y > HEIGHT:
                enemies.remove(enemy)
            elif enemy.y + enemy.height >= player.y and enemy. colliderect(player):
                enemies.remove(enemy)
                hit = True
                break

        if hit:
            text = FONT.render("You lose", 1, (0, 0, 0))
            WIN.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
            pygame.display.update()
            pygame.time.delay(5_000)
            break

        draw(player, elapsed_time, enemies)

    pygame.quit()

if __name__ == "__main__":
    main()