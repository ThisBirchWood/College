# from the socket module import all
import socket

END_DELIMTER = "//:::END::://"

# Create a TCP server socket
# Create a TCP socket using the "socket" method
# Hints: AF_INET is used for IPv4 protocols, SOCK_STREAM is used for TCP 
#<INSERT CALL TO CREATE THE SOCKET>
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# set values for host 'localhost' - meaning this machine and port number 10000
port = int(input("Port: "))

hostname = socket.gethostname()
ip_addr = socket.gethostbyname(hostname)

server_address = (ip_addr, port)
# output to terminal some info on the address details
print('*** Server is starting up on %s port %s ***' % server_address)
# Bind the socket to the host and port
sock.bind(server_address)

# Listen for one incoming connections to the server
sock.listen(1)

# Now the server waits for a connection
print('*** Waiting for a connection ***')
# accept() returns an open connection between the server and client, along with the address of the client
connection, client_address = sock.accept()

print('connection from', client_address)

# we want the server to run all the time, so set up a forever true while loop
while True:
    full_message = ''

    while True:
        data = connection.recv(16).decode()

        if data == END_DELIMTER:
            break
        full_message += data
        connection.sendall(data.encode())

    print(f"Message from {client_address[0]}: {full_message}")


    message = input("Message: ")
    connection.sendall(message.encode())

    amount_recieved = 0
    amount_expected = len(message)

    while amount_recieved < amount_expected:
        data = connection.recv(16).decode()
        amount_recieved += len(data)

    connection.sendall(END_DELIMTER.encode())
