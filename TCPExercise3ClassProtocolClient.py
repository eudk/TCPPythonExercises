from socket import *

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(('localhost', 14000))

while True:
    message = input("Enter a request (e.g., upper,'<string>' or 'quit' to exit): ")
    if message == 'quit':
        clientSocket.send(message.encode())
        break
    clientSocket.send(message.encode())
    response = clientSocket.recv(1024).decode()
    print(f"Server response: {response}")

clientSocket.close()
