import tkinter as tk
from tkinter import ttk
import datasource


class Window(tk.Tk):
    pass

def main():
    def update_data(w:Window)->None:
        datasource.update_render_data()

        w.after(5*60*1000,update_data,w) #每5分鐘執行,w參數傳遞到def update_data(w)

    window = Window()
    window.title('台北市youbike2.0')
    window.resizable(width=False,height=False)
    update_data(window)
    window.mainloop()

if __name__ == '__main__':
    main()