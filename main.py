from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Widget Examples")
window.config(padx=50, pady=50)

card_front_image=PhotoImage(file="images/card_front.png")
flash_card = Canvas(height=526, width=800)
flash_card.create_image(100, 100, image=card_front_image)



right_image=PhotoImage(file="images/right.png")
right_button = Button(image=right_image,bg=BACKGROUND_COLOR)
right_button.grid(row=1,column=1)

wrong_image=PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image,bg=BACKGROUND_COLOR)
wrong_button.grid(row=1,column=0)


label_language = Label(text="French", font=("Arial", 40, "italic"),fg="black",bg=BACKGROUND_COLOR)
label_language.grid(row=0,column=0)
window.mainloop()