import socket
import sys


def Main():
    # Get Host nad port address

    host = ''
    port = 0

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    message = input("->")
    while message != 'q':
        client_socket.send(message.encode("UTF-8"))
        data = client_socket.recv(2048).decide('utf-8')
        print("Received from server: "+data)
        message = input("->")
    client_socket.close()


if __name__ == '__main__':
    Main()
