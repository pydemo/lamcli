import os, time
import socket

host = os.environ.get("HOST")
port = int(os.environ.get("PORT"))

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server with the socket via our ngrok tunnel
server_address = (host, port)
sock.connect(server_address)
print("Connected to {}:{}".format(host, port))

# Send the message
i=0
import random

while True:
    s = ''.join(random.choice([chr(i) for i in range(ord('a'),ord('z'))]) for _ in range(1000))
    message = f"ping {s} {i}"
    print("Sending: {}".format(message))
    sock.sendall(message.encode("utf-8"))

    # Await a response
    data_received = 0
    data_expected = len(message)
    data=' '
    while data:
        data = sock.recv(1024)
        data_received += len(data)
        print("Received: {}".format(data.decode("utf-8")))
        print(123, data)
        data=None
        #time.sleep(1)
    i +=1
    #time.sleep(0.001)
    print(456)
sock.close()