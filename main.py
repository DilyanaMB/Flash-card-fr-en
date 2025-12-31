from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50)

card_front_image = PhotoImage(file="images/card_front.png")
canvas = Canvas(height=526, width=800)
canvas.create_image(526, 800, image=card_front_image)

label_language = canvas.create_text(400, 150, text="French", font=('Arial', 40, 'italic'), fill="white")
canvas.grid(row=0, column=0, columnspan=2)

label_language_translate = canvas.create_text(400, 263, text="trouve", font=('Arial', 60, 'bold'), fill="white")
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, bg=BACKGROUND_COLOR)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, bg=BACKGROUND_COLOR)
wrong_button.grid(row=1, column=0)

window.mainloop()
