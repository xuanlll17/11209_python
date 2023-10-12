import dataSource   #自訂module
import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):    #繼承tk.TK
    def __init__(self, **kwargs):   #**kwargs 轉換為引數名稱呼叫(沒有限定數量)    #父類別有default value時
        #super() 執行父類別
        super().__init__(**kwargs)  #super().__init__ 繼承父類別的__init__
        self.title("這是我的第一個視窗")    
        label = tk.Label(self,text="Hello! Tkinter!", font=('Helvetica', '30'))
        label.pack(padx=100,pady=50)

def main():
   window = Window()
   window.mainloop()


if __name__ == "__main__":
    main()  #呼叫main function