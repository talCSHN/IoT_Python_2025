# 객체지향

class Car:

    # __new__ 사용빈도 낮음, __init__ 사용빈도 높음
    # Car() 호출하면 아래의 메서드가 실행
    # company, name plateNumber 모를 때는 None
    def __init__(self, company=None, name=None, plateNumber=None):
        self.__company = company    # 멤버변수 이름 앞에 __ 쓰면 외부접근 불가
        self.__name = name
        self.__plateNumber = plateNumber
        print('Car 클래스를 새로 생성')
    
    # 주소값대신 문자열로 출력되도록 바꿔줌
    def __str__(self):
        return f'제 차는 {self.__name}이고 차번호는 {self.__plateNumber} 입니다.'
    
    # 외부에서 잘못된 차번호를 넣으면 안들어감
    def setPlateNumber(self, newPlateNumber):
        if type(newPlateNumber) is str:
            self.__plateNumber = newPlateNumber

    def setName(self, newName='글쎄'):  # 이름을 모를때 글쎄로 대체
        self.__name = newName

    def getName(self):
        return self.__name

# 모듈화 하려면 예제소스는 없어야함
# myCar = Car('BMW', '520d xDrive', '55너0528')
# 파라미터명=값 으로 매개변수 순서를 변경 가능
# myCar = Car(name='520d xDrive', plateNumber='55너0528', company='BMW')

# print(myCar)    #차의 번호를 출력하고 싶음

# myCar.__plateNumber = 1111    # 접근지정자로 클래스 외부에서의 데이터 수정 차단
# print(myCar)

# myCar.setPlateNumber(1111)
# print(myCar)

# yourCar = Car()
# print(yourCar)
# yourCar.setPlateNumber('22나2222')
# print(yourCar)
# yourCar.setName('카이엔')
# print(yourCar)