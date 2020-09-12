import tkinter as tk
import tkinter.font as font


window = tk.Tk()
window.title("Noughts and Crosses")

# Create the labels
main_label = tk.Label(window, text="Noughts and Crosses")


def button_handler(value):
    print(value)
    return value


# Create the buttons
button_numbers = range(1, 10)
button_font = font.Font(family="Helvetica", size=32)
buttons = []
for button_number in button_numbers:
    button = tk.Button(
        window,
        text=button_number,
        width=3,
        height=2,
        command=lambda: print(button_number),
    )
    button["font"] = button_font
    buttons.append[button[button_number]]


# add the elements to the grid
main_label.grid(row=1, column=0, columnspan=5)


window.mainloop()
