from tkinter import *

class Downloader:
    def __init__(self):
        self.window = Tk()
        self.window.title("Youtube Download")
        self.window.resizable(0, 0)
        self.window.geometry("1280x720+300+200")
        self.window.mainloop()

Downloader()