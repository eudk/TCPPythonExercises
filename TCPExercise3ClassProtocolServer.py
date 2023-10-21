from socket import *
import threading

def handleClient(connectionSocket, address):
    while True:
        request = connectionSocket.recv(1024).decode()
        if not request:
            break

        # Parse the request and apply the protocol
        parts = request.split(',')
        if len(parts) == 2: #len(parts) is the number of elements in the list
            action, data = parts #unpacks the list into two variables
            if action == 'quit':
                break
            elif action == 'upper':
                response = data.upper()
            elif action == 'lower':
                response = data.lower()
            elif action == 'count':
                response = str(len(data)) #counts the number of characters in the string , len means length
            elif action == 'swapcase':
                response = data.swapcase() #swaps the case of the string
            elif action == 'reverse':
                response = data[::-1] #reverses the string
            else:
                response = "Invalid action"
        else:
            response = "Invalid request format"

        connectionSocket.send(response.encode())

    connectionSocket.close()

serverPort = 14000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)
print('Server is ready to listen')

while True:
    connectionSocket, addr = serverSocket.accept()
    print(f'Connected to {addr}')
    threading.Thread(target=handleClient, args=(connectionSocket, addr)).start()
