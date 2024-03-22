import socket, select

server_name = input("Server name: ")
ip_addr = socket.gethostbyname(server_name)

filename = input("Filename: ")

with open(filename, "r") as f:
    data = f.readlines()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setblocking(0)

line_index = 0
while line_index < len(data):
    line = data[line_index]

    length = len(line)
    sock.sendto(line.encode(), (ip_addr, 6789))

    ready = select.select([sock], [], [], 1)
    if ready[0]:
        message, serverAddress = sock.recvfrom(length)
        print(message.decode())
        line_index += 1

sock.close()
