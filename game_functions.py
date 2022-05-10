# #!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time   : {2022/5/8  20:11}
# @Author : {}
# @Email  : 824935520@qq.com
# @File   : {}
import sys
import pygame
from time import sleep
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, screen, game_settings, stats, aliens, ship, bullets, sb):
    """ 按键按下 """
    if event.key == pygame.K_RIGHT:
        ship.ship_moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.ship_moving_left = True

    elif event.key == pygame.K_SPACE:
        fire_bullet(screen, game_settings, ship, bullets)

    elif event.key == pygame.K_q:
        sys.exit()

    elif event.key == pygame.K_p:
        start_game(screen, game_settings, stats, aliens, ship, bullets, sb)


def fire_bullet(screen, game_settings, ship, bullets):
    """ 开火 """
    if len(bullets) < game_settings.bullet_allowed:
        new_bullet = Bullet(screen, game_settings, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """ 按键松开 """
    if event.key == pygame.K_RIGHT:
        ship.ship_moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.ship_moving_left = False


def check_events(screen, game_settings, stats, ship, aliens, bullets, button, sb):
    # 响应鼠标和键盘事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, screen, game_settings, stats, aliens, ship, bullets, sb)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mose_x, mose_y = pygame.mouse.get_pos()
            check_button(screen, game_settings, stats, button, aliens, bullets, ship, sb, mose_x, mose_y)


def check_button(screen, game_settings, stats, button, aliens, bullets, ship, sb, mose_x, mose_y):
    """ 响应鼠标事件 """
    if button.rect.collidepoint(mose_x, mose_y) and not stats.game_active:
        start_game(screen, game_settings, stats, aliens, ship, bullets, sb)


def start_game(screen, game_settings, stats, aliens, ship, bullets, sb):
    """ 开始游戏 """
    pygame.mouse.set_visible(False)
    game_settings.initation_stats()
    stats.reset_stats()
    stats.game_active = True

    sb.prep_score()
    sb.prep_high_score()
    sb.prep_level()
    sb.prep_ship()

    aliens.empty()
    bullets.empty()

    fleet_aliens(screen, game_settings, ship, aliens)
    ship.ship_center()


def update_screen(screen, game_settings, stats, ship, aliens, bullets, button, sb):
    """ 屏幕刷新 """
    screen.fill(game_settings.screen_bg_color)

    ship.ship_blit()

    aliens.draw(screen)

    for bullet in bullets:
        bullet.bullet_draw()

    if not stats.game_active:
        button.button_draw()

    sb.show_score()

    pygame.display.flip()


def update_bullet(screen, game_settings, stats, ship, aliens, bullets, sb):
    """ 刷新子弹 """
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_alien_bullet_collision(screen, game_settings, stats, ship, aliens, bullets, sb)


def check_alien_bullet_collision(screen, game_settings, stats, ship, aliens, bullets, sb):
    """ 响应子弹和外星人相碰撞 """
    collision = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        game_settings.create_jinji_scale()
        stats.level += 1
        sb.prep_level()
        # 创建外星人舰队
        fleet_aliens(screen, game_settings, ship, aliens)
        # 清空子弹
        bullets.empty()

    elif collision:
        for aliens in collision.values():
            stats.score += game_settings.alien_point*len(aliens)
            sb.prep_score()
    elif stats.high_score < stats.score:
        stats.high_score = stats.score
        sb.prep_high_score()


def update_alien(screen, game_settings, stats, aliens, ship, bullets, sb):
    """ 更新 alien """
    for alien in aliens:
        if alien.alien_edge():
            check_alien_direction(game_settings, aliens)
            break

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(screen, game_settings, stats, ship, aliens, bullets, sb)

    for alien in aliens:
        if alien.rect.bottom >= game_settings.screen_height:
            ship_hit(screen, game_settings, stats, ship, aliens, bullets, sb)
            break

    aliens.update()


def ship_hit(screen, game_settings, stats, ship, aliens, bullets, sb):

    if stats.ship_left > 0:
        # ship_left 减一
        stats.ship_left -= 1

        sb.prep_ship()

        # 子弹和外星人均清零
        aliens.empty()
        bullets.empty()

        # 创建外星人舰队
        fleet_aliens(screen, game_settings, ship, aliens)

        # 飞船显示在底部中央
        ship.ship_center()

        # 暂停1秒
        sleep(1)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_alien_direction(game_settings, aliens):
    """ 如果 alien 碰到屏幕边缘，aliens舰队下移 """
    for alien in aliens:
        alien.rect.y += game_settings.alien_drop_speed
    game_settings.fleet_direction *= -1


def get_number_row(game_settings, alien):
    available_space_x = game_settings.screen_width - 2 * alien.rect.width
    number_row = int(available_space_x / (2 * alien.rect.width))
    return number_row


def get_number_col(game_settings, alien, ship):
    available_space_y = game_settings.screen_height - 5 * alien.rect.height - ship.rect.height
    number_col = int(available_space_y / (2 * alien.rect.height))
    return number_col


def create_alien(screen, game_settings, ship, aliens, num_x, num_y):
    alien = Alien(screen, game_settings, ship)
    alien.x = alien.rect.width + 2 * alien.rect.width * num_x
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height*num_y
    aliens.add(alien)


def fleet_aliens(screen, game_settings, ship, aliens):
    alien = Alien(screen, game_settings, ship)
    number_col = get_number_col(game_settings, alien, ship)
    number_row = get_number_row(game_settings, alien)

    for num_y in range(number_col):
        for num_x in range(number_row):
            create_alien(screen, game_settings, ship, aliens, num_x, num_y)



