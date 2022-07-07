from tkinter import *

class Downloader:
    def __init__(self):
        self.window = Tk()
        self.window.title("Youtube Download")
        self.window.resizable(0, 0)
        self.window.geometry("1280x720+300+200")


        self.img_logo = PhotoImage(file="assets/logo.png")

        self.frame = Frame(self.window, bg="#3b3b3b", pady=80)
        self.frame.pack(fill="x")

        self.label_logo = Label(self.frame, image=self.img_logo, bg="#3b3b3b")
        self.label_logo.pack()

        self.window.mainloop()

Downloader()