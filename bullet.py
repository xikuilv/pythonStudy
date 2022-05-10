# #!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time   : {2022/5/8  20:51}
# @Author : {}
# @Email  : 824935520@qq.com
# @File   : {}
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """ 子弹类 """
    def __init__(self, screen, game_settings, ship):
        super().__init__()
        self.screen = screen
        self.game_settings = game_settings

        self.rect = pygame.rect.Rect(0, 0, self.game_settings.bullet_width,
                                     self.game_settings.bullet_height)

        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.game_settings.bullet_speed_factor
        self.rect.y = self.y

    def bullet_draw(self):
        pygame.draw.rect(self.screen, self.game_settings.bullet_color, self.rect)



