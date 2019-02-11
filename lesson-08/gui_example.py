import tkinter
from tkinter import messagebox
import random

secret = random.randint(1, 100)

window = tkinter.Tk()

# greeting text
greeting = tkinter.Label(window, text="Guess the secret number!")
greeting.pack()

# guess entry field
guess = tkinter.Entry(window)
guess.pack()


# check guess
def check_guess():
    if int(guess.get()) == secret:
        result_text = "CORRECT!"
    elif int(guess.get()) > secret:
        result_text = "WRONG! Your guess is too high."
    else:
        result_text = "WRONG! Your guess is too low."

    messagebox.showinfo("Result", result_text)


# submit button
submit = tkinter.Button(window, text="Submit", command=check_guess)  # check_guess, not check_guess()
submit.pack()

window.mainloop()
