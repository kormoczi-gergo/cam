import socket



def main(recieved_image_pointer):
    # 1. Create the socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. Connect to the Server's IP
    # Replace '192.168.1.XX' with the actual IP of the Host laptop
    client_socket.connect(('192.168.0.44', 5005))

    # 3. Send data (Must be bytes!)
    message = "Motion Detected!"
    client_socket.send(message.encode('utf-8'))

    # 4. Close
    client_socket.close()





    

if __name__ == "__main__":
    main()