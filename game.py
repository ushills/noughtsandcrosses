import tkinter as tk
import tkinter.font as font
import xox


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_buttons()
        self.game = xox.XOXGame()
        self.player = self.game.first_player()

    def create_buttons(self):
        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)

        one = tk.Button(self, text="1", width=3, height=2, command=lambda: self.move(1))
        one.grid(row=0, column=0)
        two = tk.Button(self, text="2", width=3, height=2, command=lambda: self.move(2))
        two.grid(row=0, column=1)
        three = tk.Button(
            self, text="3", width=3, height=2, command=lambda: self.move(3)
        )
        three.grid(row=0, column=2)
        four = tk.Button(
            self, text="4", width=3, height=2, command=lambda: self.move(4)
        )
        four.grid(row=1, column=0)
        five = tk.Button(
            self, text="5", width=3, height=2, command=lambda: self.move(5)
        )
        five.grid(row=1, column=1)
        six = tk.Button(self, text="6", width=3, height=2, command=lambda: self.move(6))
        six.grid(row=1, column=2)
        seven = tk.Button(
            self, text="7", width=3, height=2, command=lambda: self.move(7)
        )
        seven.grid(row=2, column=0)
        eight = tk.Button(
            self, text="8", width=3, height=2, command=lambda: self.move(8)
        )
        eight.grid(row=2, column=1)
        nine = tk.Button(
            self, text="9", width=3, height=2, command=lambda: self.move(9)
        )
        nine.grid(row=2, column=2)

    def move(self, square_number):
        print("You pressed", square_number)
        self.game.player_turn(self.player, square_number)
        print(self.game.board)


root = tk.Tk()
app = Application(master=root)
app.mainloop()
