import tkinter as tk
import tkinter.font as font


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_buttons()

    def create_buttons(self):
        #         self.hi_there = tk.Button(self)
        #         self.hi_there["text"] = "Hello World\n(click me)"
        #         self.hi_there["command"] = self.say_hi
        #         self.hi_there.pack(side="top")
        #
        #         self.quit = tk.Button(self, text="QUIT", fg="red",
        #                               command=self.master.destroy)
        #         self.quit.pack(side="bottom")
        self.button = []
        for i in range(9):
            self.button.append(
                tk.Button(
                    self, text=str(i + 1), command=lambda i=i+1: self.move(i)
                )
            )
            self.button[i].grid(column=4, row=i + 1)

    def move(self, square_number):
        print("You pressed", square_number)


root = tk.Tk()
app = Application(master=root)
app.mainloop()
