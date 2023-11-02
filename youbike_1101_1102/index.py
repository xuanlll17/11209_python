import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datasource
from youbikeTreeView import YoubikeTreeView

class Window(tk.Tk):                       #繼承tkinter裡的Tk
    def __init__(self, **kwargs):          #keyword = kw, args = 引數
        super().__init__(**kwargs)         #呼叫父類別的__init__, self不用寫 

        #----------------------update database------------------------#
        try:
            datasource.update_sqlite_data()
        except Exception:                     
            messagebox.showerror('錯誤','將關閉應用程式\n請稍後再試')
            self.destroy()                 #關閉視窗

        #------------------------interface----------------------------#
        topFrame = tk.Frame(self, relief=tk.GROOVE,borderwidth=1)
        tk.Label(topFrame, text='台北市youbike即時資料', font=('arial', 20), bg='#333333', fg='#ffffff', padx=10, pady=10).pack(padx=20, pady=20)
        topFrame.pack(pady=30)
        
        #---------------------create search frame---------------------#
        middleFrame = ttk.Labelframe(self, text='搜尋')    #frame => 容器
        tk.Label(middleFrame, text='站點名稱搜尋').pack(side='left',pady=5)    #傳出none,未來不會用到,不需要接收,直接.pack()
        search_entry = tk.Entry(middleFrame)   #entry (傳出)-> none, 如果.pack()傳到self.search_entry -> none, 所以不能.pack()
        search_entry.bind("<KeyRelease>", self.onEntryClick)
        search_entry.pack(side='left')
        
        middleFrame.pack(fill='x', padx=20)    #expand = 1->True, 0->False

        #-------------------------treeview----------------------------#
        bottomFrame = tk.Frame(self)
        self.youbikeTreeView = YoubikeTreeView(bottomFrame,
                                               columns=('sna','mday','sarea','ar','tot','sbi','bemp'),
                                               show="headings",
                                               height = 20) #加'self.' => 在整個class中被公開使用 #height行數
        self.youbikeTreeView.pack(side='left')
        
        #-------------------------scrollbar---------------------------#
        self.scrollbar = ttk.Scrollbar(bottomFrame, orient="vertical", command=self.youbikeTreeView.yview)
        self.scrollbar.pack(side='left',fill='y')
        self.youbikeTreeView.configure(yscrollcommand=self.scrollbar.set)

        bottomFrame.pack(pady=(15,30),padx=20) #pady((上),(下))
    
    #------抓出使用者輸入的值-------#
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
    def update_data(w:Window)->None:
        datasource.update_sqlite_data()

        #-------------------update treeview data----------------------#
        lastest_data = datasource.lastest_datetime_data()
        w.youbikeTreeView.update_content(lastest_data)

        window.after(180*1000,update_data,w) #每3分鐘執行一次update_data, 直到window關閉

    window = Window()
    window.title('台北市youbike2.0')
    window.resizable(width=False,height=False)
    update_data(window)
    window.mainloop()



if __name__ == '__main__':
    main()




#def update_data(w:Window)->None:              
   # datasource.update_sqlite_data()
   # w.after(6*1000,update_data,w)


#def main():
   # window = Window()
   # window.title('台北市youbike2.0')
   # window.geometry('600x300')                              #設定視窗大小
   # window.resizable(width=False,height=False)              #禁止改變視窗大小resizable
   # update_data(window)
   # window.mainloop()