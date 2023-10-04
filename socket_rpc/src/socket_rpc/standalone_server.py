import pickle
import logging
import socket
from functools import wraps
from typing import Callable


def _collect_all_bytes(buffer_size, connection):
    data = b''
    while True:
        packet = connection.recv(buffer_size)
        if not packet: break
        data += packet
    return data


def _handle_connection(connection, callback, client_address, buffer_size):
    logging.info(f'Connected by {client_address}')
    data = _collect_all_bytes(buffer_size, connection)
    obj = pickle.loads(data)
    callback_args = obj['args']
    callback_kwargs = obj['kwargs']
    callback(*callback_args, **callback_kwargs)


def listener(callback, host, port, buffer_size):
    server_address = (host, port)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(server_address)
        server_socket.listen()

        logging.info(f"Server listening on {server_address}")

        try:
            while True:
                logging.info("Waiting for a connection...")
                connection, client_address = server_socket.accept()
                with connection:
                    _handle_connection(connection, callback, client_address, buffer_size)

        except KeyboardInterrupt:
            logging.info("Server is shutting down.")


def rpc(host='127.0.0.1', port=5555, buffer_size=10 * 1024 * 1024):
    def decorator(callback: Callable):
        @wraps(callback)
        def wrapper(*args, **kwargs):
            # this is just to define the behavior when the decorated function is called directly
            return callback(*args, **kwargs)

        # start the listener in the background when the function is decorated
        listener(callback, host, port, buffer_size)
        return wrapper

    return decorator
