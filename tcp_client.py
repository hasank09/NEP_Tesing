import socket


def run_client():
    # create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = '45.79.112.203'
    server_port = 4242
    # establish connection with server
    client.connect((server_ip, server_port))


    while True:
        msg = input("Enter message: ")
        client.send(msg.encode("utf-8")[:1024])

        # receive message from the server
        response = client.recv(1024)
        response = response.decode("utf-8")

        # if server sent us "closed" in the payload, we break out of the loop and close our socket
        if response.lower() == "closed":
            break
        if response:
            print(f"Received: {response}")
            #with open('gps_record_2_2.txt','ab') as file:
             #   file.write(response)

    # close client socket (connection to the server)
    client.close()
    print("Connection to server closed")

run_client()