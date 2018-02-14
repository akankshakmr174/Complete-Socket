import socket


if __name__ == '__main__':
    host = "127.0.0.1"
    port = 5000

    # AF_INET: Internet Iv4
    # SOCK_DGRAM: UDP Protocol
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    while True:
        # 1024: Buffer Size
        data, addr = server_socket.recvfrom(1024)
        data = data.decode('utf-8')

        print('message from user: ' + str(addr))
        print('from connected user: ' + data)

        # Computation Part
        data = data.upper()

        # Printing Computed Part
        print('sending: ' + data)

        # server do we send to the client
        server_socket.sendto(data.encode('utf-8'), addr)

    # Close the Socket
    server_socket.close()
