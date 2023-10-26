import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datasource

class Window(tk.Tk):                                #繼承tkinter裡的Tk
    def __init__(self, **kwargs):                   #keyword = kw, args = 引數
        super().__init__(**kwargs)                  #呼叫父類別的__init__, self不用寫 
        try:
            datasource.update_sqlite_data()
        except Exception:                     
            messagebox.showerror('錯誤','將關閉應用程式\n請稍後再試')
            self.destroy()                          #關閉視窗
        
        





def main():
    window = Window()
    window.title('台北市youbike2.0')
    window.geometry('600x300')                      #設定視窗大小
    window.resizable(width=False,height=False)      #禁止改變視窗大小resizable
    window.mainloop()
    

if __name__ == '__main__':
    main()