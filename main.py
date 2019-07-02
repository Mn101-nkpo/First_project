import pygame
import random
from pygame.locals import *

pygame.init()
screen = pygame.display.Info()
size = (width, height) = (int(screen.current_w), int(screen.current_h))
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (0, 127, 225)

sprite_image = pygame.image.load("fish.png")
sprite_image = pygame.transform.smoothscale(sprite_image, (80, 80))
sprite_rect = sprite_image.get_rect()

sprite_rect.center = (width // 2, height // 2)

speed = pygame.math.Vector2(0, 10)
rotation = random.randint(0, 0)
speed.rotate_ip(rotation)
sprite_image = pygame.transform.rotate(sprite_image, 180 - rotation)


def move_sprite():
    sprite_rect.move_ip(speed)
    global sprite_image
    screen_info = pygame.display.Info()
    sprite_rect.move_ip(speed)
    if sprite_rect.left < 0 or sprite_rect.right > screen_info.current_w:
        speed[0] *= -1
        sprite_image = pygame.transform.flip(sprite_image, True, False)
        sprite_rect.move_ip(speed[0])
    if sprite_rect < 0 or sprite_rect.bottom > screen_info.current_h:
        speed[1] *= -1
        sprite_image = pygame.transform.flip(sprite_image, False, True)
        sprite_rect.move_ip(o, speed[1])


def main():
    while True:
        clock.tick(60)
        move_sprite()
        screen.fill(color)
        screen.blit(sprite_image, sprite_rect)
        pygame.display.flip()


if __name__ == '__main__':
    main()