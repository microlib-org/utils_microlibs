import pickle
import logging
import socket
from typing import Callable


def listen_callback(
        callback: Callable,
        host: str,
        port: int,
        buffer_size: int # buffer_size = 10 * 1024 * 1024 for 10MB
):
    # Define the server address and port
    server_address = (host, port)

    # Create and configure the socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(server_address)
        server_socket.listen()

        logging.info(f"Server listening on {server_address}")

        try:
            while True:  # Infinite loop to continuously listen for connections
                logging.info("Waiting for a connection...")
                # Wait for a connection
                connection, client_address = server_socket.accept()
                with connection:
                    logging.info(f'Connected by {client_address}')
                    # Receive the data
                    data = b''
                    while True:
                        packet = connection.recv(buffer_size)
                        if not packet: break
                        data += packet

                    # Deserialize the received data
                    obj = pickle.loads(data)
                    args = obj['args']
                    kwargs = obj['kwargs']
                    callback(*args, **kwargs)

        except KeyboardInterrupt:
            logging.info("Server is shutting down.")


def rpc(host: str, port: int, buffer_size: int):
    def decorator(callback: Callable):
        def wrapper():
            listen_callback(callback, host, port, buffer_size)
        return wrapper
    return decorator
