import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("localhost", 6789))

while True:
    message, clientAddress = sock.recvfrom(2048)
    modifiedMessage = message.upper().strip()
    sock.sendto(modifiedMessage, clientAddress)