# Tkinter를 클래스화
from tkinter import *
from tkinter.messagebox import *    
from tkinter.scrolledtext import * 
from tkinter.font import *
import google.generativeai as genai

from ModelClass import WindowApp

genai.configure(api_key='AIzaSyBTRvq8zKFU7ubaf1MTv0TVtB7IsYuNdS8')
model = genai.GenerativeModel('gemini-1.5-flash')

def responseMessage():
    # showinfo('실행', 'API를 실행합니다.',)
    inputText = modelClass.textMessage.get('1.0', END).replace('\n', '').strip()
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

