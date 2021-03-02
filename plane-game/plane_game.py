import pygame
from plane_sprites import GameSprite

"""热身代码，对pygame框架进行初步了解"""

# 初始化
pygame.init()

# 创建游戏的窗口
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
bg = pygame.image.load("./images/background.png")  # 加载图像数据
screen.blit(bg, (0, 0))  # 绘制图像
# pygame.display.update()  # 刷新窗口

# 绘制英雄图像
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (189, 500))
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 记录飞机的初始位置
hero_rect = pygame.Rect(189, 500, 102, 126)

# 创建敌机的精灵
enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png", speed=3)

# 创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy, enemy1)

while True:
    # 指定循环体内代码执行的频率
    clock.tick(60)

    hero_rect.y -= 1  # 修改飞机的位置

    # 判断飞机是否超过顶部
    if hero_rect.y <= -hero_rect.height:
        hero_rect.y = 700

    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)  # 调用blit()方法绘制图像

    # 精灵组update()
    enemy_group.update()
    # 精灵组draw(),在screen上绘制精灵组
    enemy_group.draw(screen)

    pygame.display.update()  # 窗口刷新

    # 事件循环
    for event in pygame.event.get():
        # 监听关闭游戏窗口事件
        if event.type == pygame.QUIT:
            pygame.quit()  # 销毁

            exit()  # 退出系统，直接中止当前执行的程序
