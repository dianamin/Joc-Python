import pygame
import math

HEIGHT = 480
WIDTH = 800
HEIGHT_PRINCESS = 60
WIDTH_PRINCESS = 28

DOWN = 1

n = 100

height = []
treasure = []
rect_width = 80

random = 0


world = pygame.Rect((0, 0), (WIDTH, HEIGHT))
world_image = pygame.Surface((WIDTH, HEIGHT), depth = 24)
princess = pygame.Rect((0, HEIGHT / 2), (WIDTH_PRINCESS, HEIGHT_PRINCESS))

clock = pygame.time.Clock()
screen = pygame.display.set_mode(world.size)

screen = pygame.display.set_mode(world.size)
background = pygame.image.load("img/background/back1.png").convert()

princess_image = pygame.image.load("img/princess/2.png").convert()
block = pygame.image.load("img/blocks/block.png").convert()
treasure_image = pygame.image.load("img/blocks/treasure.png").convert()


def initHeights():
    from random import randint
    for i in range(0, n):
        height.append(randint(1, 3) * 80)
        treasure.append(randint(0, 1))
       # print str(height[i]) + " " + str(treasure[i])
    height.append(0)
    return
    

def init():
    initHeights()
    return

def draw_blocks(first_block):
    for i in range(first_block, n):
        nr = height[i] / 80
        for j in range(0, nr):
            world_image.blit(block, (80 * (i - first_block), HEIGHT - 80 * (j + 1)))
        if treasure[i] == 1:
            world_image.blit(treasure_image, (80 * (i - first_block), HEIGHT - 80 * nr))
            #pygame.draw.rect(screen, pygame.Color('red'), (i * rect_width, HEIGHT - height[i], rect_width, height[i]))
    return


def ok(directie, first_block):
    if directie == DOWN:
        current_block = int(math.floor(princess.right / 80) + first_block)
        print current_block
        if princess.bottom < HEIGHT - height[current_block]:
            return True 
    return False



def main():

    init()
    
    #princess_image = princess_image

    # pixdata = princess_image.load()

    # for y in xrange(princess_image.size[1]):
    #     for x in xrange(princess_image.size[0]):
    #         if pixdata[x, y] == (255, 255, 255, 255):
    #             pixdata[x, y] = (255, 255, 255, 0)

    # princess_image = princess_image.convert()
    x = 0
    vx = 10
    first_block = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_DOWN]:
            if ok(DOWN, first_block) == True:
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
        world_image.blit(princess_image, (princess.left, princess.top))
        x += 1
        if x == 40:
            first_block += 1
            x = 0
        draw_blocks(first_block)
        screen.blit(world_image, (0, 0)) 
        pygame.display.flip()
        clock.tick (30)
    return

main()