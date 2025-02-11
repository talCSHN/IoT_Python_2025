from tkinter import *
from tkinter.messagebox import *    
from tkinter.scrolledtext import * 
from tkinter.font import *
import google.generativeai as genai

# from View import WindowApp


class ChatModel:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        
    def getResponse(self, inputText):    
        try:
            # textResult.insert(END, '유저: ', BOLD)
            # textResult.insert(END, f'{inputText}\n\n', 'user')    # 'user' 텍스트 argument
            ai_response = self.model.generate_content(inputText)
            response = ai_response.text
            return response

            # textResult.insert(END, '챗봇: ', 'bold')
            # textResult.insert(END, f'{response}\n', 'ai') # 'ai' 텍스트 태그
            
        except Exception as e:
            return f'Error: {str(e)}\n\n', 'error'