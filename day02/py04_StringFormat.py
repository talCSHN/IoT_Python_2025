# 문자열 포맷팅

loginTemp = '안녕하세요, %s님!'
# name = '박관호'

# print(loginTemp % (name))
# name = input('로그인 할 이름 입력 > ')
# print(loginTemp % (name))

# 구세대 문자열 포맷팅
intro = '나는 %s(이)고, %d살입니다. 몸무게 %fkg입니다.'
print(intro % ('박관호', 31, 90.0))

intro = '나는 %10s(이)고, %03d살입니다. 몸무게 %3.1fkg입니다.'
print(intro % ('박관호', 31, 90.0))

# 중간세대 문자열 포맷팅
# {0:>10s} 로 %10s와 동일하게 적용
intro = '나는 {0:>10s}이고, {1}살입니다. 몸무게는 {2}kg입니다.'
print(intro.format('관호', 31, 90.0))

# 신세대 문자열 포맷팅
name = '박관호'
age = 31
weight = 90.0
print(f'나는 {name}이고, {age}살입니다. 몸무게는 {weight}kg입니다.')