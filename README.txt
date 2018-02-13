# CS 3251

- Name and email address:
=> Jae Min Baek (John Baek) and jbaek7023@gmail.com

- Class name, data and assignment title:
=> Networking I (T, Th), Feb 11, First Programming Assignment

- Names and descriptions of all files submitted:
  rpnserverTCP.py : TCP server code
  rpnclientTCP.py : TCP client code
  rpnserverUDP.py : UDP server code
  rpnclientUDP.py : UDP client code
  README.txt: Project description

- Protocol Description for UDP and for TCP:
1) The format of the messages exchanged between client and server (see for
example how the http message format is described),
=> 결과 스탭으로 RPN Calculation

2) How multiple compute requests are handled between client and server
=> Client 에서 Parsing후에 Server에서 single computation. Client에서 더해서 결과냄.

3) How TCP server knows that expression is complete
=> when they don't get the data anymore.

4) anything else you implemented
=> UDP timeout. Single support. timeout, ~~.

- Any known bugs or limitations of your program (for example, maximum integer
value supported or maximum number of tokens allowed)
=> maximum integer value supported: -> oo.
=> maximum number of tokens allowed.
