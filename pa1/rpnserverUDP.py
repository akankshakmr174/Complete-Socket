import socket
import operator

# Supporting addition, subtraction, multiplication and division.
operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}


if __name__ == '__main__':
    host = "127.0.0.1"
    port = 5000

    # AF_INET: Internet Iv4
    # SOCK_DGRAM: UDP Protocol
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    while True:
        # 1024: Buffer Size (For UDP, shouldn't be sending larger than 1400)
        data, addr = server_socket.recvfrom(1024)
        data = data.decode('utf-8')

        print('message from user: ' + str(addr))
        print('from connected user: ' + data)

        # RPN part
        tokens = data.split()
        # Requirement: Limit the number of input "tokens"
        if len(tokens) == 3:
            left_operand, right_operand, operator = data.split()
            if operator in operators:
                err = False
                # If the operands are not number,
                try:
                    left_operand = int(left_operand)
                    right_operand = int(right_operand)
                except ValueError:
                    print('One or more operands are not numbers')
                    err = True

                # if the error occurs, pass the operation
                if err:
                    continue
                else:
                    # Compute the single operation which was sent from the client
                    result = operators[operator](left_operand, right_operand)
                    # end of RPN calculation
                    # Requirment 3)
                    # Have the server return the answer to the client
                    # i.e) Result: 120 //single output.
                    print("Result: "+str(int(result)))
                    server_socket.sendto(str(int(result)).encode('utf-8'), addr)
            else:
                print("The operator is unknown or can't be a number")
        else:
            print("Requires only three tokens for a single operation")
    # Close the Socket
    server_socket.close()
