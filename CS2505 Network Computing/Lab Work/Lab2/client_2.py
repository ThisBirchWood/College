# from the socket module import all
from socket import *
END_DELIMTER = "//:::END::://"
# Create a TCP socket using the "socket" method
# Hints: AF_INET is used for IPv4 protocols, SOCK_STREAM is used for TCP 
sock = socket(AF_INET, SOCK_STREAM)

# set values for host 'localhost' - meaning this machine and port number 10000
# the machine address and port number have to be the same as the server is using.
ip_addr = input("Server IPv4 Address: ")
port = int(input("Server Port Number: "))
server_address = (ip_addr, port)
# output to terminal some info on the address details
print('connecting to server at %s port %s' % server_address)
# Connect the socket to the host and port
sock.connect(server_address)

while True:
    # Send data
    message = input("Message: ")
    # Data is transmitted to the server with sendall()
    # encode() function returns bytes object
    sock.sendall(message.encode())

    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        # Data is read from the connection with recv()
        # decode() function returns string object
        data = sock.recv(16).decode()
        amount_received += len(data)

    sock.sendall(END_DELIMTER.encode())

    response_message = ''
    while True:
        data = sock.recv(16).decode()

        if data == END_DELIMTER:
            break
        response_message += data
        sock.sendall(data.encode())

    print(f"Message from Server: {response_message}")
