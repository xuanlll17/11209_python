import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datasource
from threading import Timer

class Window(tk.Tk):                       #繼承tkinter裡的Tk
    def __init__(self, **kwargs):          #keyword = kw, args = 引數
        super().__init__(**kwargs)         #呼叫父類別的__init__, self不用寫 
        try:
            datasource.update_sqlite_data()
        except Exception:                     
            messagebox.showerror('錯誤','將關閉應用程式\n請稍後再試')
            self.destroy()                 #關閉視窗


def on_closing(w:Window): #傳window進來
    print("window關閉")
    t.cancel()      #global t
    w.destroy()


t = None                              #全域變數
def update_data()->None:              #主執行序關閉會一起關閉
    datasource.update_sqlite_data()
    global t                          #global t -> t = None的t
    t = Timer(20, update_data)        #每20秒一次 #t = global t #update_data 自己呼叫自己 一直執行
    t.start()       #global t


def main():
    window = Window()
    window.title('台北市youbike2.0')
    window.geometry('600x300')                              #設定視窗大小
    window.resizable(width=False,height=False)              #禁止改變視窗大小resizable
    update_data()
    #window.protocol("WM_DELETE_WINDOW", on_closing)        #當按到關閉,執行on_closing() #WM_DELETE_WINDOW不能更動
    window.protocol("WM_DELETE_WINDOW", lambda:on_closing(window))      #匿名的fun:lambda
    window.mainloop()
    

#t = None
#def main():
    #def on_closing():
    #    print("window關閉")
    #    t.cancel()
    #    window.destroy()

    
    #def update_data()->None:
    #    datasource.updata_sqlite_data()
    #    global t
    #    t = Timer(20,update_data)
    #    t.start()  

    #window = Window()
    #window.title('台北市youbike2.0')
    #window.geometry('600x300')
    #window.resizable(width=False,height=False)
    #update_data()
    #window.protocol("WM_DELETE_WINDOW",on_closing)  #註冊視窗關閉,關閉update_data執行    
    #window.mainloop()




if __name__ == '__main__':
    main()