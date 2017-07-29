
class Settings():
    def __init__(self):
        "初始化游戏的设置"
        # 屏幕设置默认值
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 8
        # 子弹设置
        self.bullet_speed_factor = 4
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = 60,60,60
        self.bullets_allowed = 5
        self.alien_speed_factor = 1
        # 外星人移动的方向
        self.fleet_direction = 1
        self.fleet_drop_speed = 20