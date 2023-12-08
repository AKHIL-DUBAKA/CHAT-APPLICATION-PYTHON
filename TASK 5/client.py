import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))

while True:
    message = input("Enter a message to send: ")
    if message == "quit":
        break

    client.sendall(message.encode('utf-8'))

client.close()
