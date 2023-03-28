# Uncomment this to pass the first stage
import socket


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    #server_socket.accept() # wait for client

    # First, we store the connection into a variable so we can read its value.

    client_connection, _ = server_socket.accept()  # wait for client

    # Next, we read data from the connection. 
    # For this stage, we know that the tester only sends us PING, so we don't have to parse the incoming data.
    
    #client_connection.recv(1024)  # wait for client to send data

    # Once we've read data, we need to respond back with PONG.

    # Simple Strings are encoded as follows: a plus character, followed by a string that is "\r\n". 
    # Simple Strings are used to transmit non binary-safe strings with minimal overhead. 
    # For example, many Redis commands reply with just "OK" on success.  --> "+OK\r\n"

    # The ideal approach is to create a RESP encoder function — but for now, since we know that our response will always be PONG, we can hardcode the response. 

    #client_connection.send(b"+PONG\r\n")

    # The PING command is the simplest of all Redis commands. It always returns PONG as a response
    # This command is often used to test if a connection is still alive, or to measure latency.

    # As an improvement, we'll now monitor for more incoming requests — and each time we get one, we'll respond back with PONG, and go back to waiting for the next one.

    while True:
        client_connection.recv(1024)  # wait for client to send data
    client_connection.send(b"+PONG\r\n")

if __name__ == "__main__":
    main()
