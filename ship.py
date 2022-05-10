# #!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time   : {2022/5/8  19:44}
# @Author : {}
# @Email  : 824935520@qq.com
# @File   : {}
import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """ 飞船类 """
    def __init__(self, screen, game_settings):
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.game_settings = game_settings

        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # 初始位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 精确定位
        self.center = float(self.rect.centerx)

        # 飞船运行标志
        self.ship_moving_right = False
        self.ship_moving_left = False

    def update_ship(self):
        """ 刷新飞船位置 """
        if self.ship_moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.game_settings.ship_speed_factor
        elif self.ship_moving_left and self.rect.left > 0:
            self.center -= self.game_settings.ship_speed_factor
        self.rect.centerx = self.center

    def ship_blit(self):
        """ 显示飞船 """
        self.screen.blit(self.image, self.rect)

    def ship_center(self):
        self.center = self.screen_rect.centerx
