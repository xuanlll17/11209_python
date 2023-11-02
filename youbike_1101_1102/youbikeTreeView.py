from tkinter import ttk
import tkinter as tk
from tkinter.simpledialog import Dialog

class YoubikeTreeView(ttk.Treeview):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.parent = parent   #加'self.' -> 實體(attribute) #整個class的任何地方都可以用
        #---------------設定欄位名稱-----------------#
        self.heading('sna', text='站點名稱')
        self.heading('mday', text='更新時間')
        self.heading('sarea', text='行政區')
        self.heading('ar', text='地址')
        self.heading('tot', text='總車輛數')
        self.heading('sbi', text='可借')
        self.heading('bemp', text='可還')

        #---------------設定欄位寬度-----------------#
        self.column('sna', width=300)
        self.column('mday', width=150)
        self.column('sarea', width=50)
        self.column('ar', width=300)
        self.column('tot', width=80)
        self.column('sbi', width=50)
        self.column('bemp', width=50)

        #---------------bind button1-----------------#
        self.bind('<ButtonRelease-1>', self.selectedItem)

    def update_content(self,site_datas):
        '''
            更新內容
        '''
        #清除所有內容
        for i in self.get_children():
            self.delete(i)

        for site in site_datas:
            #'end'每插入一筆到最後
            self.insert('','end',values=site)

    def selectedItem(self,event):
        selectedItem = self.focus()
        data_dict = self.item(selectedItem)
        data_list = data_dict['values']
        title = data_list[0]
        detail = ShowDetail(self.parent, data=data_list, title=title)

   
class ShowDetail(Dialog):
    def __init__(self, parent, data, **kwargs):  #parent名稱可以更改
        self.sna = data[0]   #attribute #資料傳進來
        self.mday = data[1]
        self.sarea = data[2]
        self.ar = data[3]
        self.tot = data[4]
        self.sbi = data[5]
        self.bemp = data[6]
        super().__init__(parent, **kwargs)
        

    def body(self, master):
        #super().body(master)
        mainFrame = tk.Frame(master)
        mainFrame.pack(padx=100, pady=100)

        #------Label------#
        tk.Label(mainFrame, text='站點名稱').grid(column=0, row=0)
        tk.Label(mainFrame, text='更新時間').grid(column=0, row=1)
        tk.Label(mainFrame, text='行政區').grid(column=0, row=2)
        tk.Label(mainFrame, text='地址').grid(column=0, row=3)
        tk.Label(mainFrame, text='總車輛數').grid(column=0, row=4)
        tk.Label(mainFrame, text='可借').grid(column=0, row=5)
        tk.Label(mainFrame, text='可還').grid(column=0, row=6)

        #------Entry------#
        snaVar = tk.StringVar()
        snaVar.set(self.sna)
        tk.Entry(mainFrame,textvariable=snaVar, state="disabled").grid(column=1, row=0)

        mdayvar = tk.StringVar()
        mdayvar.set(self.mday)
        tk.Entry(mainFrame,textvariable=mdayvar, state='disabled').grid(column=1, row=1)

        sareavar = tk.StringVar()
        sareavar.set(self.sarea)
        tk.Entry(mainFrame,textvariable=sareavar, state='disabled').grid(column=1, row=2)

        arvar = tk.StringVar()
        arvar.set(self.ar)
        tk.Entry(mainFrame,textvariable=arvar, state='disabled').grid(column=1, row=3)
        
        totvar = tk.StringVar()
        totvar.set(self.tot)
        tk.Entry(mainFrame,textvariable=totvar, state='disabled').grid(column=1, row=4)

        sbivar = tk.StringVar()
        sbivar.set(self.sbi)
        tk.Entry(mainFrame,textvariable=sbivar, state='disabled').grid(column=1, row=5)

        bempvar = tk.StringVar()
        bempvar.set(self.bemp)
        tk.Entry(mainFrame,textvariable=bempvar, state='disabled').grid(column=1, row=6)