from tkinter import *
from tkinter.messagebox import *    
from tkinter.scrolledtext import * 
from tkinter.font import *
import google.generativeai as genai

from View import WindowApp
from ModelClass import ChatModel

# genai.configure(api_key='AIzaSyBTRvq8zKFU7ubaf1MTv0TVtB7IsYuNdS8')
# model = genai.GenerativeModel('gemini-1.5-flash')

class Controller:
    def __init__(self):
        self.model = ChatModel(api_key='AIzaSyBTRvq8zKFU7ubaf1MTv0TVtB7IsYuNdS8')
        self.view = WindowApp(self)

    def responseMessage(self):  # 내용 수정
        # showinfo('동작', f'이제 API를 호출하면 됩니다.\n{self.textMessage.get("1.0", END)}')
        inputText = self.view.textMessage.get('1.0', END).replace('\n', '').strip()
        print(inputText)
        self.view.textMessage.delete('1.0', END)

        if inputText:
            try:
                self.view.textResult.insert(END, '유저: ', BOLD)
                self.view.textResult.insert(END, f'{inputText}\n\n', 'user')    # 'user' 텍스트 argument
                # ai_response = model.generate_content(self.inputText)
                # response = ai_response.text
                response = self.model.getResponse(inputText)

                self.view.textResult.insert(END, '챗봇: ', 'bold')
                self.view.textResult.insert(END, f'{response}\n', 'ai') # 'ai' 텍스트 태그
            
            except Exception as e:
                self.view.textResult.insert(END, f'Error: {str(e)}\n\n', 'error')
        
            finally:
                self.view.textResult.see(END) # 스크롤텍스트 마지막 위치로 스크롤 다운

    def run(self):
        self.view.mainloop()