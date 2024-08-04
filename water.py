from game_object import GameObject
import image_factory
import pygame
import calcite
import random
pygame.init()

class Water(GameObject):
    def __init__(self, pos, world, objects):
        GameObject.__init__(self, pos, image_factory.get_image((0, 100, 255)))
        self.name = "water"#
        self.rotate = 4#направление(можно изменить, тогда органика будет лететь в другое место)
        self.world = world#ссылка на массив с миром
        self.objects = objects#ссылка на массив с объектами
        self.killed = 0#убита или нет

    def update(self, a):#a - это тип отрисовки
        if not self.killed:#если органика не мертва(как бы странно это не звучало)
            self.world[self.pos[0]][self.pos[1]] = self.name
            sensor = self.sensor(self.world, self.rotate)
            if sensor == 0:
                self.move(self.world)
            else:
                lft = self.sensor(self.world, 5) == 0
                rgt = self.sensor(self.world, 3) == 0
                if lft and rgt:
                    self.rotate = random.choice([3, 5])
                elif lft and not rgt:
                    self.rotate = 5
                elif rgt and not lft:
                    self.rotate = 3
                else:
                    lft2 = self.sensor(self.world, 6) == 0
                    rgt2 = self.sensor(self.world, 2) == 0
                    if lft2 and rgt2:
                        self.rotate = random.choice([2, 6])
                    elif lft2 and not rgt2:
                        self.rotate = 6
                    elif rgt2 and not lft2:
                        self.rotate = 2
                self.move(self.world)
            self.rotate = 4
