import tkinter as tk
from tkinter import ttk
import firebase_admin
from firebase_admin import credentials, db

# Initialize the Firebase Admin SDK with your service account key
cred = credentials.Certificate("food-vaste-managment-firebase-adminsdk-btg0l-29deaadc28.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://food-vaste-managment-default-rtdb.firebaseio.com/'
})

# Create a Tkinter window
root = tk.Tk()
root.title("Firebase Data Table")


# Create a style for the table
style = ttk.Style()

# Configure the style to set the background and text color
style.configure("Treeview",
                background="white",  # Background color
                fieldbackground="orange",  # Field background color
                foreground="black")  # Text color

# Create an orange label
orange_label = tk.Label(root, bg="orange")
orange_label.pack(fill="both", expand=True)  # Fill the entire window

# Create a Treeview widget with "show" option set to "headings"
tree = ttk.Treeview(orange_label, columns=("Date", "Time", "FoodCategory", "Weight", "Humidity", "Temperature"), show="headings")

# Define column headings
tree.heading("#1", text="Date")
tree.heading("#2", text="Time")
tree.heading("#3", text="Food Category")  # Use "FoodCategory" without spaces
tree.heading("#4", text="Weight")  # Use "Weight" without spaces
tree.heading("#5", text="Humidity")
tree.heading("#6", text="Temperature")

# Reference to the 'Data' node
data_ref = db.reference('/Data')

# Fetch data from Firebase and add it to the table
data = data_ref.get()
if data is not None:
    for key, values in data.items():
        row = (values.get('Date', ''), values.get('Time', ''), values.get('FoodCatagory', ''),  # Use "FoodCategory"
               values.get('Weight', ''), values.get('Humidity', ''), values.get('Temperature', ''))
        tree.insert("", "end", values=row)

# Add a vertical scrollbar
scrollbar = ttk.Scrollbar(orange_label, command=tree.yview, orient="vertical")
tree.configure(yscrollcommand=scrollbar.set)

# Pack the Treeview and scrollbar
tree.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

root.mainloop()
