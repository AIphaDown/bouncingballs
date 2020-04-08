import pygame
import random
from pygame.locals import *
from ball import *

pygame.init()

screen_info = pygame.display.Info()
# screen_size = (screen_info.current_w, screen_info.current_h)

# set size
size = (width, height) = (850, 480)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (98, 26, 255)
ballAmount = random.randint(1,50)

# ball
balls = []

def main():
    for i in range(ballAmount):
        x = random.randint(50, width-50)
        y = random.randint(50, height-50)
        # balls.append(Ball((x*.5, y*.5)))
        balls.append(Ball((x, y)))
        # balls.append(Ball((width, height-50)))
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
        screen.fill(color)
        for ball in balls:
            ball.update()
        for ball in  balls:
            ball.draw(screen)
        pygame.display.flip()

if __name__ == '__main__':
    main()