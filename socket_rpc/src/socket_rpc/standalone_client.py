import pickle
import socket


def receive(x):
    return x


class RPCClient:
    def __init__(
            self,
            host: str,
            port: int,
            response_server=None
    ):
        self.server_address = (host, port)
        self.server = response_server
        if self.server is not None:
            self.server.add_fn(receive)

    def __getattr__(self, callback_name):
        def wrapped(*args, **kwargs):
            self.call_server(callback_name, *args, **kwargs)
            if self.server is not None:
                return self.server.serve_once(20)

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
