import pygame

HEIGHT = 480
WIDTH = 800
HEIGHT_PRINCESS = 60
WIDTH_PRINCESS = 28

def main():
    world = pygame.Rect((0, 0), (WIDTH, HEIGHT))
    princess = pygame.Rect((0, HEIGHT / 2), (WIDTH_PRINCESS, HEIGHT_PRINCESS))
   
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(world.size)

    screen = pygame.display.set_mode(world.size)
    princess_image = pygame.image.load("img/princess/2.png").convert()
    background = pygame.image.load("img/background/back1.png").convert()
 
    vx = 10;

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_DOWN]:
            princess.move_ip(0, 10)
        if pressed[pygame.K_UP]:
            princess.move_ip(0, -10)
        if pressed[pygame.K_RIGHT]:
            princess.move_ip(10, 0)
        if pressed[pygame.K_LEFT]:
            princess.move_ip(-10, 0)

        princess.clamp_ip(world)


        screen.blit(background, (0, 0))
        screen.blit(princess_image, princess.center)
        pygame.display.flip()
        clock.tick (30)
    return

main()