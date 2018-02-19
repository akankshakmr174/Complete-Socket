import socket
import sys
import operator


# Supporting addition, subtraction, multiplication and division.
operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}


if __name__ == '__main__':
    arguments = sys.argv
    host = ''
    port = 5002  # just a placeholder
    rpn_statement = ''

    try:
        # Get Host and port address
        host = arguments[1]
        port = int(arguments[2])
        # Requirement 1)
        # read arbitrary postfix expressions from the client command line
        rpn_statement = str(arguments[3])
    except ValueError as verr:
        print("Incorrect value of argument")
        sys.exit(0)
    except Exception as ex:
        # Incorrect Usage for different argument
        print(('Incorrect usage: python3 rpnclientTCP.py'
               '<IP address> <port> <rpn>'))
        sys.exit(0)

    # create socket Iv4 TCP AND connect to the host(server)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # RPN Calculation
    # Algorithms and Data Structures Stack07 Postfix Calculator
    # Video : https://www.youtube.com/watch?v=UU5UhVQhYkY
    # RPN calculation srouce code reference:
    # https://gist.github.com/slackorama/2281116
    stack = []
    tokens = rpn_statement.split()
    for token in tokens:
        # if the token is the number
        if set(token).issubset(set("0123456789.")):
            stack.append(float(token))
        elif token in operators:
            if len(stack) < 2:
                raise ValueError('Must have two parameters.')
            a = stack.pop()  # right operand
            b = stack.pop()  # left operand

            # Requirement 2)
            # Have the client transmit the expression to a server
            # where the computation will be performed.
            # -> The expression is a single operation
            operation = ""+str(int(b))+" "+str(int(a))+" "+str(token)

            # send the request with the operation
            client_socket.send(operation.encode("utf-8"))
            data = client_socket.recv(2048).decode("utf-8")

            # Push the result from the server
            # int(float(data)) -> Resolving invalid literal for int base 10 err
            stack.append(int(float(data)))
        else:
            raise ValueError("The RPN statement is not valid: %s" % token)

    if len(stack) == 1:
        # print the result
        # Requirement 4)
        # Have the client print the answer to the screen
        print(stack[0])
    else:
        print("The RPN calculation is not finished")

    # close the socket
    client_socket.close()
