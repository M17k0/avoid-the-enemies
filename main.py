import pygame
import time
import random

pygame.init()
WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Avoid the enemies")

BACKGROUND = pygame.image.load("./assets/background.png")

PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_VEL = 5

def draw(player):
    WIN.blit(BACKGROUND, (0, 0))

    pygame.draw.rect(WIN, (255, 0, 0), player)

    pygame.display.update()

def main():
    run = True

    player = pygame.Rect(WIDTH // 2, HEIGHT // 2, PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock()

    while run:
        clock.tick(60) # delay the while loop to run maximum 60fps

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

        draw(player)

    pygame.quit()

if __name__ == "__main__":
    main()