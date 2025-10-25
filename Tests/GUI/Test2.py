from tkinter import *
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a port
server_address = ("0.0.0.0", 8888)
server_socket.bind(server_address)


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

window = Tk()
window.title("Inventory")
window.geometry('395x675')
window.resizable(False,False)
window.configure(bg= "white")

canvas = Canvas(window,bg= "black", width=395, height =135)
canvas.place(x=0, y=0)
img= PhotoImage(file="Weight1.png")
canvas.create_image(0,0,anchor=NW,image=img)


canvas2 = Canvas(window,bg= "white", width=100, height =100)
canvas2.place(x=50, y=165)
img1= PhotoImage(file="Temp.png")
canvas2.create_image(4,2,anchor=NW,image=img1)


canvas3 = Canvas(window,bg= "white", width=100, height =100)
canvas3.place(x=50, y=295)
img2= PhotoImage(file="Humid.png")
canvas3.create_image(5,1,anchor=NW,image=img2)

canvas4 = Canvas(window,bg= "white", width=100, height =100)
canvas4.place(x=50, y=425)
img3= PhotoImage(file="Weight1.png")
canvas4.create_image(0,0,anchor=NW,image=img3)

temp_label = Label(window, text="28.7°C",bg="white", fg="black", font=("helvetica", 32))
temp_label.place(x=200,y=190)

humid_label = Label(window, text="56%",bg="white", fg="black", font=("helvetica", 32))
humid_label.place(x=210,y=320)

weight_label = Label(window, text="109g",bg="white", fg="black", font=("helvetica", 32))
weight_label.place(x=210,y=450)

#temp_label.config(window, bg= "white", text=(hum+"°C" ))




window.mainloop()