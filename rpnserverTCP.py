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
    """This is main server."""
    host = ''
    port = 13001

    while True:
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_socket.bind((host, port))
        my_socket.listen(1)
        connection, addr = my_socket.accept()
        print("Connection From " + str(addr))

        while True:
            # buffer size 1024
            data = connection.recv(1024).decode('utf-8')
            if not data:
                break
            print("Operation: "+data)

            tokens = data.split()
            # Requirement: Limit the number of input "tokens"
            if len(tokens) == 3:
                left_operand, right_operand, operator = data.split()
            else:
                print("Requires only three tokens for a single operation")

            # Compute the single operation which was sent from the client
            result = operators[operator](int(left_operand), int(right_operand))

            # end of RPN calculation
            # Requirment 3)
            # Have the server return the answer to the client
            print("Result: "+str(int(result)))
            connection.send(str(result).encode("utf-8"))

        connection.close()
