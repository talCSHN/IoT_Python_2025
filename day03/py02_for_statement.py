# for문 : 프로그래밍의 꽃
# 반복을 처리할 때 사용
# for 변수 in 반복할 값:
#   구문안으로...

# 아래와 같이 출력되는 프로그램을 작성하시오.
'''
최대 별 수 : 4
*
**
***
****
'''
# range() : 범위 생성 클래스
# 마지막 수 : max - 1
# range(8) -> range(0, 8)
# print(range(0, 8, 2))
# range(init, max, add)

# for i in [0, 1, 2, 3, 4, 5, 6, 7] # 이 조건이 참인 동안 반복
# for i in range(0, 8, 2):
#     print(i)

# num = int(input('최대변수 : '))

# for i in range(1, num + 1):
#     print('*' * i)

# 구구단
# 2단부터 9단까지
# 요구사항1 - 한줄에 각 단씩 출력되도록
# 요구사항2 - x*y값이 항상 두 줄씩 출력되도록
# 요구사항3 - 단 시작 표시되도록

for x in range(2, 9 + 1):
    # if x == 5: break
    # if x == 5: continue

    print(f'{x}단 시작 ')
    for y in range(1, 9 + 1):

        # if y == 8: break
        print(f'{x} x {y} = {x * y:2d}', end = '   ')
    
    print() # 그냥 한 줄 내리기

print('\n구구단 종료\n\n')

# 반복문 빠져나올때 : break
# 반복문의 특정 조건을 지나칠 때 : continue