import socket

server_name = input("Server name: ")
ip_addr = socket.gethostbyname(server_name)

filename = input("Filename: ")

with open(filename, "r") as f:
    data = f.readlines()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for line in data:
    length = len(line)
    sock.sendto(line.encode(), (ip_addr, 6789))
    message, serverAddress = sock.recvfrom(length)
    print(message.decode())

sock.close()
