from tkinter import *
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    try:
        data_left = pandas.read_csv("data/words_to_learn.csv")
        left_to_learn = data_left.to_dict(orient="records")
    except FileNotFoundError:
        file = open('data/words_to_learn.csv', 'w')
        current_card = random.choice(to_learn)
        to_learn.remove(current_card)
        file.write(current_card)
    else:
        current_card = random.choice(left_to_learn)
    finally:
        canvas.itemconfig(card_title, text='French', fill='black')
        canvas.itemconfig(card_word, text=current_card['French'], fill='black')
        canvas.itemconfig(card_background, image=card_front_image)
        flip_timer=window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')
    canvas.itemconfig(card_background, image=card_back_image)


window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="", font=('Arial', 40, 'italic'), fill='black')
card_word = canvas.create_text(400, 263, text="", font=('Arial', 60, 'bold'), fill="black")

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()

window.mainloop()
