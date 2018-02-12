import socket
import sys


def Main():
    host = ‘127.0.0.1’
    port = 5001

    server_address = (‘127.0.0.1’, 5000)  # server address

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.bind((host, port))

    message = input(“->”)
    while message != ‘q’:
        client_socket.sendto(message.encode(“utf-8”), server))  # send to server
        data, addr = s.recvfrom(2048)
        data = data.decode(“utf-8”)
        print(“Received from server: “+data)
        message = input(“->”)

    s.close()
