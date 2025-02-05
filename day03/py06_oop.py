# 객체지향 - Object Oriented Programming
# class 클래스명:
#   속성변수(멤버변수) = 값
#   
#   def 함수(self, 매개변수):
#       수행할 로직
#       return ...
# 클래스는 명사(변수)와 동사(함수)의 집합
class Person:
    pass

man = Person()
print(f'객체 man의 타입 {type(man)}')
print(f'객체 man의 id {id(man)}')

woman = Person()
print(f'객체 man의 타입 {type(woman)}')
print(f'객체 man의 id {id(woman)}')