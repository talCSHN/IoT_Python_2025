
import pygame   # pygame 기본 모듈 추가
from pygame.locals import QUIT  # 종료 처리 변수
import sys  # 운영체제 시스템 명령

# 기본 변수
pygame.init()
Surface = pygame.display.set_mode((640, 400))   # Tkinter에서 root.geometry('640x400')와 동일
FPSCLOCK = pygame.time.Clock()
pygame.display.set_caption('Pygame Basic')

def main():
    while True:
        # Surface.fill((255, 255, 0))   # #FFFFFF(white).    #00FFFFFF / #00000000 -> 앞 두자리 : alpha 투명도
        Surface.fill(color='azure')   # #FFFFFF(white).    #00FFFFFF / #00000000 -> 앞 두자리 : alpha 투명도
        for event in pygame.event.get():    # 키보드, 마우스 이벤트 체크
            if event.type == QUIT:  # WM_DELETE_WINDOW
                pygame.quit()   # Pygame 종료
                sys.exit()      # 윈도우앱 탈출

        pygame.display.update() # 지금까지 작성 코드를 윈도우창에 표시
        FPSCLOCK.tick(30)   # 30fps

if __name__ == '__main__':
    main()
