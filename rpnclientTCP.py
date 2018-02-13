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
    # Get Host nad port address
    arguments = sys.argv

    host = arguments[1]
    port = arguments[2]
    rpn_statement = arguments[3]

    try:
        port = int(port)
        rpn_statement = str(rpn_statement)
    except ValueError as verr:
        print("Not a valid RPN arguments;")
        sys.exit(0)
    except Exception as ex:
        print("Error Occured")
        sys.exit(0)

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

            # Send a single operation to the server
            operation = ""+str(int(b))+" "+str(int(a))+" "+str(token)
            client_socket.send(operation.encode("utf-8"))
            data = client_socket.recv(2048).decode("utf-8")

            # Push the result from the server
            # int(float(data)) -> Resolving invalid literal for int base 10 err
            stack.append(int(float(data)))
        else:
            raise ValueError("The RPN statement is not valid: %s" % token)

    if len(stack) == 1:
        # print the result
        print(stack[0])
    else:
        print("Incomplete RPN statement")

    # close the socket
    client_socket.close()


if __name__ == '__main__':
    Main()
