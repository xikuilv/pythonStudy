# #!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time   : {2022/5/8  19:34}
# @Author : {}
# @Email  : 824935520@qq.com
# @File   : {}

import pygame
from ship import Ship
from game_settings import GameSettings
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard


def main():
    # pygame 初始化
    pygame.init()

    # 创建设置类对象
    game_settings = GameSettings()


    # 创建显示屏幕对象
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption(game_settings.screen_caption)

    # 创建ship对象
    ship = Ship(screen, game_settings)
    stats = GameStats(screen, game_settings)
    # 创建 bullets 编组
    bullets = Group()
    # 创建 aliens 编组
    aliens = Group()

    button = Button(screen, game_settings, "Play")

    # 创建外星人舰队
    gf.fleet_aliens(screen, game_settings, ship, aliens)

    sb = ScoreBoard(screen, game_settings, stats)

    while True:

        gf.check_events(screen, game_settings, stats, ship, aliens, bullets, button, sb)

        if stats.game_active:

            ship.update_ship()

            gf.update_alien(screen, game_settings, stats, aliens, ship, bullets, sb)

            gf.update_bullet(screen, game_settings, stats, ship, aliens, bullets, sb)

        gf.update_screen(screen, game_settings, stats, ship, aliens, bullets, button, sb)


if __name__ == '__main__':
    main()

