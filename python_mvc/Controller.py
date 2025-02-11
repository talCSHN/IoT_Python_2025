from tkinter import *
from tkinter.messagebox import *    
from tkinter.scrolledtext import * 
from tkinter.font import *
import google.generativeai as genai

from ModelClass import View

if __name__ == '__main__':
    print('Tkinter 클래스 시작')
    app = View()
    app.mainloop()