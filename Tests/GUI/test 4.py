import tkinter as tk
from PIL import Image, ImageTk
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, db
import socket
from tkinter import ttk


server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a port
server_address = ("0.0.0.0", 8888)
server_socket.bind(server_address)

cred = credentials.Certificate("food-vaste-managment-firebase-adminsdk-btg0l-29deaadc28.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://food-vaste-managment-default-rtdb.firebaseio.com/'
})


def update_sensor_readings():
    data, client_address = server_socket.recvfrom(1024)

    t, h, g = data.decode().split(",")
    weight = g
    temp = t
    humidity = h


    weight_label.config(text=f"Weight: {weight} g")
    temp_label.config(text=f"Temperature: {temp} C")
      # Replace with the actual humidity value
    humidity_label.config(text=f"Humidity: {humidity} %")

    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    date_time_label.config(text=f"{current_datetime}")

    Food_Catagory = "Orange"  # Replace with the actual humidity value
    additional_text_label.config(text=f"Food Category : {Food_Catagory} ")


    root.after(1000, update_sensor_readings)




# Create the Tkinter window
root = tk.Tk()
root.title("Food Management System Dashboard")
root.state('zoomed')



# Create the main frame to contain the boxes
main_frame = tk.Frame(root)
main_frame.pack(side="right", fill="both", expand=True)  # Place it on the right side and expand it


# Create a Treeview widget
tree = ttk.Treeview(main_frame, columns=("Date", "Time", "FoodCategory", "Weight", "Humidity", "Temperature"), show="headings")

# Add the Treeview widget to the main frame
tree.grid(row=1, column=0, columnspan=4, padx=10, pady=50, sticky="n")


# Define the column headings
tree.heading("#1", text="Date")
tree.heading("#2", text="Time")
tree.heading("#3", text="Food Category")
tree.heading("#4", text="Weight")
tree.heading("#5", text="Humidity")
tree.heading("#6", text="Temperature")

# Reference to the 'Data' node
data_ref = db.reference('/Data')

# Fetch data from Firebase and add it to the tabledx
data = data_ref.get()
if data is not None:
 for key, values in data.items():
    row = (values.get('Date', ''), values.get('Time', ''), values.get('FoodCatagory', ''),
    values.get('Weight', ''), values.get('Humidity', ''), values.get('Temperature', ''))
    tree.insert("", "end", values=row)







side_frame = tk.Frame(root, bg="#ffa703")
side_frame.pack(side="left", fill="y")

label = tk.Label(side_frame, text="Dashboard", bg="#ffa703", fg="#FFF", font=("Arial", 15))
label.pack(pady=50, padx=40)
# Load image icons for weight, temp, and humidity
weight_icon = Image.open("weiw.png")
temp_icon = Image.open("tempw.png")
humidity_icon = Image.open("huw.png")
additional_icon = Image.open("orange.jpg")

resized_image = additional_icon.resize((350, 350), Image.LANCZOS)
photo = ImageTk.PhotoImage(resized_image)

# Convert icons to Tkinter PhotoImage for weight, temp, humidity, and additional image
weight_image = ImageTk.PhotoImage(weight_icon)
temp_image = ImageTk.PhotoImage(temp_icon)
humidity_image = ImageTk.PhotoImage(humidity_icon)
additional_image = ImageTk.PhotoImage(additional_icon)

# Create labels with icons to display sensor readings for weight
weight_frame = tk.Frame(main_frame, bg="#ffa703")
weight_frame.grid(row=0, column=0, padx=10, pady=50, sticky="n")  # Place it at the top, add padding, and align it to the north (top)

# Create a label for the image (icon) for weight
weight_image_label = tk.Label(weight_frame, image=weight_image, bg="#ffa703")
weight_image_label.grid(row=0, column=0, padx=10)  # Align it to the left

# Create a label for the text for weight
weight_label = tk.Label(weight_frame, text="Weight: -- kg", font=("Arial", 14))
weight_label.grid(row=0, column=1, padx=10)  # Align it to the left

# Create labels with icons to display sensor readings for temp
temp_frame = tk.Frame(main_frame, bg="#ffa703")
temp_frame.grid(row=0, column=1, padx=10, pady=50, sticky="n")  # Place it at the top, add padding, and align it to the north (top)

# Create a label for the image (icon) for temp
temp_image_label = tk.Label(temp_frame, image=temp_image, bg="#ffa703")
temp_image_label.grid(row=0, column=0, padx=10)  # Align it to the left

# Create a label for the text for temp
temp_label = tk.Label(temp_frame, text="Temperature: -- C", font=("Arial", 14))
temp_label.grid(row=0, column=1, padx=10)  # Align it to the left

# Create labels with icons to display sensor readings for humidity
humidity_frame = tk.Frame(main_frame, bg="#ffa703")
humidity_frame.grid(row=0, column=2, padx=10, pady=50, sticky="n")  # Place it at the top, add padding, and align it to the north (top)

# Create a label for the image (icon) for humidity
humidity_image_label = tk.Label(humidity_frame, image=humidity_image, bg="#ffa703")
humidity_image_label.grid(row=0, column=0, padx=10)  # Align it to the left

# Create a label for the text for humidity
humidity_label = tk.Label(humidity_frame, text="Humidity: -- %", font=("Arial", 14))
humidity_label.grid(row=0, column=1, padx=10)  # Align it to the left

# Create a frame for the additional image
additional_frame = tk.Frame(main_frame, bg="#ffa703")
additional_frame.grid(row=0, column=3, padx=10, pady=50, sticky="n")  # Place it at the top, add padding, and align it to the north (top)

# Create a label for the additional image
additional_image_label = tk.Label(additional_frame, image=photo, bg="#ffa703")
additional_image_label.grid(row=0, column=0, padx=10 , pady=6)  # Align it to the left

additional_text_label = tk.Label(additional_frame, text="Orange", font=("Arial", 12))
additional_text_label.grid(row=1, column=0, padx=10, pady=5, sticky="n")  # Align it to the north (top)

# Create a frame for the date and time label
date_time_frame = tk.Frame(main_frame, bg="#ffa703")
date_time_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nw")  # Place it at the top corner

# Create a label for the date and time
date_time_label = tk.Label(date_time_frame, text="current_datetime", font=("Arial", 12))
date_time_label.grid(row=0, column=0, padx=10 , pady=5)  # Align it to the left


# Call the function to start updating sensor readings
update_sensor_readings()
additional_image_label.image = photo
root.mainloop()