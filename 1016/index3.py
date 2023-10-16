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
        #self.configure(background='#FEDFE1') #只有tk可以用,ttk不行
        self.aligement = tk.StringVar(value='left') #字串變數 StringVar
        #用grid layout做radio button
        #三個都要寫variagle = self.aligement才會在同一組
        ttk.Radiobutton(self,text="左邊",value='left',variable=self.aligement, command=self.choiced).grid(column=0,row=0, padx=12) #value 傳出值
        ttk.Radiobutton(self,text="中間",value='center',variable=self.aligement, command=self.choiced).grid(column=1,row=0, padx=12)
        ttk.Radiobutton(self,text="右邊",value='right',variable=self.aligement, command = self.choiced).grid(column=2,row=0, padx=12)
        self.pack(expand=1, fill='x', padx=10, pady=10)

    def choiced(self):
        print(self.aligement.get()) #取得按按鈕時的值

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