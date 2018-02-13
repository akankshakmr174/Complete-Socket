#!/usr/bin/python

import socket
import sys


def Main():
    # Get Host nad port address
    arguments = sys.argv

    host = arguments[1]
    port = arguments[2]
    rpn_statement = arguments[3]

    try:
        port = int(port)
        rpn_statement = str(rpn_statement)
    except ValueError as verr:
        print("Not a valid arguments; Check your host and port address as well as RPN statement")
        sys.exit(0)
    except Exception as ex:
        print("Not a valid arguments; Check your host and port address as well as RPN statement")
        sys.exit(0)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Split the RPN Statements
    tokens = rpn_statement.split()
    print(len(tokens))

    print(tokens)
    count = 0
    for token in tokens:
        if count !== 0 && count ==3: 
            client_socket.send(rpn_statement.encode("UTF-8"))
            data = client_socket.recv(2048).decode('utf-8')

        count = count + 1


    client_socket.send(rpn_statement.encode("UTF-8"))
    data = client_socket.recv(2048).decode('utf-8')
    print(data)
    client_socket.close()


if __name__ == '__main__':
    Main()
