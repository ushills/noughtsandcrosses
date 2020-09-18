from tkinter import *
from tkinter import ttk
import xox


class Application:
    def __init__(self, root):
        self.game = xox.XOXGame()

        self.root = root
        root.title("Noughts and Crosses")
        self.mainframe = ttk.Frame(root, padding=10)
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        self.create_gui()
        self.create_buttons()

    def create_gui(self):
        self.current_player_label_text = StringVar()
        self.current_player = self.game.next_player()
        self.current_player_label_text.set("Player: " + self.current_player)
        self.current_player_label = Label(
            self.mainframe, textvariable=self.current_player_label_text
        ).grid(
            columnspan=3,
            row=0,
        )
        self.winner_label_text = StringVar()
        self.winner_label = Label(
            self.mainframe,
            textvariable=self.winner_label_text,
        ).grid(
            columnspan=3,
            row=5,
        )

    def create_buttons(self):
        self.mainframe.columnconfigure(0, pad=3)
        self.mainframe.columnconfigure(1, pad=3)
        self.mainframe.columnconfigure(2, pad=3)
        self.mainframe.rowconfigure(1, pad=3)
        self.mainframe.rowconfigure(2, pad=3)
        self.mainframe.rowconfigure(3, pad=3)

        self.button_one = Button(
            self.mainframe,
            width=3,
            height=2,
            command=lambda: self.move(1, self.button_one),
        )
        self.button_one.grid(row=1, column=0)

        self.button_two = Button(
            self.mainframe,
            width=3,
            height=2,
            command=lambda: self.move(2, self.button_two),
        )
        self.button_two.grid(row=1, column=1)

        self.button_three = Button(
            self.mainframe,
            width=3,
            height=2,
            command=lambda: self.move(3, self.button_three),
        )
        self.button_three.grid(row=1, column=2)

        self.button_four = Button(
            self.mainframe,
            width=3,
            height=2,
            command=lambda: self.move(4, self.button_four),
        )
        self.button_four.grid(row=2, column=0)

        self.button_five = Button(
            self.mainframe,
            width=3,
            height=2,
            command=lambda: self.move(5, self.button_five),
        )
        self.button_five.grid(row=2, column=1)

        self.button_six = Button(
            self.mainframe,
            width=3,
            height=2,
            command=lambda: self.move(6, self.button_six),
        )
        self.button_six.grid(row=2, column=2)

        self.button_seven = Button(
            self.mainframe,
            width=3,
            height=2,
            command=lambda: self.move(7, self.button_seven),
        )
        self.button_seven.grid(row=3, column=0)

        self.button_eight = Button(
            self.mainframe,
            width=3,
            height=2,
            command=lambda: self.move(8, self.button_eight),
        )
        self.button_eight.grid(row=3, column=1)

        self.button_nine = Button(
            self.mainframe,
            width=3,
            height=2,
            command=lambda: self.move(9, self.button_nine),
        )
        self.button_nine.grid(row=3, column=2)

    def move(self, square_number, button_number):
        if (
            self.game.player_turn(self.game.current_player, square_number)
            != "Invalid Move"
        ):
            button_number["text"] = self.game.current_player
            button_number["relief"] = 'sunken'
            next_player = self.game.next_player()
            self.current_player_label_text.set("Player: " + next_player)
            winner = self.game.check_winner()

        if winner is not False:
            self.winner_label_text.set(winner)



window = Tk()
app = Application(window)
window.mainloop()
