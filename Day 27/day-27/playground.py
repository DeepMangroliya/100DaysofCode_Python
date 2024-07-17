# def add(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total
#
# print(add((5, 7, 13))

from tkinter import *

window = Tk()
window.title("This is GUI Program")
window.minsize(width=500, height=300)

#Label

my_label = Label(text="Label", font=("Arial", 20, "bold"))
my_label.pack()  #side="left"


#Button
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)
# or
#     my_label.config(text="Button got Clicked2")

button = Button(text="Click me", command=button_clicked)
button.pack()

#input
input = Entry(width=10)
input.pack()
print(input.get())
# submit_button = Button(text="Submit", command = input.get()).pack()
# print(submit_button)

# my_label2 = Label(text="Click hereeee", font=("Arial", 20, "bold"))
# my_label2.pack()
window.mainloop()
