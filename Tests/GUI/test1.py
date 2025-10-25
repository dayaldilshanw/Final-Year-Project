import tkinter as tk
from tkinter import messagebox


# Function to display real-time data
def show_realtime_data():
    # Replace these placeholders with your actual data retrieval code
    temperature = get_temperature()
    humidity = get_humidity()
    weight = get_weight()

    # Create a message with the real-time data
    message = f"Temperature: {temperature}°C\nHumidity: {humidity}%\nWeight: {weight} kg"

    messagebox.showinfo("Real-Time Data", message)


# Replace these placeholder functions with actual data retrieval logic
def get_temperature():
    # Implement code to retrieve real-time temperature data
    return 25.5  # Example value


def get_humidity():
    # Implement code to retrieve real-time humidity data
    return 60.2  # Example value


def get_weight():
    # Implement code to retrieve real-time weight data
    return 12.3  # Example value


# Create the main application window
app = tk.Tk()
app.title("Real-Time Data Display")

# Create a label
label = tk.Label(app, text="Real-Time Data Display")
label.pack(pady=10)

# Create a button to display real-time data
button = tk.Button(app, text="Show Data", command=show_realtime_data)
button.pack(pady=10)

# Start the main event loop
app.mainloop()
