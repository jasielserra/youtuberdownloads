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

        self.frame2 = Frame(self.window, pady=20)
        self.frame2.pack()

        self.label_insert = Label(self.frame2, text="  Insert link:  ", font="arial 12")
        self.label_insert.pack(side="left")

        self.link = Entry(self.frame2, font="arial 20", width=50)
        self.link.pack(side="left")

        self.play = Button(self.frame2, bg="red", text=">", bd=0, fg="white", width=4, height=2, command=None)
        self.play.pack()

        self.window.mainloop()

Downloader()