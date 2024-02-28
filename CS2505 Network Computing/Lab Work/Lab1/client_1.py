# from the socket module import all
from socket import *

# Create a TCP socket using the "socket" method
# Hints: AF_INET is used for IPv4 protocols, SOCK_STREAM is used for TCP 
sock = socket(AF_INET, SOCK_STREAM)

# set values for host 'localhost' - meaning this machine and port number 10000
# the machine address and port number have to be the same as the server is using.
server_address = ('localhost', 10000)
# output to terminal some info on the address details
print('connecting to server at %s port %s' % server_address)
# Connect the socket to the host and port
sock.connect(server_address)

try:
    
    # Send data
    message = '''No man was ever born into this world with such a passionate love of liquor as myself, it isn't that I love liquor for the taste of it, I love the "plop" of whiskey into a glass, I love it, I love to listen to it, I love to see the cream on a pint, I love the first powerful,violent impact of a glass of whiskey when I throw it back in me and when it hits the mark below. I chase it then with a pint and thats even more beautiful still'''
    print('sending "%s"' % message)
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
        print('received "%s"' % data)

finally:
    print('closing socket')
    sock.close()
