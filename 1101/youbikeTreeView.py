from tkinter import ttk
import tkinter as tk

class YoubikeTreeView(ttk.Treeview):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        #----------------設定欄位名稱----------------#
        self.heading('sna', text='站點名稱')
        self.heading('mday', text='更新時間')
        self.heading('sarea', text='行政區')
        self.heading('ar', text='地址')
        self.heading('tot', text='總車輛數')
        self.heading('sbi', text='可借')
        self.heading('bemp', text='可還')

        #----------------設定欄位寬度----------------#
        self.column('sna', width=300)
        self.column('mday', width=150)
        self.column('sarea', width=50)
        self.column('ar', width=300)
        self.column('tot', width=80)
        self.column('sbi', width=50)
        self.column('bemp', width=50)

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


def search():
    query = search_entry.get()
    selections = []
    for child in tree.get_children():
        if query.lower() in tree.item(child)['values'].lower():   # compare strings in  lower cases.
            print(tree.item(child)['values'])
            selections.append(child)
    print('search completed')
    tree.selection_set(selections)
    


    values = []

    root = tk.Tk()
    root.title("Medicine database")

    lb1 = tk.Label(root, text="Search:")
    lb1.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
    search_entry = tk.Entry(root, width=15)
    search_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.E, rowspan=1)
    btn = tk.Button(root, text="search", width=10, command=search)
    btn.grid(row=0, column=0, padx=10, pady=10, rowspan=2)
    
   
