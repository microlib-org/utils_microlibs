import pickle
import socket


def rpc_call(host: str, port: int):
    def wrapped(*args, **kwargs):
        server_address = (host, port)
        data = {
            'args': args,
            'kwargs': kwargs
        }
        pickled_data = pickle.dumps(data)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect(server_address)
            client_socket.sendall(pickled_data)
    return wrapped
