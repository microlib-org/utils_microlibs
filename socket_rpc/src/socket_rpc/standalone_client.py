import pickle
import socket


class RPCClient:
    def __init__(self, host, port):
        self.server_address = (host, port)

    def __getattr__(self, callback_name):
        def wrapped(*args, **kwargs):
            return self.call_server(callback_name, *args, **kwargs)
        return wrapped

    def call_server(self, callback_name, *args, **kwargs):
        data = {
            'callback_name': callback_name,
            'args': args,
            'kwargs': kwargs
        }
        pickled_data = pickle.dumps(data)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect(self.server_address)
            client_socket.sendall(pickled_data)

