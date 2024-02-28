# from the socket module import all
from socket import *
from math import ceil

# Create a TCP socket using the "socket" method
# Hints: AF_INET is used for IPv4 protocols, SOCK_STREAM is used for TCP 
sock = socket(AF_INET, SOCK_STREAM)

# set values for host 'localhost' - meaning this machine and port number 10000
# the machine address and port number have to be the same as the server is using.
hostname = gethostname()
ip_addr = gethostbyname(hostname)
print(ip_addr)
server_address = (ip_addr, 10000)
# output to terminal some info on the address details
print('connecting to server at %s port %s' % server_address)
# Connect the socket to the host and port
sock.connect(server_address)

try:
    
    # Send data
    message = input("Send message: ")
    print('sending "%s"' % message)
    # Data is transmitted to the server with sendall()
    # encode() function returns bytes object
    sock.sendall(message.encode())
    
    for i in range(ceil(len(message)/16)*2):
    	# Data is read from the connection with recv()
        # decode() function returns string object
        data = sock.recv(16).decode()
        print('received "%s"' % data)

finally:
    print('closing socket')
    sock.close()
