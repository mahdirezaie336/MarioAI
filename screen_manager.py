import time

import pygame
from constants import Consts
import threading
import sys
from items import *

from map import Map


# from state import State


class Display:

    def __init__(self, map_: str):
        self.__map = map_ + 'F'
        self.__w = len(map_) + 1
        self.__h = 4
        w, h = self.__w, self.__h

        # PyGame part
        pygame.init()
        sw, sh = Consts.SCREEN_WIDTH, Consts.SCREEN_HEIGHT
        self.screen = pygame.display.set_mode((sw, sh))
        self.screen.fill(Consts.BACKGROUND_COLOR)

        # Setting cell size and other sizes
        if w / h > sw / sh:
            rect_width = sw - 2 * Consts.SCREEN_MARGIN_SIZE
            cell_size = int(rect_width / w)
            rect_height = cell_size * h
        else:
            rect_height = sh - 2 * Consts.SCREEN_MARGIN_SIZE
            cell_size = int(rect_height / h)
            rect_width = cell_size * w
        self.cell_size = cell_size
        self.rect_width = rect_width
        self.rect_height = rect_height

        # Loading images
        goomba = pygame.image.load(Consts.GOOMBA_IMAGE)
        mushroom = pygame.image.load(Consts.MUSHROOM_IMAGE)
        lakitu = pygame.image.load(Consts.LAKITU_IMAGE)
        mario = pygame.image.load(Consts.GOOMBA_IMAGE)
        flag = pygame.image.load(Consts.FLAG_IMAGE)
        ground_surf = pygame.image.load(Consts.GROUND_SURF_IMAGE)
        ground = pygame.image.load(Consts.GROUND_IMAGE)
        self.__images = {'G': pygame.transform.scale(goomba, (cell_size, cell_size)),
                         'M': pygame.transform.scale(mushroom, (cell_size, cell_size)),
                         'L': pygame.transform.scale(lakitu, (cell_size, cell_size)),
                         'X': pygame.transform.scale(mario, (cell_size, 2*cell_size)),
                         'GR': pygame.transform.scale(ground, (cell_size, cell_size)),
                         'GS': pygame.transform.scale(ground_surf, (cell_size, cell_size)),
                         'F': pygame.transform.scale(flag, (cell_size, cell_size)),
                         }
        self.draw_cells()
        pygame.display.update()
        while True:
            pygame.display.update()
            pygame.event.pump()
            time.sleep(0.3)

    def draw_cells(self):
        sw, sh = Consts.SCREEN_WIDTH, Consts.SCREEN_HEIGHT
        w, h = self.__w, self.__h
        rect_width, rect_height = self.rect_width, self.rect_height
        cell_size = self.cell_size

        # Drawing cells
        init_y = (sh - rect_height) / 2
        init_x = (sw - rect_width) / 2
        for j in range(3):
            for i in range(w):
                x = init_x + i * cell_size
                y = init_y + j * cell_size
                color = Consts.SKY_COLOR
                pygame.draw.rect(self.screen, color, (x, y, cell_size, cell_size), 0)
                if j == 2:
                    item_char = self.__map[i]
                    if item_char != '_':
                        self.draw_in_position(j, i, self.__images[item_char])
        j = 3
        for i in range(w):
                x = init_x + i * cell_size
                y = init_y + j * cell_size
                color = Consts.BLOCK_COLOR
                pygame.draw.rect(self.screen, color, (x, y, cell_size, cell_size), 0)
                self.draw_in_position(j, i, self.__images['GS'])

    def draw_in_position(self, y: int, x: int, image):
        init_y = (Consts.SCREEN_HEIGHT - self.rect_height) / 2
        init_x = (Consts.SCREEN_WIDTH - self.rect_width) / 2
        pos_x = init_x + x * self.cell_size
        pos_y = init_y + y * self.cell_size
        self.screen.blit(image, (pos_x, pos_y))



Display('__M_____')
