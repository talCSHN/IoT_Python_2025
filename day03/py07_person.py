class Person:
    # 명사(속성)인 멤버변수
    name = '박관호'
    age = 31
    weight = 90
    gender = 'male'

    # 생성자. 초기화 메서드(파이썬 기본 내장 메서드,)
    def __init__(self, name, age, weight, gender):
        self.name = name
        self.age = age
        self.weight = weight
        self.gender = gender

    # 객체 출력을 문자열 포맷팅
    def __str__(self):
        retStr = f'{self.name}\n{self.age}\n{self.weight}\n{self.gender}'
        return retStr

    # 동사인 멤버함수(메서드)
    def getup(self):    # myself
        print(f'{self.name}이(가) 일어납니다.')

    def setWeight(self, weight):
        print(f'{self.name}의 몸무게가 변경됩니다.')
        print(f'현재 {self.weight}kg')
        self.weight = weight
        print(f'변경 후 {self.weight}kg')

    def getGender(self):
        return self.gender

man = Person('관호', 29, 85, 'man') # __init__() 함수를 실행
man.getup()
man.setWeight(92.5)
print(f'{man.name}의 성별은 {man.getGender()}.')
print('-----------------------------')
print('객체 정보')
print(man)