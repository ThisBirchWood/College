import socket, select

server_name = input("Server name: ")
username = input("Username: ")
port = 6789

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((server_name, port))
sock.sendall(username.encode())

while True:
    message = input()

    sock.sendall(message.encode())

    