# 수학 모듈 : 수학 함수들이 모여있는 파이썬 모듈
import math

print(math.pi)

PI = 3.141592
# 2**10 -> int
print(math.pow(2, 10))  # -> float
print(math.sqrt(4))
print(math.log2(2))

import random

numbers = [i for i in range(1, 45 + 1)] # 1 ~ 45 리스트로
result = []

# 초간단 로또추첨
for i in range(6):  # 여섯번 반복
    result.append(random.choice(numbers))

print(result)

# 한꺼번에 여섯개를 추출하는 랜덤
# weight : 가중치
numbers = weight = list(range(1, 45 + 1))
random.shuffle(weight)

result = random.choices(numbers, weights=weight, k=6)
print(result)