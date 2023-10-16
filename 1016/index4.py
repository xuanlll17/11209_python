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
        self.geometry("+800+300")
        self.title("Lines")
        #self.configure(background='#ED784A')        

class MyFrame(tk.LabelFrame):
    def __init__(self,master,title,**kwargs):
        super().__init__(master,text=title,**kwargs)
        self.pack(expand=1, fill='both', padx=10, pady=10)

        #標題
        heading = ttk.Label(self,text="會員登入",font=('Helvetica',20),foreground='green')
        heading.grid(column=0,row=0,columnspan=2)

        username_label = ttk.Label(self,text="使用者名稱:",font=('Helvetica',10))
        username_label.grid(column=0, row=1,pady=10,padx=(10,1))

        username_entry = ttk.Entry(self)
        username_entry.grid(column=1, row=1,padx=(0,10))

        password_label = ttk.Label(self,text="密碼:",font=('Helvetica',10))
        password_label.grid(column=0, row=2,sticky=tk.E, pady=10)
        
        password_entry = ttk.Entry(self,show="*")
        password_entry.grid(column=1, row=2,padx=(0,10))

        login_button = ttk.Button(self,text="登入")
        login_button.grid(column=1,row=3,sticky=tk.E,padx=(0,10),pady=(0,20))

    def choiced(self):
        print(self.aligement.get())

def main():
    '''
    param: (如果有參數在這裡說明)
    function 使用說明書
    '''
    window = Window()
    myFrame = MyFrame(window,title="對齊方式")
    
    window.mainloop()

if __name__ == '__main__':
    main()