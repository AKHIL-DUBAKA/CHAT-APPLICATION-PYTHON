import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen(5)

print("Server is listening for incoming connections...")

while True:
    client, address = server.accept()
    print(f"Connection established from {address}")

    while True:
        data = client.recv(1024)
        if not data:
            break

        print(f"Received message: {data.decode('utf-8')}")

    client.close()
