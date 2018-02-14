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
    port = 5002  # it's just a placeholder before getting a port number
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

    server_address = ("127.0.0.1", 5000)  # server address

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.bind((host, port))

    # Set time out for 2 seconds
    client_socket.settimeout(2)
    request_count = 0

    while request_count < 3:
        try:
            # imcrement the request time attempt (for Timeout)
            request_count = request_count + 1

            # RPN Calculation starts here
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
                    # Have the client transmit the expression to server
                    # where the computation will be performed.
                    # -> The expression is a single operation
                    operation = ""+str(int(b))+" "+str(int(a))+" "+str(token)

                    # send the request with the operation
                    client_socket.sendto(
                        operation.encode('utf-8'),
                        server_address)
                    data, addr = client_socket.recvfrom(2048)
                    data = data.decode('utf-8')

                    # Push the result from the server
                    # int(float(data)) -> Resolving invalid literal for int base 10 err
                    stack.append(int(float(data)))
                else:
                    raise ValueError("RPN statement isn't valid: %s" % token)

            if len(stack) == 1:
                # print the result
                # Requirement 4)
                # Have the client print the answer to the screen
                print(stack[0])
            else:
                print("The RPN calculation is not finished")
            # Break the while loop if the connection was ok.
            break
        except socket.timeout:
            print("Connection Timeout")
            if request_count > 2:
                print("Closing after three connection attempts")
        except socket.error:
            print("Error Occured")

    client_socket.close()
