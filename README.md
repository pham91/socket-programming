# socket-programming

#### The UDP client:
------
The client sends an Operation Code (OC), and two numbers.
OC can be: Addition, Subtraction, Multiplication , and Division.
To make the problem simple, your client sends two integer numbers.
There is a possibility that the client does not receive a reply and it repeats sending the request.
The client uses a technique known as exponential backoff, where its attempts become less and
less frequent. This technique is used in other well-known communication protocols, such as
CSMA/CD, the underlying protocol of Ethernet.
The client sends it initial request and waits for certain amount of time (in our case d=0.1
second). If it does not receive a reply, it retransmits the request, but this time waits twice the
previous amount, 2*d. It repeats this process, each time waiting for a time equal to twice the
length of previous cycle. This process is repeated until the wait time exceed 2 second. At which
time, the client sends a warning that the server is “DEAD” and aborts.
The two numbers and the OC are read from the user via keyboard. Your program.
1. Read and displays the OC and numbers first,
a. Set d=0.1
2. Send the request to the server
3. Wait (start a timeout) for d seconds
4. If timeout expires (before a reply comes back),
a. Set d=2*d
b. If d>2, raise an exception and stop!
c. Otherwise go to step 2
5. If receive a reply before timeout, check the status code and the result from the server.
6. If the status code is OK (200), display the result. And if the status code is anything else
(say 300), warn the user of the failure.
7. Go to step 1.


#### The UDP Server:
------
The server performs the operation (OC) requested on the two numbers it receives from the
sender and returns the result. More specifically the server must
1. Open a socket as a server and
2. listen to the socket
3. Receive a request
4. Randomly (with probability .5) drop the request and go to step 2.
5. Parse the request (which consist of an operation code (OC) and two numbers)
6. Check to OC and the numbers to make sure they are valid.
7. If the request is not valid, it sends a return status code of 300 and the result of -1 (to be
consistent) and goes to Step 2
Invalid requests are:
• Invalid OC
• Invalid operands
o Operands not integers
o Division by zero (0).
8. If the request is valid, performs the operation and returns a status code of “200” and
the result.
9. Goes to Step 2
