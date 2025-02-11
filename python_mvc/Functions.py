# Tkinter를 클래스화
from tkinter import *
from tkinter.messagebox import *    
from tkinter.scrolledtext import * 
from tkinter.font import *
import google.generativeai as genai


genai.configure(api_key='AIzaSyBTRvq8zKFU7ubaf1MTv0TVtB7IsYuNdS8')
model = genai.GenerativeModel('gemini-1.5-flash')

class WindowApp(Tk):
    
    def initWindow(self):
        self.myFont = Font(family='NanumGothic', size=10)
        self.boldFont = Font(family='NanumGothic', size=10, weight=BOLD, slant=ITALIC)

        self.inputFrame = Frame(self, width=730, height=30, bg='#EFEFEF')
        self.inputFrame.pack(side=BOTTOM, fill=BOTH)

        self.textMessage = Text(self.inputFrame, width=75, height=1, wrap=WORD, font=self.myFont)
        self.textMessage.bind('<Key>', self.keypress)
        self.textMessage.pack(side=LEFT, padx=15)

        self.sendButton = Button(self.inputFrame, text='전송', bg='green', fg='white', font=self.myFont, command=self.responseMessage)
        self.sendButton.pack(side=RIGHT, padx=20, pady=5)

        self.textResult = ScrolledText(self, wrap=WORD, bg='#000000', fg='white', font=self.myFont)  # bg='black'
        self.textResult.pack(fill=BOTH, expand=True)

        self.textResult.tag_configure('user', font=self.boldFont, foreground='yellow')
        self.textResult.tag_configure('ai', font=self.myFont, foreground='limegreen') #89F336
        self.textResult.tag_configure('error', font=self.boldFont, foreground='red')

        self.textMessage.focus_set()

        self.protocol('WM_DELETE_WINDOW', self.onClosing)

    def responseMessage(self):
        # showinfo('실행', 'API를 실행합니다.',)
        inputText = self.textMessage.get('1.0', END).replace('\n', '').strip()
        print(inputText)
        self.textMessage.delete('1.0', END)  # 입력창에 내용 입력 후 엔터치면 입력창 내용 삭제
        # showinfo('결과', inputText) # 다이얼로그, 모달(Modal)창

        if inputText:
            try:
                self.textResult.insert(END, '유저: ', BOLD)
                self.textResult.insert(END, f'{inputText}\n\n', 'user')    # 'user' 텍스트 argument
                ai_response = model.generate_content(inputText)
                response = ai_response.text

                self.textResult.insert(END, '챗봇: ', 'bold')
                self.textResult.insert(END, f'{response}\n', 'ai') # 'ai' 텍스트 태그
                
            except Exception as e:
                self.textResult.insert(END, f'Error: {str(e)}\n\n', 'error')
            
            finally:
                self.textResult.see(END) # 스크롤텍스트 마지막 위치로 스크롤 다운


    # 8. textMessage 위젯에서 엔터를 치면 전송버튼이 클릭
    def keypress(self, event):
        # print(repr(event.char)) # repr 안쓰면 \r, \x80 표시안됨
        # \r(캐리지 리턴), \n(뉴라인) 혼용해서 사용 \r\n, \n, \r
        if event.char == '\r':
            self.responseMessage()
    
    # 11. 종료 시 이벤트처리 함수

    def onClosing(self):
        if askyesno('종료 확인', '종료하시겠습니까?'):
            self.destroy()  # 완전 종료

