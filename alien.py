# _*_ coding:utf-8 _*_
# @Time    : 2022/5/9 9:34
# @Author  : lxk
# @File    : alien.py

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """ 外星人类 """
    def __init__(self, screen, game_settings, ship):
        super(Alien, self).__init__()
        self.screen = screen
        self.game_settings = game_settings

        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def alien_edge(self):
        """ 判断alien是否到屏幕边缘 """
        if self.rect.right >= self.game_settings.screen_width:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        self.x += self.game_settings.alien_speed_factor * self.game_settings.fleet_direction
        self.rect.x = self.x

