import logging
import pickle
import socket
import traceback
from typing import Callable


class RPCServer:
    def __init__(self, host: str, port: int, buffer_size: int = 10 * 1024 * 1024, client=None):
        self.host = host
        self.port = port
        self.buffer_size = buffer_size
        self.functions = {}  # dictionary to store function references
        self.client = client

    def add_fn(self, callback: Callable):
        name = callback.__name__
        self.functions[name] = callback

    def _collect_all_bytes(self, connection):
        data = b''
        while True:
            packet = connection.recv(self.buffer_size)
            if not packet: break
            data += packet
        return data

    def _handle_connection(self, connection, client_address):
        try:
            logging.info(f'Connected by {client_address}')
            data = self._collect_all_bytes(connection)
            obj = pickle.loads(data)
            callback_name = obj['callback_name']  # expects a 'callback_name' in the received object
            callback_args = obj['args']
            callback_kwargs = obj['kwargs']

            if callback_name in self.functions:
                return self.functions[callback_name](*callback_args, **callback_kwargs)
            else:
                logging.error(f"No such function: {callback_name}")

        except Exception as e:
            logging.error(f"Exception happened while processing connection: {e}")
            logging.error(traceback.format_exc())

    def serve(self):
        server_address = (self.host, self.port)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind(server_address)
            server_socket.listen()
            logging.info(f"Server listening on {server_address}")

            try:
                while True:
                    logging.info("Waiting for a connection...")
                    connection, client_address = server_socket.accept()
                    with connection:
                        output = self._handle_connection(connection, client_address)
                        if self.client is not None:
                            logging.info("Sending output to client")
                            self.client.receive(output)

            except KeyboardInterrupt:
                logging.info("Server is shutting down.")

    def serve_once(self, timeout: float):
        server_address = (self.host, self.port)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.settimeout(timeout)
            server_socket.bind(server_address)
            server_socket.listen()
            logging.info(f"Server listening on {server_address}")

            logging.info("Waiting for a connection...")
            connection, client_address = server_socket.accept()
            with connection:
                output = self._handle_connection(connection, client_address)
        return output
