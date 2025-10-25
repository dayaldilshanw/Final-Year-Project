import socket

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a port
server_address = ("0.0.0.0", 8888)
server_socket.bind(server_address)

# Listen for incoming messages
while True:
    data, client_address = server_socket.recvfrom(1024)

   # Split the data into three variables using the comma delimiter
    t, h, g = data.decode().split(",")

    # Print the variables
    print(f"Temperature: {t}")
    print(f"Humidity: {h}")
    print(f"Weight: {g}")

   # print(data)