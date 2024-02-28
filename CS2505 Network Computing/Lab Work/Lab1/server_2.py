# from the socket module import all
import socket
import datetime

# Create a TCP server socket
# Create a TCP socket using the "socket" method
# Hints: AF_INET is used for IPv4 protocols, SOCK_STREAM is used for TCP 
#<INSERT CALL TO CREATE THE SOCKET>
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# set values for host 'localhost' - meaning this machine and port number 10000
hostname = socket.gethostname()
ip_addr = socket.gethostbyname(hostname)
print(ip_addr)
server_address = (ip_addr, 10000)
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
        print('Connection from', client_address)
        full_message = ''
        # Receive the data in small chunks and retransmit it
        while True:
            # decode() function returns string object
            data = connection.recv(16).decode()
            if data:
                full_message += data
                print('Received "%s"' % data)
                print('Sending data back to the client')
                # encode() function returns bytes object
                in_file = open("log.txt", "a")
                now = datetime.datetime.now()
                date_string = now.strftime("%m/%d/%Y, %H:%M:%S")

                in_file.write(f"{date_string} - {data}\n")
                in_file.close()

                connection.sendall(date_string.encode())
            else:
                print(f"Full Message: {full_message}")
                print('No more data from', client_address)
                break
            
    finally:
        # Clean up the connection
        connection.close()

# now close the socket
sock.close()
