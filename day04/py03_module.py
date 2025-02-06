# 모듈 - 레고
# 모듈 사용하려면
# import 모듈명
# from 모듈명 import 상세...
import py02_car

hisCar = py02_car.Car('Porche', '타이칸', '몰라')
print(hisCar)

import py02_car as c

herCar = c.Car('페라리', 'GT911', '222너2222')
print(herCar)

from py02_car import Car

thatCar = Car('람보르기니', '우라칸', '333나3333')