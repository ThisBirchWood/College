# from the socket module import all
import socket

# Create a TCP server socket
# Create a TCP socket using the "socket" method
# Hints: AF_INET is used for IPv4 protocols, SOCK_STREAM is used for TCP 
#<INSERT CALL TO CREATE THE SOCKET>
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# set values for host 'localhost' - meaning this machine and port number 10000
server_address = ('localhost', 10000)
# output to terminal some info on the address details
print('*** Server is starting up on %s port %s ***' % server_address)
# Bind the socket to the host and port
sock.bind(server_address)

# Listen for one incoming connections to the server
sock.listen(1)

# we want the server to run all the time, so set up a forever true while loop
while True:

    # Now the server waits for a connection
    print('*** Waiting for a connection ***')
    # accept() returns an open connection between the server and client, along with the address of the client
    connection, client_address = sock.accept()
    
    try:
        print('connection from', client_address)
        full_message = ''
        # Receive the data in small chunks and retransmit it
        while True:
            # decode() function returns string object
            data = connection.recv(32).decode()
            if data:
                full_message += data
                print('received "%s"' % data)
                print('sending data back to the client')
                # encode() function returns bytes object
                connection.sendall(data.encode())
            else:
                print(f"Full Message: {full_message}")
                print('no more data from', client_address)
                break
            
    finally:
        # Clean up the connection
        connection.close()

# now close the socket
sock.close()
