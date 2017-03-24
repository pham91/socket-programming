# UDP_Client
from socket import *
serverName = '127.0.0.1'
serverPort = 54321

#open a socket to the server
clientSocket = socket(AF_INET, SOCK_DGRAM)

#variable for repeat
again = "Y"
while (again=="y") | (again=="Y"):
    #Read and display the OC and numbers first; stop if requested
    message1 = input("\nInput first number: ")
    message2 = input("\nInput operation: ")
    message3 = input("\nInput second number: ")
    print ("\n ")
    print ("Your inputed value: '" + message1 + " " + message2 + " " + message3 + "' ")

    #set d = 0.1
    d = 10

    while True:
        # Send request to server
        clientSocket.sendto(message1.encode(), (serverName, serverPort))
        clientSocket.sendto(message2.encode(), (serverName, serverPort))
        clientSocket.sendto(message3.encode(), (serverName, serverPort))

        try:
            print ("Timeout is set. Waiting for result from server...")
            # set timeout
            clientSocket.settimeout(d)
            #Receive the status code and the result from the server
            resultMessage, serverAddress =  clientSocket.recvfrom(2048)
            statusMessage, serverAddress =  clientSocket.recvfrom(2048)

            #If the status code is OK (200), display the result.
            if statusMessage.decode() == "200":
                print ("Status code 200 OK. \nThe result from server: " + resultMessage.decode())
                again = input("Do you want to repeat? (y or n)")
                break
            #anything else warn user for failure. Go to step 1
            else:
                print ("Status code 300 Invalid. \nYour input is invalid.")
                again = input("Do you want to repeat? (y or n)")
                break
        # If timeout expires
        except socket.timeout:
            print ("Timeout occured. Multiple current timeout by 2")
            #Set d=2*d
            d = 2*d
            #If d>2, raise an exception and stop!
            if d > 2:
                print("Timeout expires. The server is DEAD")
                #stop the request
                clientSocket.close()
