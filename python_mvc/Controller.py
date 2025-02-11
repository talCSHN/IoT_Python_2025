from tkinter import *
from tkinter.messagebox import *    
from tkinter.scrolledtext import * 
from tkinter.font import *
import google.generativeai as genai

import ModelClass as modelClass
import Functions as fx

if __name__ == '__main__':
    print('Tkinter 클래스 시작')
    app = modelClass.WindowApp()   # Tkinter 클래스 객체 생성
    app.mainloop()