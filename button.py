# _*_ coding:utf-8 _*_
# @Time    : 2022/5/9 14:57
# @Author  : lxk
# @File    : button.py

import pygame.font


class Button:
    """ 按钮类 """
    def __init__(self, screen, game_settings, msg):
        self.screen = screen
        self.game_settings = game_settings

        # 按钮尺寸及属性
        self.button_width, self.button_height = 150, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.text_font = pygame.font.SysFont(None, 48)

        # 按钮对象
        self.rect = pygame.Rect(0, 0, self.button_width, self.button_height)
        self.rect.center = (self.screen.get_rect()).center

        # 按钮游戏时只显示一次
        self.prep_button(msg)

    def prep_button(self, msg):
        self.msg_image = self.text_font.render(msg, True, self.text_color, self.button_color)
        self.msg_rect = self.msg_image.get_rect()
        self.msg_rect.center = self.rect.center

    def button_draw(self):
        #  绘制一个用颜色填充的按钮，再绘制文本
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_rect)

