import socket
import sys

def Main():

    # Getting host and port address.
    # ex) rpncalc 127.0.0.1 13001 "246 549 +" where,
    # 127.0.0.1 : host address
    # 13001 : port address
    # 246 549 + : problem

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

    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.bind((host, port))
    my_socket.listen()
    c, addr = my_socket.accept()
    print("Connection From " + str(addr))

    while True:
        data = c.recv(1024).decode('utf-8')
        if not data:
            break
        print("From connected server: "+data)
        # RPN Calculation Algorithm starts where
        print("sending"+data)
        c.send(data.encode("utf-8"))

    c.close()


if __name__ == '__main__':
    Main()
