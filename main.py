#модули
from random import randint as rand
import pygame
import water
import calcite
pygame.init()

#НАСТРОЙКА

keep_going = True
pause = [False]
render_brain = [False]
mouse = ["set"]
botcode = [None]
bots = [0]
white = (255, 255, 255)
grey = (90, 90, 90)

W = pygame.display.Info().current_w
H = pygame.display.Info().current_h
#W = 900#для отладки
#H = 900
screen = pygame.display.set_mode([W, H])
description = "Cyber Biology 3"
pygame.display.set_caption(description)
objects = pygame.sprite.Group()
world_scale = [
    int((W - 300) / 10),
    int(H / 10)
    ]
world = [["none" for y in range(world_scale[1])]for x in range(world_scale[0])]
draw_type = [0]
font = pygame.font.SysFont(None, 24)
timer = pygame.time.Clock()
selection = None
input_name = None
save_button = None

#ОСНОВНОЕ

def render_text(text, pos, color=(0, 0, 0), size=24, centerx=False, centery=False):#отрисовка текста на экране
    font = pygame.font.SysFont(None, size)
    text_img = font.render(text, True, color)
    text_rect = text_img.get_rect()
    if centerx:
        text_rect.centerx = pos[0]
    else:
        text_rect.x = pos[0]
    if centery:
        text_rect.centery = pos[1]
    else:
        text_rect.y = pos[1]
    screen.blit(text_img, text_rect)

def draw_brain(brain):#отрисовка мозга
    for x in range(len(brain)):
        for y in range(len(brain[x])):
            pos = [
                x * 45 + 605,
                y * 45 + 5
                ]
            pygame.draw.rect(screen, (128, 128, 128), (pos[0], pos[1], 40, 40))
            render_text(str(brain[x][y]), (pos[0] + 20, pos[1] + 20), centerx=True, centery=True)

def mouse_function():#обработка нажатий мыши
    global selection
    mousepos = pygame.mouse.get_pos()
    botpos = [#позиция объекта, на который нажали
        int(mousepos[0] / 10),
        int(mousepos[1] / 10)
        ]
    if botpos[0] < world_scale[0]:
        if pygame.mouse.get_pressed()[0]:
            if world[botpos[0]][botpos[1]] == "none":
                new_water = water.Water(botpos.copy(), world, objects)
                objects.add(new_water)
                world[botpos[0]][botpos[1]] = "water"
        elif pygame.mouse.get_pressed()[1]:
            for u in objects:
                if u.pos == botpos:
                    u.kill()
                    break
            world[botpos[0]][botpos[1]] = "none"
        elif pygame.mouse.get_pressed()[2]:
            if world[botpos[0]][botpos[1]] == "none":
                new_calcite = calcite.Calcite(botpos.copy(), world, objects)
                objects.add(new_calcite)
                world[botpos[0]][botpos[1]] = "calcite"
            
steps = 0
steps2 = 0
mousedown = 0

while keep_going:#основной цикл
    steps2 += 1
    steps2 %= 60
    events = pygame.event.get()
    for event in events:#обработка нажатий клавиш
        if event.type == pygame.QUIT:
            keep_going = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousedown = 1
        if event.type == pygame.MOUSEBUTTONUP:
            mousedown = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                keep_going = False
    screen.fill(grey)
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, world_scale[0] * 10, world_scale[1] * 10))
    if mousedown:#обработка нажатий
        mouse_function()
    if not pause[0]:#обновить всех ботов
        steps += 1
        bots[0] = 0
        objects.update(draw_type[0])
    objects.draw(screen)#отрисовка ботов
    #рисование текста
    render_text("Main:", (W - 300, 0))
    render_text("Steps: " + str(steps) + ", fps: " + str(int(timer.get_fps())), (W - 300, 20))
    render_text("Objects: " + str(len(objects)), (W - 300, 40))
    pygame.display.update()
    timer.tick(240)
pygame.quit()
