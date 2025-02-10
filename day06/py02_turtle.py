# turtle 라이브러리는 주피터노트북에서 실행 불가
import turtle as t

t.home()
t.shape('turtle')

for i in range(3):
    t.forward(100)
    t.left(120)
t.done()    # 반드시 필요