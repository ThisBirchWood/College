import socket, select

ip_addr = "localhost"
port = 6789

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((ip_addr, port))

print(f"**starting server on {ip_addr}:{port}")

sock.listen(1)

clients = [sock]

while True:

    ready = select.select(clients, [], [])

    for connection in ready[0]:
        if connection == sock:
            conn, address = sock.accept()
            print(f"**connection from {address}")
            conn.setblocking(0)
            clients.append(conn)
        else:
            m = connection.recv(1024).decode()
            print(m)

    

