import pygame
import math
import time


HEIGHT = 480
WIDTH = 800
HEIGHT_PRINCESS = 60
WIDTH_PRINCESS = 28

DOWN = 1
RIGHT = 3
LEFT = 4

n = 100
heart = 5

height = []
treasure = []
monster = []
rect_width = 80

random = 0
score = 0


world = pygame.Rect((0, 0), (WIDTH, HEIGHT))
world_image = pygame.Surface((WIDTH, HEIGHT), depth = 24)
princess = pygame.Rect((0, 0), (WIDTH_PRINCESS, HEIGHT_PRINCESS))

clock = pygame.time.Clock()
screen = pygame.display.set_mode(world.size)

screen = pygame.display.set_mode(world.size)
background = pygame.image.load("img/background/back1.png").convert()

princess_image_right = pygame.image.load("img/princess/3.png").convert()
princess_image_left = pygame.image.load("img/princess/4.png").convert()
princess_image_front = pygame.image.load("img/princess/2.png").convert()
princess_image = pygame.image.load("img/princess/2.png").convert()
block = pygame.image.load("img/blocks/block.png").convert()
monster_image = pygame.image.load("img/monster/monster.png").convert()
treasure_image = pygame.image.load("img/blocks/treasure.png").convert()
heart_image = pygame.image.load("img/hearts/heart.png").convert()

begin = pygame.image.load("img/other/begin.png").convert()
end = pygame.image.load("img/other/end.png").convert()

done = False

def init():
    from random import randint
    for i in range(0, n):
        height.append(randint(1, 3) * 80)
        treasure.append(randint(0, 1))
        monster.append(randint(0, 6 ))
    height.append(0)
    monster[0] = 0
    return

def ok(directie, first_block):
    current_block = int(math.floor(princess.right / 80) + first_block)
    if monster[current_block] == 1 and princess.top >= HEIGHT - height[current_block]:
        global score
        score -= 5
        monster[current_block] = 0
        global heart
        heart -= 1
        if heart == 0:
            done = True
        return False
    if directie == DOWN:
        if princess.bottom < HEIGHT - height[current_block]:
            return True 
        return False
    if directie == RIGHT:
        if treasure[current_block] == 1 and princess.top >= HEIGHT - height[current_block]:
            global score
            score += 10
            treasure[current_block] = 0
            return True
        if princess.top < HEIGHT - height[current_block]:
            return True
        return False
    if directie == LEFT:
        current_block -= 1
        if treasure[current_block] == 1 and princess.top >= HEIGHT - height[current_block]:
            global score
            score += 10
            treasure[current_block] = 0
            return True
        if princess.top < HEIGHT - height[current_block]:
            return True
        return False
    return

def draw_blocks(first_block):
    #if ok(RIGHT, first_block) == False:
    #    return
    for i in range(first_block, n):
        nr = height[i] / 80
        for j in range(0, nr):
            world_image.blit(block, (80 * (i - first_block), HEIGHT - 80 * (j + 1)))
        if treasure[i] == 1:
            world_image.blit(treasure_image, (80 * (i - first_block), HEIGHT - 80 * nr))
        if monster[i] == 1:
            world_image.blit(monster_image, (80 * (i - first_block), HEIGHT - 80 * nr))
    return

def show_life():
    heart_width = 25
    for i in range(heart):
        screen.blit(heart_image, (WIDTH - (i + 1) * heart_width, 0))
    return

def main():

    init()
    pygame.font.init()
    font = pygame.font.SysFont(pygame.font.get_default_font(), 28)
    
    x = 0
    vx = 10
    first_block = 0
    jumping = False
    jumped = 0
    falling = True
    jumping_speed = 20

    screen.blit(begin, (0, 0))
    pygame.display.flip()
    time.sleep(3)
    global done
    while done == False:
        princess_image = princess_image_front
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_DOWN]:
            if ok(DOWN, first_block) == True:
                princess.move_ip(0, 20)
        if pressed[pygame.K_UP]:
            if jumping == False:
                jumping = True
                jumped = 0
        if pressed[pygame.K_RIGHT]:
            princess_image = princess_image_right
            if ok(RIGHT, first_block) == True:
                princess.move_ip(20, 0)
        if pressed[pygame.K_LEFT]:
            if ok(LEFT, first_block) == True:
                princess_image = princess_image_left
            princess.move_ip(-20, 0)

        princess.clamp_ip(world)

        if jumping == True:
            princess.move_ip(0, -jumping_speed)
            jumped += jumping_speed
        if jumped == 140:
            falling = True
            jumping = False
        if falling == True and jumping == False:
            if (ok(DOWN, first_block)):
                princess.move_ip(0, jumping_speed)
                jumped -= jumping_speed

        world_image.set_alpha(128) 
        world_image.blit(background, (0, 0))
        world_image.blit(princess_image, (princess.left, princess.top))
        x += 1
        if x == 20:
            first_block += 1
            x = 0
        draw_blocks(first_block)
        screen.blit(world_image, (0, 0))
        if first_block == 90:
            done = True
        text = font.render("score: %d" % score, True, pygame.Color('black'))
        screen.blit(text, (0, 0))
        show_life()
        pygame.display.flip()
        clock.tick (30)
        global heart
        if heart == 0:
            done = True

    text = font.render("score: %d" % score, True, pygame.Color('black'))
    screen.blit(end, (0,0))
    screen.blit(text, (0, 0))
    pygame.display.flip()
    time.sleep(3)
    return

main()