# IoT_Python_2025
IoT 개발자 기초 프로그래밍 언어 Repository

## 1일차
- 개발환경 설정
    - 압축, 폰트, 개발용 에디터 설치
        - 반디집(교육, 회사에서 전부 무료 사용가능)
        - D2Coding, 추후 나눔고딕코딩 필요
        - NotePad++
    - Visual Studio Code 설치
        - 확장 Korean
        - Font Family, D2Coding, Mouse Whell Zoom 설정

- 프로그래밍 언어 종류
    - 컴파일러(실행파일(.exe) 생성)
        - C, C++, C#, Java, ...
    - 인터프리터(소스코드를 바로 실행, 실행파일(.exe) 없음)
        - Python, Javascript, ...

- Python
    - 1990년에 개발한 인터프리터 언어
    - 네덜란드 개발자 귀도 반 로섬
    - 객체지향 프로그래밍 언어(Object Oriented Programming)
    - 아주 쉽게 학습할 수 있는 언어

- Python 개발환경 Pyenv
    - Python 버전을 손쉽게 변경할 수 있는 툴
    - PowerShell 관리자모드 실행 후, 아래의 명령어 실행
        ```shell
        > Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine
        ```
    - https://pyenv-win.github.io/pyenv-win/ Quick Start 1번 실행
    - pyenv로 파이썬 버전 설치 및 전역설정

- Visual Studio Code
    - 확장에서 Python 설치
    - *.py 파일 생성 후 코딩
    - Ctrl + F5로 실행

## 2일차
- 파이썬 기초
    - 변수
        - `데이터`를 담아서 다른데서 쓰기 위해 사용
    - 자료형
        - None, int, float, str, bool, list, tuple, dict, set, ...
        - type() 함수로 <class 'str'> 확인 가능 
    - 화면입출력 - 콘솔에서 입력하고 결과 출력
        - input(), print()    
    - 문자열 포맷팅
        - 문자열을 좀 더 깔끔하게 표현
        - %s, %d, %f, ...
        - {0}, {1}, {2}.format() ...
        - f'{name} ...{age}'  
    - 연산자
        - 사칙연산  : +, -, *, /, //, %, **, ()
        - 리스트 연산 : list[0], list[0:3 + 1]
        - 문자열 연산 : split(), replace(), strip(), find(), upper(), lower()....

- GitHub
    1. **fetch origin** : 리모트 최신 변경사항 확인(중요)
    2. pull : 리모트의 변경사항을 로컬로 내려받기
    3. commit : 로컬, 리모트에 변경사항을 확정
    4. push : 로컬의 변경사항을 리모트로 올리기

## 3일차
- 파이썬 기초
    - 흐름제어
        - if - 참을 기준으로 분기
        - for - 일반적인 반복문
        - while - 참인 조건일 동안 무한반복
    - 파일입출력
        - open(경로, mode='r|w|a', encoding='utf-8')
        - write(), readline()
        - close()
    - 함수
        - f(x) = y
        - 자주 사용할 로직을 묶어놓은 덩어리
        - 함수 호출
        ```python
        def funcName(param):
            # 로직
        ```
    - 객체지향
        - 현실 세계와 동일하게 프로그래밍 하겠다는 설계방식
        - 객체의 틀이 되는 클래스 선언
        - 클래스 : 명사와 동사의 집합
            - 명사 : 멤버변수(속성)
            - 동사 : 멤버함수(메서드)

        ```python
        class ClassName:
            # 멤버변수

            def 멤버함수(self, param):
                # 로직
        ```

## 4일차
- 파이썬 기초
    - 객체지향
    - 모듈, 패키지
    - 예외처리
    - 디버깅
