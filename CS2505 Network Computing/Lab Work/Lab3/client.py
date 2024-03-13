import socket, sys

thisfile, ip_addr, port, filename = sys.argv
port = int(port)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (ip_addr, port)


print('connecting to server at %s port %s' % server_address)

sock.connect(server_address)
print('connected!')
sock.sendall(f"GET /{filename} HTTP/1.1".encode())
message = ''

while True:
    data = sock.recv(16).decode()

    if not data:
        break

    message += data

print(message)
