from game_object import GameObject
import image_factory
import pygame
pygame.init()

class Calcite(GameObject):
    def __init__(self, pos, world, objects):
        GameObject.__init__(self, pos, image_factory.get_image((108, 94, 60)))
        self.name = "calcite"#
        self.rotate = 4#направление
        self.world = world#ссылка на массив с миром
        self.objects = objects#ссылка на массив с объектами
        self.killed = 0#убита или нет

    def update(self, a):#a - это тип отрисовки
        if not self.killed:#если не мертва
            self.world[self.pos[0]][self.pos[1]] = self.name
