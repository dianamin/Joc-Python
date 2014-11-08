import pygame

HEIGHT = 480
WIDTH = 800
HEIGHT_PRINCESS = 60
WIDTH_PRINCESS = 28

n = 10
height = []
rect_width = 80

random = 0

def initHeights():
    from random import randint
    for i in range(0, n):
        height.append(randint(100, 300))
        print height[i]
    return
    

def init():
    initHeights()
    return


def main():

    init()

    world = pygame.Rect((0, 0), (WIDTH, HEIGHT))
    world_image = pygame.Surface((WIDTH, HEIGHT), depth = 24)
    princess = pygame.Rect((0, HEIGHT / 2), (WIDTH_PRINCESS, HEIGHT_PRINCESS))
    
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(world.size)

    screen = pygame.display.set_mode(world.size)
    background = pygame.image.load("img/background/back1.png").convert()

    princess_image = pygame.image.load("img/princess/2.png").convert()
    
    #princess_image = princess_image

    # pixdata = princess_image.load()

    # for y in xrange(princess_image.size[1]):
    #     for x in xrange(princess_image.size[0]):
    #         if pixdata[x, y] == (255, 255, 255, 255):
    #             pixdata[x, y] = (255, 255, 255, 0)

    # princess_image = princess_image.convert()

    vx = 10;

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_DOWN]:
            princess.move_ip(0, 20)
        if pressed[pygame.K_UP]:
            princess.move_ip(0, -20)
        if pressed[pygame.K_RIGHT]:
            princess.move_ip(20, 0)
        if pressed[pygame.K_LEFT]:
            princess.move_ip(-20, 0)

        princess.clamp_ip(world)


        #key = (0,255,0)
        #world_image.fill(world_image.get_rect(), key)
        #world_image.set_colorkey(key)
        #world_image.blit(image, (0,0))


        world_image.set_alpha(128) 

        world_image.blit(background, (0, 0))
        world_image.blit(princess_image, princess.center)
        screen.blit(world_image, (0, 0))    
        for i in range(0, n):
            pygame.draw.rect(screen, pygame.Color('red'), (i * rect_width, HEIGHT - height[i], rect_width, height[i]))
        pygame.display.flip()
        clock.tick (30)
    return

main()