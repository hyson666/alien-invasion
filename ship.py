
import pygame

class Ship():

    #在参数中要定义在哪个屏幕对象中
    def __init__(self, ui_settings, screen):
        "初始化飞船并且设置其初始位置"
        self.screen = screen
        self.ui_settrings = ui_settings

        # 利用pygame的读取图像函数，加载飞船图像并且获取奇外接矩形
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #每艘新飞船都放在屏幕底部中央,止呕胡可以调整位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)

        #移动标志
        self.moving_left = False
        self.moving_right = False

    # 调整位置
    def updata(self):
        if self.moving_left and self.rect.left>0:
            self.center -= self.ui_settrings.ship_speed_factor
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ui_settrings.ship_speed_factor

        # 根据self。center更新rect对象
        self.rect.centerx = self.center

    def blitme(self):
        "在指定位置绘制飞船"
        self.screen.blit(self.image,self.rect)