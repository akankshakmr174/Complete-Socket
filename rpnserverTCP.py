import socket
import sys
import operator

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}


def Main():

    # Getting host and port address.
    # ex) rpncalc 127.0.0.1 13001 "246 549 +" where,
    # 127.0.0.1 : host address
    # 13001 : port address
    # 246 549 + : problem

    host = ''
    port = 13001

    try:
        port = int(port)
        # rpn_statement = str(rpn_statement)
    except ValueError as verr:
        print("Incorrect RPN Statement")
        sys.exit(0)
    except Exception as ex:
        print("Incorrect RPN Statement")
        sys.exit(0)

    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.bind((host, port))
    my_socket.listen(5)
    connection, addr = my_socket.accept()
    print("Connection From " + str(addr))

    while True:
        data = connection.recv(1024).decode('utf-8')
        if not data:
            break
        print("Operation: "+data)

        if len(data) == 0:
            continue

        # Compute a single operation which was sent from the client
        left_operand, right_operand, operator = data.split()
        result = operators[operator](int(left_operand), int(right_operand))

        # end of RPN calculation
        print("Result: "+str(int(result)))
        connection.send(str(result).encode("utf-8"))

    connection.close()


if __name__ == '__main__':
    Main()
