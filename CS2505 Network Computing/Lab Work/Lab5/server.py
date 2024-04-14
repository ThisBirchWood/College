import socket, random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("localhost", 6789))

while True:
    message, clientAddress = sock.recvfrom(2048)

    ran = random.randint(0, 10)

    if ran > 5:
        print(message.decode(), clientAddress[0])
        sock.sendto(message, clientAddress)

sock.close()