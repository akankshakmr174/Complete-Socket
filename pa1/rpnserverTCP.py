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
    host = ''
    port = 13001

    while True:
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_socket.bind((host, port))
        my_socket.listen(1)
        connection, addr = my_socket.accept()
        print("Connection From " + str(addr))

        while True:
            # buffer size 2048
            # one just pick a size that can hold the largest individual message
            # I think 2048 is likely fine.
            data = connection.recv(2048).decode('utf-8')
            if not data:
                break
            print("Operation: "+data)

            tokens = data.split()
            # Requirement: Limit the number of input "tokens"
            if len(tokens) == 3:
                left_operand, right_operand, operator = data.split()
                if operator in operators:
                    # If the operands are not number,
                    err = False
                    try:
                        left_operand = int(left_operand)
                        right_operand = int(right_operand)
                    except ValueError:
                        print('One or more operands are not numbers')
                        err = True
                    if err:
                        # if the error occurs, skip
                        continue
                    else:
                        # Compute the single operation which was sent from the client
                        result = operators[operator](left_operand, right_operand)
                        # end of RPN calculation
                        # Requirment 3)
                        # Have the server return the answer to the client
                        # i.e) Result: 120 //single output.
                        print("Result: "+str(int(result)))
                        connection.send(str(result).encode("utf-8"))
                else:
                    print("The operator is unknown or can't be a number")
            else:
                print("Requires only three tokens for a single operation")

        connection.close()
