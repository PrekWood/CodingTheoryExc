import socket


# When i want to send data from socket a convert it to string and the to binary
# to receive this data i convert it to string and the to list or int

def receive_data_from_client():
    not_receive = True
    data = -1
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while not_receive:
        try:
            s.connect((socket.gethostname(), 8181))
            # receive the message with 1 byte every time
            data = s.recv(1024)
            # Decode received data into UTF-8
            data = data.decode('utf-8')
            # Convert decoded data into list
            data = eval(data)
            not_receive = False
        except Exception:
            not_receive = True
    return data


def send_data_to_client(data):
    # make the socket
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            s1.bind((socket.gethostname(), 8080))
            break
        except Exception:
            continue

    s1.listen(5)
    # convert to string
    codded_word = data[0]
    data = str(data)
    # make it binary
    data = data.encode()
    print("----------------------------------------------------------------------------------")
    print("Welcome to Server Socket")
    print("~Run the client!~")
    print("* When you run the client you see the ip address, port and the input_message~")
    while True:
        clientsocket, address = s1.accept()
        print("~~~New client run")
        print(f"Connection from{address} has been established and the input_message was:")
        print(codded_word)
        clientsocket.send(data)
        break


def send_data_to_server(n):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            s.bind((socket.gethostname(), 8181))
            break
        except Exception:
            continue
    s.listen(5)
    n = str(n)
    n = n.encode()
    while True:
        clientsocket, address = s.accept()
        clientsocket.send(n)
        break


def receive_data_from_server():
    # make the connection s
    data = []
    not_receive = True
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while not_receive:
        try:
            s.connect((socket.gethostname(), 8080))
            # receive the message with 1 byte every time
            data = s.recv(1024)
            # Decode received data into UTF-8
            data = data.decode('utf-8')
            # Convert decoded data into list
            data = eval(data)
            not_receive = False
        except Exception:
            not_receive = True
    return data
