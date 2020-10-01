import pygame
from plane_sprites import *

HERO_SPEED = 4


class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self):
        print("游戏初始化")
        # 创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 调用私有方法，精灵和精灵组的创建
        self.__create_sprites()
        # 设置定时器事件--创建敌机 1s,英雄发射子弹 0.5s
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def __create_sprites(self):
        # 创建背景精灵和精灵组
        # bg1 = Background("./images/background.png")
        # bg2 = Background("./images/background.png")
        # bg2.rect.y = -bg2.rect.height
        # self.back_group = pygame.sprite.Group(bg1, bg2)
        self.back_group = pygame.sprite.Group(Background(), Background(True))
        # 创建敌机精灵组
        self.enemy_group = pygame.sprite.Group()
        # 创建英雄的精灵和精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("开始游戏")
        while True:
            # 设置刷新频率
            self.clock.tick(FRAME_PER_SEC)
            # 监听事件
            self.__event_handler()
            # 碰撞检测
            self.__check_collide()
            # 更新/绘制精灵组
            self.__update_sprites()
            # 更新显示
            pygame.display.update()

    def __event_handler(self):
        for event in pygame.event.get():
            # 判断是否对出游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                # 创建敌机
                enemy = Enemy()
                # 将敌机精灵添加到精灵组
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
            # 获取键盘按键
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_RIGHT]:
                self.hero.speed = HERO_SPEED
                self.hero.speedy = 0
            elif keys_pressed[pygame.K_LEFT]:
                self.hero.speed = -HERO_SPEED
                self.hero.speedy = 0
            elif keys_pressed[pygame.K_DOWN]:
                self.hero.speed = 0
                self.hero.speedy = HERO_SPEED
            elif keys_pressed[pygame.K_UP]:
                self.hero.speed = 0
                self.hero.speedy = -HERO_SPEED
            else:
                self.hero.speed = 0
                self.hero.speedy = 0

    def __check_collide(self):
        # 子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullets_group, self.enemy_group, True, True)
        # 敌机撞毁英雄
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        # 判断列表是否有内容
        if len(enemies) > 0:
            # 让英雄牺牲
            self.hero.kill()
            # 结束游戏
            PlaneGame.__game_over()

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets_group.update()
        self.hero.bullets_group.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()


if __name__ == "__main__":
    # 创建游戏对象
    game = PlaneGame()

    # 启动游戏
    game.start_game()
