# UDP_Server
from socket import *
import random
import re

#probability drop packet
p = 0.5
#regular expression for checking valid expression + - * /
regex = (r'[^+\-*\/^0-9\s]')

#Open and listen to socket as a server
serverPort = 54321
serverName = '127.0.0.1'
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((serverName, serverPort))
print ("The UDP server is ready to receive\n")

#repeat step 2
while True:

    #Receive a request which consist of an operation code (OC) and two numbers
    message1, clientAddress = serverSocket.recvfrom(2048)
    message2, clientAddress = serverSocket.recvfrom(2048)
    message3, clientAddress = serverSocket.recvfrom(2048)
    print ("Received this message:" + str(message1.decode()) +" "+ str(message2.decode()) +" "+ str(message3.decode()))
    # If random number > 0.5. Drop incoming packet
    a = random.random()
    print ("Random number: " + str(a))
    if a >= p:
        print ("Your request was randomly dropped!!!")
    #Check the numbers to make sure they are valid. If true = valid
    elif message1.isdigit() and message3.isdigit() and int(message3) != 0:
        print ("Starting parse request...\n")
        #Check the OC to make sure they are valid.
        #If match regex -> Invalid. Send a return status code of 300 and the result of -1
        if re.match(regex, message2.decode('utf-8')):
            print ("Invalid request")
            resultMessage = -1
            statusMessage = "300"
            serverSocket.sendto(str(resultMessage).encode('utf-8'), clientAddress)
            serverSocket.sendto(statusMessage.encode(), clientAddress)
        # else valid
        else:
            #send a return status code of 200 and the result after computed
            if '+' in message2.decode('utf-8'):
                resultMessage = int(message1) + int(message3)
                statusMessage = "200"
                serverSocket.sendto(str(resultMessage).encode('utf-8'), clientAddress)
                serverSocket.sendto(statusMessage.encode(), clientAddress)
                print ("Your request is valid.\n")
                print ("Sent result back to client.\n")
            elif '-' in message2.decode('utf-8'):
                resultMessage = int(message1) - int(message3)
                statusMessage = "200"
                serverSocket.sendto(str(resultMessage).encode('utf-8'), clientAddress)
                serverSocket.sendto(statusMessage.encode(), clientAddress)
                print ("Your request is valid.\n")
                print ("Sent result back to client.\n")
            elif '*' in message2.decode('utf-8'):
                resultMessage = int(message1) * int(message3)
                statusMessage = "200"
                serverSocket.sendto(str(resultMessage).encode('utf-8'), clientAddress)
                serverSocket.sendto(statusMessage.encode(), clientAddress)
                print ("Your request is valid.\n")
                print ("Sent result back to client.\n")
            else:
                resultMessage = int(message1) / int(message3)
                statusMessage = "200"
                serverSocket.sendto(str(resultMessage).encode('utf-8'), clientAddress)
                serverSocket.sendto(statusMessage.encode(), clientAddress)
                print ("Your request is valid.\n")
                print ("Sent result back to client.\n")
    #Else -> invalid integer
    else:
        print ("Invalid request")
        #If the request is not valid, send a return status code of 300 and the result of -1
        resultMessage = -1
        statusMessage = "300"
        serverSocket.sendto(str(resultMessage).encode('utf-8'), clientAddress)
        serverSocket.sendto(statusMessage.encode(), clientAddress)
