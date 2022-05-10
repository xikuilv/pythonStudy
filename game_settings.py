# #!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time   : {2022/5/8  19:52}
# @Author : {}
# @Email  : 824935520@qq.com
# @File   : {}

class GameSettings:
    """ 设置类 """
    def __init__(self):

        # 屏幕设置
        self.screen_width = 800
        self.screen_height = 600
        self.screen_bg_color = (230, 230, 230)
        self.screen_caption = "Alien Invaision"

        # 飞船设置

        self.ship_limit = 3

        # 子弹设置
        self.bullet_width = 3
        self.bullet_height = 15

        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        # 外星人设置
        self.alien_point = 50
        self.alien_drop_speed = 10

        # 晋级速率
        self.game_scale = 1.1



        self.initation_stats()

    def initation_stats(self):
        self.ship_speed_factor = 1
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        self.fleet_direction = 1  # 外星舰队运动方向

    def create_jinji_scale(self):
        self.ship_speed_factor *= self.game_scale
        self.bullet_speed_factor *= self.game_scale
        self.alien_speed_factor *= self.game_scale





