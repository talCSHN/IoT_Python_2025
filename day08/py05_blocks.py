# 벽돌꺠기 게임
import pygame
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_SPACE, Rect
import sys

import random
import math

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

class Block:
    def __init__(self, col, rect, speed = 0):
        self.col = col
        self.rect = rect
        self.speed = speed
        self.dir = random.randint(-45, 45) + 270    # 225 ~ 315

    def move(self): # 공 움직임
        # 공이 움직이는 x축 값을 계속 계산하려면 x는 dir 값을 radian으로 변환 후 cos 처리
        self.rect.centerx += math.cos(math.radians(self.dir)) * self.speed
        # 공이 움직이는 y축 값을 계속 계산하려면 y는 dir 값을 radian으로 변환 후 sin 처리
        self.rect.centery -= math.sin(math.radians(self.dir)) * self.speed

    def draw_E(self):   # 공을 circle이 아니라 ellipse로 생성
        pygame.draw.ellipse(Surface, self.col, self.rect)
    
    def draw_R(self):
        pygame.draw.rect(Surface, self.col, self.rect)

pygame.init()
Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FPSCLOCK = pygame.time.Clock()
pygame.display.set_caption('Pygame Blocks')
pygame.key.set_repeat(10, 10)

def main():
    isGameStart = False
    score = 0
    BLOCK = []
    BALL = Block((200,200,0), Rect(375,650,20,20), 10)  # 공 생성, 공 스피드 10으로 시작
    PADDLE = Block((200,200,0), Rect(375,700,100,30))   # 공을 튕길 패들 생성

    # 클래스 생성
    # 무지개색 정보
    colors = [(255,0,0), (255,150,0), (255,228,0), (11,201,4), 
              (0,80,255), (0,0,147), (201,0,167)]
    
    # 초기에 생성 될 블럭들 모양(무지개색으로 아홉개씩, 54개 블럭)
    for y, color in enumerate(colors, start=0): # y값은 0~6
        for x in range(0, 9):
            BLOCK.append(Block(color, Rect(x*80 + 150, y*40 + 40, 60, 20)))
    
    bigFont = pygame.font.SysFont('NanumGothic', 80)
    smallFont = pygame.font.SysFont('NanumGothic', 45)
    M_GAME_TITLE = bigFont.render('GAME START?', True, 'white')
    M_GAME_SUBTITLE = smallFont.render('PRESS SPACE_BAR', True, 'white')
    M_CLEAR = bigFont.render('CLEAR.', True, 'yellow')
    M_FAIL = bigFont.render('FAIL', True, 'red')

    while True:
        # if isGameStart:
        #     BALL = Block((200,200,0), Rect(375,650,20,20), 10)  # 공 생성, 공 스피드 10으로 시작

        # 스코어, 스피드 표시 글자
        M_SCORE = smallFont.render(f'SCORE: {score}', True, 'white')
        M_SPEED = smallFont.render(f'SPEED: {BALL.speed}', True, 'white')
        Surface.fill((0, 0, 0))
        for event in pygame.event.get():    # 이벤트 처리 기본
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    if PADDLE.rect.centerx < 50:
                        PADDLE.rect.centerx = 50   # 패들은 왼쪽, 오른쪽으로만 이동
                    else:
                        PADDLE.rect.centerx -= 10
                elif event.key == K_RIGHT:
                    if PADDLE.rect.centerx > (SCREEN_WIDTH - 50):
                        PADDLE.rect.centerx = (SCREEN_WIDTH - 50)
                    else:
                        PADDLE.rect.centerx += 10
                elif event.key == K_SPACE:
                    isGameStart = True  # 게임 시작

        # 게임화면 랜더링
        if isGameStart == False:
            Surface.blit(M_GAME_TITLE, ((SCREEN_WIDTH / 2) - (400 / 2), (SCREEN_HEIGHT / 2) - (50 / 2)))
            Surface.blit(M_GAME_SUBTITLE, ((SCREEN_WIDTH / 2) - (300 / 2), (SCREEN_HEIGHT / 2) + 50))
        else:   # 게임 시작 후 블록들을 그리고 공이 움직이도록 처리, 바도 움직이도록 처리
            Surface.blit(M_SCORE, (10, 770))
            Surface.blit(M_SPEED, (SCREEN_WIDTH - 220, 770))
            LenBlock = len(BLOCK)   # 54개로 시작하지만 공에 충돌해서 갯수가 계속 줄어듦
            # Collision Detection(충돌 체크)
            BLOCK = [x for x in BLOCK if not x.rect.colliderect(BALL.rect)]
            if len(BLOCK) != LenBlock:  # 블럭이 공에 맞아서
                BALL.dir *= -1  # 공의 방향이 바뀜
                BALL.speed += 0.25
                # 점수 처리
                score += 10

            if BALL.rect.centery < 1000:
                BALL.move()

            # 패들과 공이 부딪힘(Collision Detect)
            if PADDLE.rect.colliderect(BALL.rect):
                BALL.speed += 0.25
                BALL.dir = 90 +(PADDLE.rect.centerx - BALL.rect.centerx) / PADDLE.rect.width * 100

            if BALL.rect.centerx < 10 or BALL.rect.centerx > (SCREEN_WIDTH - 10):   # 게임 화면 양쪽 벽 밖으로 못나가도록
                BALL.dir = 180 - BALL.dir   # 반사각만큼 방향 전환
            elif BALL.rect.centery < 10: ## 게임화면 천장에 부딪히면 반사
                BALL.dir = -BALL.dir

            # 게임 클리어, 종료 로직
            if len(BLOCK) == 0: # 공으로 블럭을 다 없앴을 때
                Surface.blit(M_CLEAR, ((SCREEN_WIDTH / 2) - (240 / 2), (SCREEN_HEIGHT / 2) - (50 / 2)))
            if BALL.rect.centery > 800:
                Surface.blit(M_FAIL, (((SCREEN_WIDTH / 2) - (240 / 2), (SCREEN_HEIGHT / 2) - (50 / 2))))
                # isGameStart = False # 게임 종료 후 재시작은 나중에 다시

            BALL.draw_E()
            PADDLE.draw_R()

            for i in BLOCK: # Block()
                i.draw_R()

        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == '__main__':
    main()