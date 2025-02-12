# 이벤트 처리
import pygame
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_UP, K_RIGHT, K_DOWN
import sys

pygame.init()
Surface = pygame.display.set_mode((640, 400))
FPSCLOCK = pygame.time.Clock()
pygame.display.set_caption('Pygame Event')
pygame.key.set_repeat(10,10)    # 키보드 연속 움직임 풀링

def main():
    xpos = 50
    ypos = 50
    while True:
        Surface.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN: # 키보드 입력이 시작되었으면
                if event.key == K_LEFT:    # xpos -num
                    if xpos <= 20: xpos = 20
                    else: xpos -= 10
                if event.key == K_RIGHT:
                    if xpos >= 620: xpos = 620
                    else: xpos += 10
                if event.key == K_UP:
                    if ypos <= 20: ypos = 20
                    else: ypos -= 10
                if event.key == K_DOWN:
                    if ypos >= 380: ypos = 380
                    else: ypos += 10                        

        pygame.draw.circle(Surface, (255,0,0), (xpos, ypos), 20)
        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == '__main__':
    main()