import socket
import sys
import operator

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}


def eval_expression(tokens, stack):
    for token in tokens:
        if set(token).issubset(set("0123456789.")):
            stack.append(float(token))
        elif token in operators:
            if len(stack) < 2:
                raise ValueError('Must have two parameters.')
            a = stack.pop()
            b = stack.pop()
            op = operators[token]
            stack.append(op(b, a))
        else:
            raise ValueError("WTF? %s" % token)
    return stack


def Main():

    # Getting host and port address.
    # ex) rpncalc 127.0.0.1 13001 "246 549 +" where,
    # 127.0.0.1 : host address
    # 13001 : port address
    # 246 549 + : problem

    arguments = sys.argv

    host =  '127.0.0.1' # arguments[1]
    port = 13001 # arguments[2]
    #rpn_statement = arguments[3]

    try:
        port = int(port)
        # rpn_statement = str(rpn_statement)
    except ValueError as verr:
        print("Not a valid arguments; Check your host and port address as well as RPN statement")
        sys.exit(0)
    except Exception as ex:
        print("Not a valid arguments; Check your host and port address as well as RPN statement")
        sys.exit(0)

    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.bind((host, port))
    my_socket.listen()
    connection, addr = my_socket.accept()
    print("Connection From " + str(addr))

    while True:
        data = connection.recv(1024).decode('utf-8')
        if not data:
            break
        print("From connected server: "+data)

        # RPN Calculation Algorithm starts where
        stack = []
        # while True:
        expression = data
        if expression in ['quit', 'q', 'exit']:
            exit()
        elif expression in ['clear', 'empty']:
            stack = []
            continue
        elif len(expression) == 0:
            continue
        stack = eval_expression(expression.split(), stack)
        data = str(stack[0])
        # end of RPN calculation
        print("sending"+data)
        connection.send(data.encode("utf-8"))

    connection.close()


if __name__ == '__main__':
    Main()
