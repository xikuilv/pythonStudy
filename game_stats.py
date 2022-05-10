# _*_ coding:utf-8 _*_
# @Time    : 2022/5/9 14:28
# @Author  : lxk
# @File    : game_stats.py

class GameStats:
    """ 信息类 """
    def __init__(self, screen, game_settings):
        self.screen = screen
        self.game_settings = game_settings

        self.game_active = False
        self.high_score = 0

        self.reset_stats()

    def reset_stats(self):
        self.ship_left = self.game_settings.ship_limit
        self.score = 0
        self.level = 1




