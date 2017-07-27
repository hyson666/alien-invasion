"官方模块"
import sys

"第三方模块"
import pygame
from pygame.sprite import Group
from settings import Settings   #引入设置类
from ship import Ship
import game_functions as gf

def run_game():
    #初始化游戏并创建一个窗口，这里的参数主要用于绘制屏幕参数
    pygame.init()
    ui_settings = Settings()
    screen = pygame.display.set_mode((ui_settings.screen_width,ui_settings.screen_height))    #参数用列表传输屏幕大小宽、高
    pygame.display.set_caption("Alien Invasion")

    #给飞船对象传输当前屏幕对象而创建一个实例
    ship = Ship(ui_settings,screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()

    bg_color = (230,230,230)    #使用RGB参数绘制

#开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        gf.check_events(ui_settings, screen, ship, bullets)
        #根据按键调整坐标再画图
        ship.updata()
        bullets.update()

        # 注意删除已经消失的子弹以节省内存,copy()副本检测使修改原数据成为了可能
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)  #可以通过remove()删除group中的内容

        gf.updata_screen(ui_settings, screen, ship, bullets)

run_game()