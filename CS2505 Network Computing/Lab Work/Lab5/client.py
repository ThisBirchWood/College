import socket, sys, select, datetime
from time import perf_counter

thisfile, num_pings, ip_addr = sys.argv

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setblocking(0)

i = 1
while i <= int(num_pings):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S.%f")
    print(f"Pinging {ip_addr}...")

    message = f"Ping {i} {current_time}"
    length = len(message)

    start = perf_counter()
    sock.sendto(message.encode(), (ip_addr, 6789))
    ready = select.select([sock], [], [], 1)

    if ready[0]:
        end = perf_counter()
        message, serverAddress = sock.recvfrom(length)
        print(f"Reply from {ip_addr}, time={(end-start)*1000}ms")
        i += 1
    else:
        print(f"Request timed out.")

sock.close()
input()