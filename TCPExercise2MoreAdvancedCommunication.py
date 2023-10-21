from socket import *
import threading

def handleClient(connectionSocket, address):
    while True:
        sentence = connectionSocket.recv(1024).decode()
        print(f"Received: {sentence}")
        if sentence.lower() == "quit": 
            break #dosen't break for some reason
        capitalizedSentence = sentence.upper()
        connectionSocket.send(capitalizedSentence.encode())
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
