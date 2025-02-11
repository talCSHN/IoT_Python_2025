# Tkinter를 클래스화
from tkinter import *
from tkinter.messagebox import *    
from tkinter.scrolledtext import * 
from tkinter.font import *
import google.generativeai as genai

genai.configure(api_key='AIzaSyBTRvq8zKFU7ubaf1MTv0TVtB7IsYuNdS8')
model = genai.GenerativeModel('gemini-1.5-flash')

class WindowApp(Tk):
    def __init__(self):
        super().__init__()  # 부모 객체도 같이 초기화
        self.title('Gemini ChatBot v2.0')
        self.geometry('730x450')
        self.iconbitmap('./image/chatbot.ico')
        # 클래스 작업할때 self 유심히 다룰것
        self.protocol('WM_DELETE_WINDOW', self.onClosing)

        self.initWindow()  # 윈도우 화면 초기화 멤버메서드

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

    def keypress(self, event):
        if event.char == '\r':
            self.responseMessage()

    def responseMessage(self):  # 내용 수정
        # showinfo('동작', f'이제 API를 호출하면 됩니다.\n{self.textMessage.get("1.0", END)}')
        self.inputText = self.textMessage.get('1.0', END).replace('\n', '').strip()
        print(self.inputText)
        self.textMessage.delete('1.0', END)

        if self.inputText:
            try:
                self.textResult.insert(END, '유저: ', BOLD)
                self.textResult.insert(END, f'{self.inputText}\n\n', 'user')    # 'user' 텍스트 argument
                ai_response = model.generate_content(self.inputText)
                response = ai_response.text

                self.textResult.insert(END, '챗봇: ', 'bold')
                self.textResult.insert(END, f'{response}\n', 'ai') # 'ai' 텍스트 태그
            
            except Exception as e:
                self.textResult.insert(END, f'Error: {str(e)}\n\n', 'error')
        
            finally:
                self.textResult.see(END) # 스크롤텍스트 마지막 위치로 스크롤 다운


    def onClosing(self):
        if askyesno('종료 확인', '종료하시겠습니까?'):
            self.destroy()  # 완전 종료

if __name__ == '__main__':
    print('Tkinter 클래스 시작')
    app = WindowApp()   # Tkinter 클래스 객체 생성
    app.mainloop()

