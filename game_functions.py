
"重构的检测时间，在此检测游戏时间"
import sys

import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ui_settings, screen, ship, bullets):
    # 飞船坐标加减改为开关就可以持续移动了
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_SPACE:
        if len(bullets) < ui_settings.bullets_allowed:
            fire_bullet(ui_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ui_settings, screen, ship, bullet):
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = False

def check_events(ui_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # 先进入按下键的事件再判断哪个键
        elif event.type == pygame.KEYDOWN:  #有按键按下时
            check_keydown_events(event, ui_settings, screen, ship, bullets)
        # 先进入放开键的事件再判断哪个键
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ui_settings, screen, ship, bullets)

def update_screen(ui_settings, screen, ship, aliens, bullets):
    """更新屏幕上的图像，并且切换到新屏幕"""
    # 每次输出显示前都进行绘制(染色函数）
    screen.fill(ui_settings.bg_color)
    # 传送飞船位图(按图层开始显示）
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    # 让最近绘制的屏幕可见(屏幕处理完成后输出)
    pygame.display.flip()

def update_bullets(bullets):
    "更新子弹位置，删除消失子弹"
    bullets.update()
    # 注意删除已经消失的子弹以节省内存,copy()副本检测使修改原数据成为了可能
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)  # 可以通过remove()删除group中的内容

def update_aliens(aliens):
    aliens.update()

def fire_bullet(ui_settings, screen, ship, bullets):
    if len(bullets) < ui_settings.bullets_allowed:
        new_bullet = Bullet(ui_settings, screen, ship)
        bullets.add(new_bullet)

def get_number_aliens_x(ui_settings, alien_width):
    "计算每行可容纳多少个外星人"
    available_space_x = ui_settings.screen_width - 2 * alien_width
    number_alien_x = int(available_space_x / (2 * alien_width))
    return number_alien_x

def get_number_rows(ui_settings, ship_height, alien_height):
    "计算屏幕可容纳多少行外星人"
    available_space_y = (ui_settings.screen_height - 3 * alien_height - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    print(number_rows)
    return number_rows

def create_alien(ui_settings, screen, aliens, alien_number, row_number):
    """创建外星人函数"""
    """
    可以使用以下方式生成随机位置：
    from random import randint
    random_number = randint(-10,10)
    """
    alien = Alien(ui_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.y = alien.rect.height + 2 * alien.rect.height * row_number
    # 计算后后定位进入rect的属性
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)

def create_fleet(ui_settings, screen, ship, aliens):
    "创建外星人群"
    # 创建一个外星人，并计算一行可以容纳多少个外形人
    # 外星人间距为外星人宽度
    alien = Alien(ui_settings, screen)
    number_alien_x = get_number_aliens_x(ui_settings, alien.rect.width)
    number_rows = get_number_rows(ui_settings, ship.rect.width, alien.rect.height)

    #创建第一行外星人
    for row_number in range(number_rows):
        for alien_number in range(number_alien_x):
            # 创建一个外星人并加入当前行
            create_alien(ui_settings, screen , aliens, alien_number, row_number)

def check_fleet_edges(ui_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ui_settings, aliens)
            break

def change_fleet_direction(ui_settings, aliens):
    "将整群外星人下移，并改变它们的方向"
    for alien in aliens.sprites():
        alien.rect.y += ui_settings.fleet_drop_speed
    ui_settings.fleet_direction *= -1

def update_aliens(ui_settings, aliens):
    "检查是否有处于边缘的外星人，更新群体外星人位置"
    check_fleet_edges(ui_settings, aliens)
    aliens.update()


