from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

#  --------------------- Change Word --------------------------------
def change_word():
    data = pd.read_csv("/Users/deepmangroliya/Downloads/flash-card-project-start/data/french_words.csv")
    frequency_data = pd.DataFrame(data)
    frequency_data_dict = frequency_data.to_dict(orient="records")
    new_dict = {}
    
    print(new_dict)

#  --------------------- UI --------------------------------

# window widget
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# setting canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
my_image = PhotoImage(file="/Users/deepmangroliya/Downloads/flash-card-project-start/images/card_front.png")
canvas.create_image(400, 263, image=my_image)

# text on canvas
canvas.create_text(400, 150, fill="black", text="French", font=("Arial 40 italic"))
canvas.create_text(400, 263, fill="black", text="trouve", font=("Arial 60 bold"))
canvas.grid(row=0, column=0, columnspan=2)

# buttons
wrong_button_img = PhotoImage(file="/Users/deepmangroliya/Downloads/flash-card-project-start/images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=change_word)
wrong_button.grid(row=1, column=0)
right_button_img = PhotoImage(file="/Users/deepmangroliya/Downloads/flash-card-project-start/images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0, command=change_word)
right_button.grid(row=1, column=1)

window.mainloop()
