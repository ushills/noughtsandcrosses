from tkinter import *
from tkinter import ttk
import xox


class Application:
    def __init__(self, root):
        self.game = xox.XOXGame()
        self.root = root
        root.title("Noughts and Crosses")
        self.mainframe = ttk.Frame(root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        self.create_gui()
        self.create_buttons()

#         self.current_player = self.game.next_player()

        
        
    def create_gui(self):
        ttk.Label(self.mainframe, text="Player").grid(column=0, row=0)
        self.current_player_label_text = StringVar()
        self.current_player_label_text.set(self.game.next_player())
        self.current_player_label =  Label(self.mainframe, textvariable=self.current_player_label_text).grid(column=1, row=0,)
        ttk.Label(self.mainframe, text="turn").grid(column=3, row=0)

    def create_buttons(self):
#         self.columnconfigure(0, pad=3)
#         self.columnconfigure(1, pad=3)
#         self.columnconfigure(2, pad=3)
#         self.rowconfigure(0, pad=3)
#         self.rowconfigure(1, pad=3)
#         self.rowconfigure(2, pad=3)

        button_one = Button(
            self.mainframe, width=3, height=2, command=lambda: self.move(1, button_one)
        ).grid(row=1, column=0)
#         button_two = Button(
#             self, width=3, height=2, command=lambda: self.move(2, button_two)
#         )
#         button_two.grid(row=0, column=1)
#         button_three = Button(
#             self,
#             width=3,
#             height=2,
#             command=lambda: self.move(3, button_three),
#         )
#         button_three.grid(row=0, column=2)
#         button_four = Button(
#             self, width=3, height=2, command=lambda: self.move(4, button_four)
#         )
#         button_four.grid(row=1, column=0)
#         button_five = Button(
#             self, width=3, height=2, command=lambda: self.move(5, button_five)
#         )
#         button_five.grid(row=1, column=1)
#         button_six = Button(
#             self, width=3, height=2, command=lambda: self.move(6, button_six)
#         )
#         button_six.grid(row=1, column=2)
#         button_seven = Button(
#             self,
#             width=3,
#             height=2,
#             command=lambda: self.move(7, button_seven),
#         )
#         button_seven.grid(row=2, column=0)
#         button_eight = Button(
#             self,
#             width=3,
#             height=2,
#             command=lambda: self.move(8, button_eight),
#         )
#         button_eight.grid(row=2, column=1)
#         button_nine = Button(
#             self, width=3, height=2, command=lambda: self.move(9, button_nine)
#         )
#         button_nine.grid(row=2, column=2)

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
        if result is not False:
            print(result)
            print("Game Finished")
        print(self.game.board)


window = Tk()
app = Application(window)
window.mainloop()
