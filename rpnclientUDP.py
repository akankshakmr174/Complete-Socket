import socket
import sys


def Main():
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

    server_address = ("127.0.0.1", 5000)  # server address

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.bind((host, port))

    # Set time out for 2 seconds
    client_socket.settimeout(2)
    request_count = 0

    while request_count <= 3:
        try:
            # Sending a request
            request_count = request_count + 1
            client_socket.sendto(rpn_statement.encode('utf-8'), server_address)
            data, addr = client_socket.recvfrom(2048)
            data = data.decode('utf-8')
            print(data)
        except socket.timeout:
            print("Connection Timeout")
        except socket.error:
            print("Error Occured")

    client_socket.close()


if __name__ == "__main__":
    Main()
