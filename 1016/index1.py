'''
文件的說明
學習 Canvas
'''
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.geometry("300x250+800+300")
        self.title("Lines")
        self.configure(background='#ED784A')        

class MyFrame(tk.Frame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)
        self.configure(background='#FEDFE1')
        self.img = Image.open("pets.png")
        self.pets = ImageTk.PhotoImage(self.img)
        canvas = tk.Canvas(self, 
                           width=self.img.size[0], #48
                           height=self.img.size[1]) #48
        canvas.create_image(24, 24, image = self.pets, anchor = tk.CENTER)
        canvas.pack()
        self.pack(expand=1, fill='both')

def main():
    '''
    param: (如果有參數在這裡說明)
    function 使用說明書
    '''
    window = Window()
    myFrame = MyFrame(window)
    window.mainloop()

if __name__ == '__main__':
    main()