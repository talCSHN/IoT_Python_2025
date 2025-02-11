# GUI를 위한 모듈
from tkinter import *   # tkinter 모듈에 있는 모든 클래스, 함수, 변수 등을 다 쓰겠다
from tkinter.messagebox import *    # 모듈 밑에 있는 모듈을 from tkinter import *로 가져올 수 없음
from tkinter.scrolledtext import *  # 모듈 밑에 있는 모듈을 from tkinter import *로 가져올 수 없음
from tkinter.font import *
# Gemini를 위한 모듈
import google.generativeai as genai

# 6. Gemini API용 구성
genai.configure(api_key='AIzaSyBTRvq8zKFU7ubaf1MTv0TVtB7IsYuNdS8')
model = genai.GenerativeModel('gemini-1.5-flash')

# 4. 전송버튼 이벤트, Gemini 실행
def responseMessage():
    # showinfo('실행', 'API를 실행합니다.',)
    inputText = textMessage.get('1.0', END).replace('\n', '').strip()
    print(inputText)
    textMessage.delete('1.0', END)  # 입력창에 내용 입력 후 엔터치면 입력창 내용 삭제
    # showinfo('결과', inputText) # 다이얼로그, 모달(Modal)창

    if inputText:
        try:
            textResult.insert(END, '유저: ', BOLD)
            textResult.insert(END, f'{inputText}\n\n', 'user')    # 'user' 텍스트 argument
            ai_response = model.generate_content(inputText)
            response = ai_response.text

            textResult.insert(END, '챗봇: ', 'bold')
            textResult.insert(END, f'{response}\n', 'ai') # 'ai' 텍스트 태그
            
        except Exception as e:
            textResult.insert(END, f'Error: {str(e)}\n\n', 'error')
        
        finally:
            textResult.see(END) # 스크롤텍스트 마지막 위치로 스크롤 다운


# 8. textMessage 위젯에서 엔터를 치면 전송버튼이 클릭
def keypress(event):
    # print(repr(event.char)) # repr 안쓰면 \r, \x80 표시안됨
    # \r(캐리지 리턴), \n(뉴라인) 혼용해서 사용 \r\n, \n, \r
    if event.char == '\r':
        responseMessage()

# 11. 종료 시 이벤트처리 함수
def onClosing():
    if askyesno('종료 확인', '종료하시겠습니까?'):
        root.destroy()  # 완전 종료


# 1. 메인 윈도우 생성, 초기 설정
root = Tk()
root.title('Gemini ChatBot')
root.geometry('730x450')

# 12. 아이콘 변경
# ./image/ 경로는 삭제
root.iconbitmap('chatbot.ico')  # pyinstaller로 설치할 땐 실행파일폴더에 아이콘 이미지 복사

# 7. 전체에서 사용할 폰트 지정 -> 나눔고딕
myFont = Font(family='NanumGothic', size=10)
boldFont = Font(family='NanumGothic', size=10, weight=BOLD, slant=ITALIC)

# 2. UI화면 구성
inputFrame = Frame(root, width=730, height=30, bg='#EFEFEF')
inputFrame.pack(side=BOTTOM, fill=BOTH)

# 3. inputFrame에 들어갈 Entry와 Button 구성
textMessage = Text(inputFrame, width=75, height=1, wrap=WORD, font=myFont)
# 8. 입력창에서 엔터를 치면 keypress 이벤트처리 함수 실행
textMessage.bind('<Key>', keypress)
textMessage.pack(side=LEFT, padx=15)

sendButton = Button(inputFrame, text='전송', bg='green', fg='white', font=myFont, command=responseMessage)
sendButton.pack(side=RIGHT, padx=20, pady=5)

# 5. API호출 결과 메시지 출력될 스크롤 기능 텍스트 위젯
textResult = ScrolledText(root, wrap=WORD, bg='#000000', fg='white', font=myFont)  # bg='black'
textResult.pack(fill=BOTH, expand=True)

# 10. 스크롤텍스트에 나올 메세지 디자인
textResult.tag_configure('user', font=boldFont, foreground='yellow')
textResult.tag_configure('ai', font=myFont, foreground='limegreen') #89F336
textResult.tag_configure('error', font=boldFont, foreground='red')

# 9. 실행 후 바로 입력창에 포커스가 가도록
textMessage.focus_set()

# 11. 종료버튼(x) 누르면 종료메세지 확인 후 종료
root.protocol('WM_DELETE_WINDOW', onClosing)

# 1. 종료시까지 계속 실행
root.mainloop()
