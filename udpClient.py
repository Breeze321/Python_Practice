#!/usr/bin/env python3

import socket 

target = "127.0.0.1"
port = 53

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(b"PLOKOON", (target, port))

data , add = client.recvfrom(4096)

print(data.decode())
client.close()
