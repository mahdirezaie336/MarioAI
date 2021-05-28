import pygame

from constants import Consts


class Item:

    image = None

    def __init__(self, size: tuple[int, int], position: tuple[int, int]):
        self._size = size
        self._position = position  # (y, x)

    def get_size(self):
        return self._size

    def get_position(self):
        return self._position

    def get_image(self):
        return self.image


class Mario(Item):

    image = pygame.image.load(Consts.MARIO_IMAGE)

    def __init__(self, size, position):
        super().__init__(size, position)
        self.image = pygame.transform.scale(pygame.image.load(Consts.MARIO_IMAGE), size)


class Lakitu(Item):

    image = pygame.image.load(Consts.LAKITU_IMAGE)

    def __init__(self, size, position):
        super().__init__(size, position)
        self.image = pygame.transform.scale(self.image, size)


class Goomba(Item):

    image = pygame.image.load(Consts.GOOMBA_IMAGE)

    def __init__(self, size, position):
        super().__init__(size, position)
        self.image = pygame.transform.scale(self.image, size)
