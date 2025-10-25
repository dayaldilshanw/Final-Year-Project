import tkinter as tk

window = tk.Tk()
window.title("Inventory")
window.geometry('340x440')
#window.resizable(False,False)

#frame= tk.Frame()

label = tk.Label(window, text = "Temperature", fg="blue", font=("calibri",30))
label.grid(row=0, column=0)
button = tk.Button(window, text = "Temperature")
button.grid(row=1, column=0)

#frame.grid()

window.mainloop()

