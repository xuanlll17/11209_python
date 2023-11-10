import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datasource
from youbikeTreeView import YoubikeTreeView
from threading import Timer

class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    #-----interface-----#
        topFrame = tk.Frame(self, relief=tk.GROOVE,borderwidth=1)
        tk.Label(topFrame, text='台北市youbike即時資料', font=('arial', 20), bg='#333333', fg='#ffffff', padx=10, pady=10).pack(padx=20, pady=20)
        topFrame.pack(pady=30)

    #------treeview-----#
        bottomFrame = tk.Frame(self)
        self.youbikeTreeView = YoubikeTreeView(bottomFrame,
                                               columns=('sna','mday','sarea','ar','tot','sbi','bemp'),
                                               show="headings",
                                               height = 20)
        self.youbikeTreeView.pack(side='left')
        
        #-----scrollbar-----#
        self.scrollbar = ttk.Scrollbar(bottomFrame, orient="vertical", command=self.youbikeTreeView.yview)
        self.scrollbar.pack(side='left',fill='y')
        self.youbikeTreeView.configure(yscrollcommand=self.scrollbar.set)

        bottomFrame.pack(pady=(15,30),padx=20) #pady((上),(下))

def main():
    def update_data(w:Window)->None:

        try:
            #datasource.update_render_data()
            pass
        except Exception:                     
            messagebox.showerror('錯誤','將關閉應用程式\n請稍後再試')

        lastest_data = datasource.lastest_datetime_data()
        w.youbikeTreeView.update_content(lastest_data)
        #w.after(5*60*1000,update_data,w) #每5分鐘執行,w參數傳遞到def update_data(w)
        
        t = Timer(5*60, update_data,args=(window,))
        t.start()

    window = Window()
    window.title('台北市youbike2.0')
    window.resizable(width=False,height=False)
    #window.after(1000,update_data,window)
    
    #-----update treeview data-----#
    lastest_data = datasource.lastest_datetime_data()
    window.youbikeTreeView.update_content(lastest_data)
    t = Timer(1, update_data,args=(window,))
    t.start()
    window.mainloop()

if __name__ == '__main__':
    main()