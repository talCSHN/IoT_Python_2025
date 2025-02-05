# 함수, Function, Method, Procedure...
# 인자, Parameter, 매개변수, Argument
# def 함수명(인자(parameter, Argument, 매개변수), ...):
#   함수안으로 진입

def say_hi():
    print('안녕')
    # return None

def say_hello(name):
    print(f'{name}야, 안녕.')
    # return None

def get_age(birthYear):
    age = 2025 - birthYear + 1
    return age  # return value -> 반환값을 가지고 메서드 호출 위치로 감

def closing():
    return 'bye'

print('인사하기:', end =' ')
say_hi()    # 함수 호출
say_hi()

name = input('이름입력 > ')
print('이름으로 인사하기:', end=' ')
say_hello(name)

year = int(input('생일년도 입력 > '))
real_age = get_age(year)
print(f'나이는: {real_age}세')

print('프로그램 종료 : ', closing())