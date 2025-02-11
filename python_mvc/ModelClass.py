from tkinter import *
from tkinter.messagebox import *    
from tkinter.scrolledtext import * 
from tkinter.font import *
import google.generativeai as genai

from Functions import WindowApp

genai.configure(api_key='AIzaSyBTRvq8zKFU7ubaf1MTv0TVtB7IsYuNdS8')
model = genai.GenerativeModel('gemini-1.5-flash')

class View(Tk):
    def __init__(self):
        super().__init__()  # 부모 객체도 같이 초기화
        self.title('Gemini ChatBot v2.0')
        self.geometry('730x450')
        self.iconbitmap('./image/chatbot.ico')
        # 클래스 작업할때 self 유심히 다룰것
        self.protocol('WM_DELETE_WINDOW', WindowApp.onClosing)
        WindowApp.initWindow(self)  # 윈도우 화면 초기화 멤버메서드

    # def initWindow(self):
    #     self.myFont = Font(family='NanumGothic', size=10)
    #     self.boldFont = Font(family='NanumGothic', size=10, weight=BOLD, slant=ITALIC)

    #     self.inputFrame = Frame(self, width=730, height=30, bg='#EFEFEF')
    #     self.inputFrame.pack(side=BOTTOM, fill=BOTH)

    #     self.textMessage = Text(self.inputFrame, width=75, height=1, wrap=WORD, font=self.myFont)
    #     self.textMessage.bind('<Key>', fx.keypress)
    #     self.textMessage.pack(side=LEFT, padx=15)

    #     self.sendButton = Button(self.inputFrame, text='전송', bg='green', fg='white', font=self.myFont, command=fx.responseMessage)
    #     self.sendButton.pack(side=RIGHT, padx=20, pady=5)

    #     self.textResult = ScrolledText(self, wrap=WORD, bg='#000000', fg='white', font=self.myFont)  # bg='black'
    #     self.textResult.pack(fill=BOTH, expand=True)

    #     self.textResult.tag_configure('user', font=self.boldFont, foreground='yellow')
    #     self.textResult.tag_configure('ai', font=self.myFont, foreground='limegreen') #89F336
    #     self.textResult.tag_configure('error', font=self.boldFont, foreground='red')

    #     self.textMessage.focus_set()

    #     self.protocol('WM_DELETE_WINDOW', fx.onClosing)