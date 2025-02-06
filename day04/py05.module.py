# 외부 모듈을 사용하기 위한 방법
# 내 컴퓨터에 없는 모듈을 가져와서 사용하려면
# pip -  파이썬이 제공하는 Package Installer of Python
# 터미널 -> pip install requests
# http://pypi.org 에서 설치할 패키지 검색
import requests

print('외부 패키지 사용')

# 웹 브라우저가 아닌 파이썬 상에서 웹사이트 접속
res = requests.get('https://www.google.com')    # website URL

print(res.status_code)  # 200 : OK
# print(res.content)

f = open('./day04/index.html', mode='w', encoding='utf-8')

f.write(str(res.content, 'utf-8'))
f.close()

print('파일생성')

class Sample:
    pass

import py02_car as c
# __main__ : 프로그램이 시작하는 진입점(entry point) 지칭
# C언어등의 static void main()과 동일한 역할
# 폴더 안에 py파일 중 실행되는 파이썬 파일이 __main__(진입점)이 되고
# 나머지는 모듈이 됨
if __name__ == '__main__':  # __name__ : 현재 모듈의 이름(py05.module.py)
    sam = Sample()
    print(sam)
    print(__name__)
    car = c.Car()
    print(car)