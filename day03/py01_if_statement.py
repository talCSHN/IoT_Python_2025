# if문 : 흐름제어의 가장 기본
# 흐름제어 마지막에는 항상 : 사용해야함
# if (참이 되는 조건):
#   if문 안으로 들어간다.

age = int(input('나이를 입력하세요. '))

# 만약에 나이가 19세가 아니면 담배를 살 수 없음
# 조건이 여러 개일때 and, or로 계속 작성
# if age > 19 or age == 19: #참인 조건. if는 무조건 참 
if age >= 19:
    print('4,500원입니다.')
else: # False
    print('집에 가라')

grade = input('학점을 입력하세요(A| B| C| D| F) ').upper()  # 소문자도 대문자로 변경

if grade == 'A' or grade == 'B':    # 학점이 A거나 B면, 이 구문에 걸리면
    # 구문 안으로 들어간다
    print('열심히 했네')
    print('축하합니다.')

    if grade == 'A':
        print('장학금 지급')
    else:
        print('장학금은 안된다')

elif grade == 'C':  # 학점이 C이면
    print('그럭저럭 했네')
else:
    print('공부해라')