import random
import pygame

# 窗口大小
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新的帧率
FRAME_PER_SEC = 60
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵类"""

    def __init__(self, image_name, speed=1):
        # 调用父类的初始化方法
        super().__init__()

        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 屏幕的垂直方向上移动
        self.rect.y += self.speed


class Background(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):
        # 调用父类方法实现精灵的创建
        super().__init__("./images/background.png")
        # 判断是否时交替图像,如果时,设置初始位置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 调用父类的方法实现
        super().update()
        # 判断是否移出屏幕,如果移出屏幕,将图像设置到屏幕的上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -SCREEN_RECT.height


class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):
        # 调用父类方法,创建敌机精灵,同时指定敌机图片
        super().__init__("./images/enemy1.png")
        # 指定敌机的初始随机速度 1-3
        self.speed = random.randint(1, 3)
        # 指定敌机的初始随机位置
        # self.rect.y = -self.rect.height
        self.rect.bottom = 0  # 垂直方向
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)  # 水平方向

    def __del__(self):
        # print("敌机销毁 %s" % self.rect)
        pass

    def update(self):
        # 调用父类方法.保持垂直方向的飞行
        super().update()
        # 判断是否飞出屏幕,如果飞出就从精灵组删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            # print("飞出屏幕,需要从精灵组删除")
            self.kill()  # 将敌机精灵从精灵组中销毁


class Bullet(GameSprite):
    """子弹精灵"""

    def __init__(self):
        # 调用父类方法,设置子弹图片,设置子弹速度
        super().__init__("./images/bullet1.png", -2)

    def update(self):
        # 调用父类方法,让子弹眼垂直方向飞行
        super().update()
        # 判断字段是否飞出屏幕
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        # print("子弹被销毁")
        pass


class Hero(GameSprite):
    """英雄精灵"""

    def __init__(self, speedy=0):
        # 调用父类方法,设置image和speed
        super().__init__("./images/me1.png", 0)
        # 设置英雄的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        self.speedy = speedy
        # 创建子弹的精灵组
        self.bullets_group = pygame.sprite.Group()

    def update(self):
        # 英雄在水平方向移动
        self.rect.x += self.speed
        # 英雄在垂直方向移动
        self.rect.y += self.speedy
        # 控制英雄不能离开屏幕
        if self.rect.left < SCREEN_RECT.left:
            self.rect.left = SCREEN_RECT.left
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        if self.rect.top < SCREEN_RECT.top:
            self.rect.top = SCREEN_RECT.top
        elif self.rect.bottom > SCREEN_RECT.bottom:
            self.rect.bottom = SCREEN_RECT.bottom

    def fire(self):
        for i in range(3):
            # 创建子弹精灵
            bullet = Bullet()
            # 设计子弹的位置
            bullet.rect.bottom = self.rect.y - 20 * i
            bullet.rect.centerx = self.rect.centerx
            # 将子弹精灵添加到精灵组
            self.bullets_group.add(bullet)
