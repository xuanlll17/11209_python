import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datasource
from youbikeTreeView import YoubikeTreeView
from threading import Timer
from threading import Thread
import time

class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    #-----interface-----#
        topFrame = tk.Frame(self, relief=tk.GROOVE,borderwidth=1)
        tk.Label(topFrame, text='台北市youbike即時資料', font=('arial', 20), bg='#333333', fg='#ffffff', padx=10, pady=10).pack(padx=20, pady=20)
        topFrame.pack(pady=30)

    #-----create search frame-----#
        middleFrame = ttk.Labelframe(self, text='搜尋')    #frame => 容器
        tk.Label(middleFrame, text='站點名稱搜尋').pack(side='left',pady=5)    #傳出none,未來不會用到,不需要接收,直接.pack()
        search_entry = tk.Entry(middleFrame)   #entry (傳出)-> none, 如果.pack()傳到self.search_entry -> none, 所以不能.pack()
        search_entry.bind("<KeyRelease>", self.onEntryClick)
        search_entry.pack(side='left')
        
        middleFrame.pack(fill='x', padx=20)    #expand = 1->True, 0->False

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

        #-----抓出使用者輸入的值-----#
    def onEntryClick(self, event):
        searchEntry = event.widget          #event.widget -> 抓到entry參考, 所以entry不用加'self.'
        input_value = searchEntry.get()     #使用者輸入的文字
        if input_value == '':
            lastest_data = datasource.lastest_datetime_data()
            self.youbikeTreeView.update_content(site_datas=lastest_data)
        else:
            search_data = datasource.search_sitename(word=input_value)
            #print(search_data)
            self.youbikeTreeView.update_content(site_datas=search_data)

def main():
    def update_data(w:Window)->None: # w:Window 傳進來的參數
        
        global t
        try:
            datasource.update_render_data()
            #pass
        except Exception:                     
            messagebox.showerror('錯誤','將關閉應用程式\n請稍後再試')

        lastest_data = datasource.lastest_datetime_data()
        try:
            w.youbikeTreeView.update_content(lastest_data)
            
        except RuntimeError: # 次執行中心會產生RuntimeError的錯誤
            return
        
        #w.after(5*60*1000,update_data,w) #每5分鐘執行,w參數傳遞到def update_data(w)
        t = Timer(5*60, update_data,args=(window,)) # args = ()(tuple) -> window,
        
        t.start()

    global t, window # 建立才要用global 
    window = Window()
    window.title('台北市youbike2.0')
    window.resizable(width=False,height=False)
    window.protocol("WM_DELETE_WINDOW", on_closing) # register -> 只寫function名，表示註冊，非執行
    #window.after(1000,update_data,window)
    
    #-----update treeview data-----#
    lastest_data = datasource.lastest_datetime_data()
    window.youbikeTreeView.update_content(lastest_data)
    t = Timer(1, update_data,args=(window,))
    #print(id(t))
    t.start()
    window.mainloop()

def on_closing():
    datasource.threadRun = False
    window.destroy()
    t.cancel() # 使用不需要加global

if __name__ == '__main__':
    t = None
    window = None
    main()