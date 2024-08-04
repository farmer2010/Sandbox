import pygame
pygame.init()

def is_relative(brain1, brain2):#функция проверки родственников(если 29 из 30 команд совпадают)
    errors = 0
    if brain1 == brain2:
        return(True)
    for x in range(5):
        for y in range(6):
            if brain1[x][y] != brain2[x][y]:
                errors += 1
            if errors > 1:
                return(False)
    if errors <= 1:
        return(True)
    else:
        return(False)

class GameObject(pygame.sprite.Sprite):#game_object - класс - потомок бота и органики
    movelist = [#массив с поворотами(для движения)
        (0, -1),
        (1, -1),
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1),
        (-1, 0),
        (-1, -1),
        ]
    def __init__(self, pos, image):
        pygame.sprite.Sprite.__init__(self)
        self.name = None#имя(изменяется потомками)
        self.rotate = 0#направление(изменяется потомками)
        self.image = image#картинка
        self.pos = pos#позиция
        self.rect = self.image.get_rect()#настройка местоположения на экране
        self.rect.x = self.pos[0] * 10
        self.rect.y = self.pos[1] * 10
        self.W = pygame.display.Info().current_w#настройка размеров экрана
        self.H = pygame.display.Info().current_h
        self.world_scale = [#настройка размера мира
            int((self.W - 300) / 10),
            int(self.H / 10)
            ]
        self.border = self.world_scale[1]

    def update(self):#обновление(изменяется потомками)
        pass

    def move(self, world):#переместиться
        pos2 = [#позиция, не которую смотрит game_object
            (self.pos[0] + GameObject.movelist[self.rotate][0]) % self.world_scale[0],
            self.pos[1] + GameObject.movelist[self.rotate][1]
            ]
        if pos2[1] >= 0 and pos2[1] <= self.border - 1:#если можно сдвинуться
            if world[pos2[0]][pos2[1]] == "none":
                world[self.pos[0]][self.pos[1]] = "none"#перемещение
                world[pos2[0]][pos2[1]] = self.name
                self.pos[0] += GameObject.movelist[self.rotate][0]
                self.pos[0] %= self.world_scale[0]
                self.pos[1] += GameObject.movelist[self.rotate][1]
                self.rect.x = self.pos[0] * 10
                self.rect.y = self.pos[1] * 10

    def sensor(self, world, rotate):#сенсор
        #0 - пусто, 1 - стена, 2 - вода
        pos2 = [#позиция, не которую смотрит game_object
            (self.pos[0] + GameObject.movelist[rotate][0]) % self.world_scale[0],
            self.pos[1] + GameObject.movelist[rotate][1]
            ]
        if pos2[1] >= 0 and pos2[1] <= self.world_scale[1] - 1:#если не смотрит в границу(иначе вернуть 1)
            if world[pos2[0]][pos2[1]] == "calcite":#если перед сенсором блок
                return 1
            elif world[pos2[0]][pos2[1]] == "water":#если перед сенсором вода
                return 2
            elif world[pos2[0]][pos2[1]] == "none":#если перед сенсором ничего нет
                return 0
        else:
            return 1
