import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from Data1 import fruit_data


plt.rcParams["axes.prop_cycle"] = plt.cycler(color=["#4C2A85"])

# Chart 1: Bar chart of sales data
fig1, ax1 = plt.subplots()
ax1.bar(fruit_data.keys(), fruit_data.values())
ax1.set_title("Data")
ax1.set_xlabel("Fruit")
ax1.set_ylabel("Weight")

root = tk.Tk()
root.title("Inventory")
root.state('zoomed')

side_frame = tk.Frame(root, bg="#4C2A85")
side_frame.pack(side="left", fill="y")

label = tk.Label(side_frame, text="Dashboard", bg="#4C2A85", fg="#FFF", font=25)
label.pack(pady=400, padx=100)

charts_frame = tk.Frame(root)
charts_frame.pack()

upper_frame = tk.Frame(charts_frame)
upper_frame.pack(fill="both", expand=True)

canvas1 = FigureCanvasTkAgg(fig1, upper_frame)
canvas1.draw()
canvas1.get_tk_widget().pack(side="left", fill="both", expand=True)



root.mainloop()
