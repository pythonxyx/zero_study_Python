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
        self.wallx = 400
        self.pineUp = pygame.image.load('pip1.jpg')
        self.pineDown = pygame.image.load('pip2.jpg')

    def updatePipline(self):
        """定义管道的水平移动"""
        self.wallx -= 5
        if self.wallx < -80:
            global score
            score += 1
            self.wallx = 400


def creatmap():
    """定义创建地图的方法"""
    screen.fill((255, 255, 255))
    screen.blit(backgroud,(0, 0))

    # 显示管道
    screen.blit(Pipeline.pineUp,(Pipeline.wallx,0))
    screen.blit(Pipeline.pineDown,(Pipeline.wallx,500))
    Pipeline.updatePipline()

    # 显示小鸟
    if Bird.dead:
        Bird.status = 2
    elif Bird.jump:
        Bird.status = 1
    screen.blit(Bird.birdStatus[Bird.status],(Bird.birdX,Bird.birdY))  # 设置小鸟的坐标
    Bird.birdUpdate()
    pygame.display.update()

    # 显示分数
    screen.blit(font.render('score:'+str(score),-1,(255,255,255)),(100,50)) # 设置颜色及坐标位置
    pygame.display.update()


def checkDead():
    #  上方管子的矩形位置
    upRect = pygame.Rect(Pipeline.wallx,400,
                         Pipeline.pineUp.get_width() - 10,
                         Pipeline.pineUp.get_height())

    #  下方管子的矩形位置
    downRect = pygame.Rect(Pipeline.wallx,500,
                           Pipeline.pineDown.get_width() - 10,
                           Pipeline.pineDown.get_height())

    # 检测小鸟与上下方管子是否碰撞
    if upRect.colliderect(Bird.birdRect) or downRect.colliderect(Bird.birdRect):
        Bird.dead = True
    #  检测小鸟是否飞出上下边界
    if not 0 < Bird.birdRect[1] < height:
        Bird.dead = True
        return True
    else:
        return False


def getResult():
    final_text1 = 'Game Over'
    final_text2 = 'Your final score：'+str(score)
    ft1_font = pygame.font.SysFont('Arial',70)
    ft1_surf = font.render(final_text1,1,(242,3,36))
    ft2_font = pygame.font.SysFont('Arial',50)
    ft2_surf = font.render(final_text2,1,(253,177,6))
    #  设置第一行文字显示位置
    screen.blit(ft1_surf,[screen.get_width()/2 - ft1_surf.get_width()/2, 100])
    #  设置第二行文字显示位置
    screen.blit(ft2_surf,[screen.get_width()/2 - ft1_surf.get_width()/2, 200])
    pygame.display.flip()

if __name__ == '__main__':
    """主程序"""
    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont(None,50) # 设置默认字体和大小
    size = width, height = 400,650
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    Pipeline = Pipeline()
    Bird = Bird()
    score = 0
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
        if checkDead():
            getResult()
        else:
            creatmap()
    pygame.quit()
