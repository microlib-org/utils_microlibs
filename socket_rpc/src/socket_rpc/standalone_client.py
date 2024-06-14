import logging
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
        self.host = host
        self.port = port
        self.server = response_server
        if self.server is not None:
            self.server.add_fn(receive)
        self._client_ip = None
        if host.endswith('.local'):
            self._client_ip = socket.gethostbyname(host)

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
        if self._client_ip is not None:
            try:
                self._invoke_host(self._client_ip, pickled_data)
            except ConnectionRefusedError:
                # The .local domain changed ip
                self._client_ip = socket.gethostbyname(self.host)
                self._invoke_host(self.host, pickled_data)
        else:
            self._invoke_host(self.host, pickled_data)

    def _invoke_host(self, host, pickled_data):
        logging.info(f"Invoking {host}:{self.port}")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, self.port))
            client_socket.sendall(pickled_data)
