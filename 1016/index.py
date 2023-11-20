'''
文件的說明
學習 Canvas 畫線
'''
import tkinter as tk
from tkinter import ttk #使用ttk(新)(沒有全部)要從tkinter裡import, tkinter裡放tk(舊)

class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.geometry("400x250+300+300") #"+300(x軸)+300(y軸)" 視窗打開會在這個位置
        self.title("Lines")
        self.configure(background='#ED784A')        

class MyFrame(tk.Frame): #(tk.Frame) -> 繼承tk.Frame
    def __init__(self,master,**kwargs): #自訂class一定要有__init__
        super().__init__(master,**kwargs) #(呼叫) master = master/ master 相同
        self.configure(background='#FEDFE1')
        canvas = tk.Canvas(self)
        canvas.create_line(15, 30, 200, 30) #canvas預設無大小, 設定pack
        canvas.create_line(300, 35, 300, 200, dash=(4, 2))
        canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)
        canvas.pack(expand=1, fill='both')
        self.pack(expand=1, fill='both') #expand = 1(True)/0(False)先擴充, 在填滿 fill = 'both兩邊/x上下/y左右' 

def main():
    '''
    param: (如果有參數在這裡說明)
    function 使用說明書
    '''
    window = Window()
    myFrame = MyFrame(window) #window -> master
    window.mainloop() #一定是最後執行

if __name__ == '__main__':
    main()