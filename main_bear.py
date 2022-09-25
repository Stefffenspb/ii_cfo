from tkinter import *
from tkinter.filedialog import askdirectory

import os
import fnmatch
from tkinter import messagebox
class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.input_text1 = StringVar()
        self.input_text2 = StringVar()
        self.input_text3 = StringVar()
        self.master.geometry('400x400')
        self.master.title("Поиск Белого Медведя")
        self.master.resizable(width=0, height=0)
        self.master.rowconfigure(5, weight=1)
        self.master.columnconfigure(5, weight=1)
        self.grid(sticky=W+E+N+S)
        self.label4 = Label(self, text="Путь к снимкам", width=30)
        self.label4.grid(row=0, column=0, sticky=W)
        self.button = Button(self, text="Выбрать Каталог", command=self.load_file, width=20)
        self.entry = Entry(self, textvariable=self.input_text1, width=40)
        self.entry.grid(row=1, column=0, sticky=W)
        self.label2 = Label(self, text="Снимков для обработки: ", width=30)
        self.label2.grid(row=2, column=0, sticky=W)
        self.label = Entry(self, textvariable=self.input_text2, width=30)
        self.label.grid(row=3, column=0, sticky=W)
        self.button.grid(row=1, column=1, sticky=E)
        self.label3 = Label(self, text=" ", width=30)
        self.label3.grid(row=4, column=0, sticky=W)
        self.button_poisk = Button(self, text="Начать поиск Медведя", command=self.poisk_m, width=30)
        self.button_poisk.grid(row=6, column=0, sticky=N)
        self.label5 = Label(self, text="", width=30)
        self.label5.grid(row=7, column=0, sticky=W)
        self.label6 = Label(self, text="", width=30)
        self.label6.grid(row=8, column=0, sticky=W)


    def load_file(self):
        fname = askdirectory()
        count_f = len(fnmatch.filter(os.listdir(fname), '*.jpg'))
        self.input_text2.set(count_f)

        if fname:
            try:
                self.input_text1.set(fname)

            except:                     # <- naked except is a bad idea
                messagebox.showerror("Открытие Каталога", "Не возможно прочитать\n'%s'" % fname)
            return

    def poisk_m(self):
        self.after(10000, self.label5.config(text='Поиск белых медведей завершен'))
        self.label6.config(text='Результат в '+ os.path.abspath(os.curdir))
        return






if __name__ == "__main__":

    MyFrame().mainloop()