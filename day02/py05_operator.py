# 연산자

# 사칙연산 : + - * /
a, b = 15, 14
# Shift + Del - 한줄 삭제
print(a + b)
print(a - b)
print(a * b)

# 나누기 연산자 /, //, %
a = 14
b = 4
print(a / b)    # 나눈 결과는 float
print(a // b)   # 몫, int
print(a % b)    # 나머지, int

# 거듭제곱(Power) **
print(2 ** 10)

# 연산자 우선순위
# 계산식이 복잡해서 연산자 우선순위를 잘 모르곘으면 () 사용
print((3 + 4) * 7)
print(3 + (4 * 7))

# 리스트 연산
# index = len(list) - 1
listSample = [1, 3, 5, 7, 9]
print(listSample[0])
print(len(listSample)) # 리스트의 길이

print(listSample[1])
print(listSample[2])
print(listSample[3])
print(listSample[4])

listSample[4] = 11

print(listSample[len(listSample) - 1])
# print(listSample[5])

# 문자열 연산 : +, * 만 존재
greeting = 'Hello'
target = 'World'
print(greeting, target) # 문자열 연산 아님
print(greeting + ' ' + target) # 문자열 연산 String Concatenate
print('{0} {1}'.format(greeting, target))
print(f'{greeting} {target}')

print(greeting * 5) # 해당 문자열을 * n 만큼 반복

## 문자열(Character Array) : List와 유사하지만 값 수정 불가
print(greeting[1]) # 리스트 연산
# greeting[0] = 'C'
print(greeting)

# 리스트 연산, 슬라이싱
listSample = ['2', '0', '2', '5', '-', '0', '2', '-', '0', '4']
current = '2025-02-04'

for i in listSample:
    print(i, end='')
print()

print(current)
# 준비 끝

# 인덱싱, 인덱스에 있는 값을 가져오기
print(listSample[-7])
print(current[-7])

# 슬라이싱, 리스트 자르기
# [start : end] : end값 - 1까지만 추출
print(listSample[0:3 + 1])
print(current[0:3 + 1])

# 2025-02-04
year = current[0:3 + 1]
month = current[5:6 + 1]
day = current[8:]   # end 끝까지는 숫자를 생략
print(year, month, day)
print(current[-2:])

# 문자열 연산 중 함수를 사용
full_name = "KWAN HO. PARK"
# 자르기
print(full_name.split())
print(type(full_name))
print(full_name.split(' '))
print(type(full_name))

names = full_name.split(' ')
print(type(names))
print(names)

names = full_name.split('.')
print(type(names))
print(names)

# 바꾸기
print(full_name.replace('KWAN HO.', 'PAN'))

# 공백제거
origin = '     Hello  ~     '
print(f'//{origin}//')
print(f'//{origin.lstrip()}//')
print(f'//{origin.rstrip()}//')
print(f'//{origin.strip()}//')

# 단어찾기
full_name = "KWAN HO. PARK"
print(full_name.find('P'))
print(full_name.find('p'))  # -1 : p를 찾을 수 없음

print(full_name.count('P')) # P가 문장에 몇번 존재
# print(full_name.index('b')) # 오류 발생

print(full_name.upper())
print(full_name.lower())

# T로 자를때
# '', "" == Empty(비어있음)
# ' ', " " == Space(공백 존재)
origin = 'TESTSTRING'
print(origin.split('T'))

