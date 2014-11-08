import pygame

HEIGHT = 600
WIDTH = 800
HEIGHT_PRINCESS = 60
WIDTH_PRINCESS = 28

def main():
    world = pygame.Rect((0, 0), (WIDTH, HEIGHT))
    princess = pygame.Rect((0, HEIGHT / 2), (WIDTH_PRINCESS, HEIGHT_PRINCESS))
   
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(world.size)

    screen = pygame.display.set_mode(world.size)
    princess = pygame.image.load("img/princess/2.png").convert()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
        screen.blit(princess, (0, 0))
        pygame.display.flip()
    return

main()