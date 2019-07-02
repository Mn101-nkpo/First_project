from pygame.local import*

pygame.init()
screen = pygame.display.imfo()
size = (width,height) = (int(screen.current_w),int(screen.current_h))
screen = pygame.display.set_mode_size
clock = pygame.time.Clock()
color = (0, 127, 225)
def main():
    while True:
        clock.tick(60)
        screen.fill(color)
        pygame.display.flip()

if __name__ == '__main__':
