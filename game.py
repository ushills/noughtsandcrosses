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
        self.current_player = self.game.next_player()

    def create_buttons(self):
        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)

        button_one = tk.Button(
            self, width=3, height=2, command=lambda: self.move(1, button_one)
        )
        button_one.grid(row=0, column=0)
        button_two = tk.Button(
            self, width=3, height=2, command=lambda: self.move(2, button_two)
        )
        button_two.grid(row=0, column=1)
        button_three = tk.Button(
            self,
            width=3,
            height=2,
            command=lambda: self.move(3, button_three),
        )
        button_three.grid(row=0, column=2)
        button_four = tk.Button(
            self, width=3, height=2, command=lambda: self.move(4, button_four)
        )
        button_four.grid(row=1, column=0)
        button_five = tk.Button(
            self, width=3, height=2, command=lambda: self.move(5, button_five)
        )
        button_five.grid(row=1, column=1)
        button_six = tk.Button(
            self, width=3, height=2, command=lambda: self.move(6, button_six)
        )
        button_six.grid(row=1, column=2)
        button_seven = tk.Button(
            self,
            width=3,
            height=2,
            command=lambda: self.move(7, button_seven),
        )
        button_seven.grid(row=2, column=0)
        button_eight = tk.Button(
            self,
            width=3,
            height=2,
            command=lambda: self.move(8, button_eight),
        )
        button_eight.grid(row=2, column=1)
        button_nine = tk.Button(
            self, width=3, height=2, command=lambda: self.move(9, button_nine)
        )
        button_nine.grid(row=2, column=2)

    def move(self, square_number, button_number):
        print(
            f"You pressed {square_number}, current player is {self.game.current_player}"
        )
        if (
            self.game.player_turn(self.game.current_player, square_number)
            != "Invalid Move"
        ):
            button_number["text"] = self.game.current_player
            self.game.next_player()
        result = self.game.check_winner()
        print(result)
        print(self.game.board)


root = tk.Tk()
app = Application(master=root)
app.mainloop()
