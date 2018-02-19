# CS 3251

- Name and email address:
=> Jae Min Baek (John Baek) and jbaek7023@gmail.com

- Class name, data and assignment title:
=> Networking I (T, Th), Feb 13, First Programming Assignment

- Names and descriptions of all files submitted:
  rpnserverTCP.py : TCP server implementation
  rpnclientTCP.py : TCP client implementation
  rpnserverUDP.py : UDP server implementation
  rpnclientUDP.py : UDP client implementation
  README.txt: readme file / Protocol Description
  sample.txt: Sample testing commands and outputs

- Protocol Description for UDP and for TCP:
1) The format of the messages exchanged between client and server (see for
example how the http message format is described),
python3 rpnclientTCP.py <IP address> <port> <rpn>
=> From TCP client to the server, the format of message includes
   IP address of TCP server, port number of TCP server and the data for the payload.
   And it includes the address and port number of client to send it back
   to the client.
   The port number MUST be 13001
python3 rpnclientUDP.py <IP address> <port> <rpn>
=> From UDP client to the server, the format of message includes
   IP address of UDP server, port number of UDP server and the data for the payload.
   And it includes the address and port number of client to send it back
   to the client.
   The port number MUST be 5000
=> From TCP server to client, the message includes the address and port number
   of TCP client. It also includes the data.
=> From UDP server to client, the message includes the address and port number
   of UDP client. It also includes the data and the address and port number of UDP server.


2) How multiple compute requests are handled between client and server
Because the request has a single operation, server doesn't need to be aware
of the procedure for the multiple operations to compute the RPN statement.
=> First the client sends a request to the server with a single operation
=> Server receives and computes the request.
=> Server sends a request with the computation result data to the client
=> Client receives the request.

3) How TCP server knows that expression is complete
=> When the server doesn't get the data anymore.

4) anything else you implemented
=> UDP client deals with lost request messages or non-responding server
   by setting a timeout for two seconds for receiving a response.
  It retries the same query 3 times.
  After 3 unsuccessful request, the client prints "Closing after three connection attempts"
=> TCP and UDP servers check if the operation has three tokens
=> TCP and UDP servers validate if the operator is one of the operators we supports
=> TCP and UDP servers validate if two operands are numbers.
=> TCP and UDP clients check the number of arguments and the command argument types (such as integer or string)

- Any known bugs or limitations of your program (for example, maximum integer
value supported or maximum number of tokens allowed)
=> messages may not be longer than 269,973 characters. Each message chunk header is
   represented as a 4-digit number, meaning the maximum number of chunks is 9,999 chunks.
   The packet size is defined as 32 characters, with 5 dedicated for the header and header delimiter.
   Therefore, 9999*(32-5)=269973 is the maximum message length.
