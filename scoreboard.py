# _*_ coding:utf-8 _*_
# @Time    : 2022/5/10 8:39
# @Author  : lxk
# @File    : scoreboard.py

import pygame.font
from pygame.sprite import Group
from ship import Ship


class ScoreBoard:
    """ 显示积分 """
    def __init__(self, screen, game_settings, stats):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.game_settings = game_settings
        self.stats = stats

        self.score_font = pygame.font.SysFont(None, 24)
        self.font_color = (0, 230, 0)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()

        self.prep_ship()

    def prep_score(self):
        """ 显示得分 """
        score_str = "{:,}".format(self.stats.score)
        self.score_image = self.score_font.render("Score: "+score_str, True,
                    self.font_color, self.game_settings.screen_bg_color)

        self.score_rect = self.score_image.get_rect()

        self.score_rect.right = self.screen_rect.right - 10
        self.score_rect.top = 10

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.grop_ships_draw()

    def prep_high_score(self):
        """ 显示最高得分 """
        high_score_str = "{:,}".format(self.stats.high_score)
        self.high_score_image = self.score_font.render("High Score: " + high_score_str, True,
                                                  self.font_color, self.game_settings.screen_bg_color)

        self.high_score_rect = self.high_score_image.get_rect()

        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 10

    def prep_level(self):
        """ 显示水平 """
        level_str = "{:,}".format(self.stats.level)
        self.level_image = self.score_font.render("Level: " + level_str, True,
                                                  self.font_color, self.game_settings.screen_bg_color)

        self.level_rect = self.level_image.get_rect()

        self.level_rect.right = self.screen_rect.right - 10
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ship(self):
        self.grop_ships = Group()
        for ship_num in range(self.stats.ship_left):
            ship = Ship(self.screen, self.game_settings)
            ship.rect.x = 10 + ship.rect.width * ship_num
            ship.rect.y = 10
            self.grop_ships.add(ship)

    def grop_ships_draw(self):
        self.grop_ships.draw(self.screen)


