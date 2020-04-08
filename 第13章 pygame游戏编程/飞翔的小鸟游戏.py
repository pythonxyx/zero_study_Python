import pygame
import sys
import random

class Bird(object):
    ''' 定义一个鸟类 '''
    def __init__(self):
        """定义初始化方法"""
        self.birdRect = pygame.Rect(65,50,50,50)  # 鸟的矩形
        self.birdStatus = [pygame.image.load('bird1.png'),
                           pygame.image.load('bird1.png'),
                           pygame.image.load('bird1.png')]
        self.status = 0
        self.birdX = 120
        self.birdY = 350
        self.jump = False
        self.jumpSpeed = 10
        self.gravity = 5
        self.dead = False

    def birdUpdate(self):
        """用来实现鸟的移动"""
        if self.jump:
            # 小鸟跳跃
            self.jumpSpeed -= 1
            self.birdY -= self.jumpSpeed
        else:
            # 小鸟坠落
            self.gravity += 0.2
            self.birdY += self.gravity
        self.birdRect[1] = self.birdY



class Pipeline(object):
    """定义一个管道类"""
    def __init__(self):
        """定义管道的初始化方法"""
        pass

    def updatePipline(self):
        """定义管道的水平移动"""
        pass

def creatmap():
    """定义创建地图的方法"""
    screen.fill((255, 255, 255))
    screen.blit(backgroud,(0, 0))
    # 显示小鸟
    if Bird.dead:
        Bird.status = 2
    elif Bird.jump:
        Bird.status = 1
    screen.blit(Bird.birdStatus[Bird.status],(Bird.birdX,Bird.birdY))  # 设置小鸟的坐标
    Bird.birdUpdate()
    pygame.display.update()

if __name__ == '__main__':
    """主程序"""
    pygame.init()
    size = width, height = 400,650
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    Pipeline = Pipeline()
    Bird = Bird()
    while True:
        clock.tick(60)
        #   轮询事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        if (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN) and not Bird.dead:
            Bird.jump = True
            Bird.gravity = 5
            Bird.jumpSpeed = 10

        backgroud = pygame.image.load('sky.png')
        creatmap()
    pygame.quit()
