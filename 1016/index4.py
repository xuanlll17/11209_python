'''
文件的說明
ttk LabelFrame
'''
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.geometry("300x250+800+300")
        self.title("Lines")
        #self.configure(background='#ED784A')        

class MyFrame(tk.LabelFrame):
    def __init__(self,master,title,**kwargs):
        super().__init__(master,text=title,**kwargs)
        self.pack(expand=1, fill='both', padx=10, pady=10)

    def choiced(self):
        print(self.aligement.get())

def main():
    '''
    param: (如果有參數在這裡說明)
    function 使用說明書
    '''
    window = Window()
    myFrame = MyFrame(window,title="對齊方式")
    s = ttk.Style()
    
    window.mainloop()

if __name__ == '__main__':
    main()