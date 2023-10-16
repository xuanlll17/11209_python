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
        self.configure(background='#ED784A')        

class MyFrame(ttk.LabelFrame):
    def __init__(self,master,title,**kwargs):
        super().__init__(master,text=title,**kwargs)
        self.aligement = tk.StringVar(value='left')
        ttk.Radiobutton(self,text="左邊",value='left',variable=self.aligement, command=self.choiced).grid(column=0,row=0, padx=12) 
        ttk.Radiobutton(self,text="中間",value='center',variable=self.aligement, command=self.choiced).grid(column=1,row=0, padx=12)
        ttk.Radiobutton(self,text="右邊",value='right',variable=self.aligement, command = self.choiced).grid(column=2,row=0, padx=12)
        self.pack(expand=1, fill='both', padx=10, pady=10)
        print(self.config('style')) # config/configure都可
        print(self.winfo_class()) #查標籤名稱: TLabelframe
        self.style = ttk.Style()
        self.style.configure('TLabelframe.Label',font=('Helvetica',20),foreground='yellow',background = 'white') #改TLabelframe內的樣式(對齊方式)

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
    print(s.theme_names())
    print(s.theme_use())
    print(s.theme_use())
    window.mainloop()

if __name__ == '__main__':
    main()