import pygame

pygame.init()

# 创建游戏窗口
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 1. 记载图像数据
bg = pygame.image.load("./images/background.png")
# 2. bilt 绘制图像
screen.blit(bg, (0, 0))

# 绘制英雄的飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (150, 300))

# 可以再所有绘制工作完成之后，同一调用update方法

pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 1. 定义rect记录飞机初始位置
hero_rect = pygame.Rect(150, 300, 102, 126)

# 游戏循环--》 意味着游戏正式开始！
while True:
    # 可以指定循环体内部的代码执行频率
    clock.tick(60)

    # 1.捕获用户事件
    event_list = pygame.event.get()
    # 判断用户是否点击退出
    for event in event_list:
        if event.type == pygame.QUIT:
            print("退出游戏")
            pygame.quit()
            # 退出系统
            exit()

    # 2.修改飞机的位值
    hero_rect.y -= 1
    # 判断飞机的位置
    if hero_rect.y <= -126:
        hero_rect.y = 700

    # 3.调用blit方法绘制图像
    # 并且修重新绘制背景图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 调用update跟新图像
    pygame.display.update()

pygame.quit()
