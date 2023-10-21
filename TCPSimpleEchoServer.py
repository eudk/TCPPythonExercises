from socket import *

serverPort = 13000 #Sets the port number
serverSocket = socket(AF_INET, SOCK_STREAM) #Creates the socket
serverSocket.bind(('', serverPort)) #Binds the socket to the port
serverSocket.listen(1) #Listens for the connection from the client
print('Server is ready to listen') #Prints that the server is ready to listen
while True: 
    connectionSocket, addr = serverSocket.accept() #Accepts the connection from the client
    sentence = connectionSocket.recv(1024).decode() #Receives the message from the client
    capitalizedSentence = sentence.upper() #Converts the message to uppercase
    connectionSocket.send(capitalizedSentence.encode()) #Sends the message back to the client
    connectionSocket.close() #Closes the connection

    #Put port 13000 in SocketTest Client and run it