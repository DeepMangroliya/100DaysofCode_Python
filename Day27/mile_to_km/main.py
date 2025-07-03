from tkinter import *

def convert():
    miles = float(miles_inp.get())
    km = round(miles * 1.60934)
    return_label.config(text=f"{km}")


window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=400, height=300)
window.config(padx=20, pady=20)

#entry
miles_inp = Entry(width=7)
# input.pack()
miles_inp.grid(row=0, column=1)
# print(miles_inp.get())

#miles label
miles_label = Label(text="Miles", font=("Arial", 20, "bold"))
miles_label.grid(row=0, column=2)

# is equal to
equal_label = Label(text="is equal to", font=("Arial", 20, "bold"))
equal_label.grid(row=1, column=0)

return_label = Label()
return_label.grid(row=1, column=1)


# km label
km_label = Label(text="KM", font=("Arial",20,"bold"))
km_label.grid(row=1, column=2)

#button
calculate_button = Button(text="Calculate", command=convert)
calculate_button.grid(row=2, column=1)

window.mainloop()
