import pickle
import socket
from time import time

import torch


def send_np_array_to_server(numpy_array, server_address):
    # Serialize the NumPy array
    data = pickle.dumps(numpy_array)
    # Create and configure the socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(server_address)
        # Send the serialized data
        print(f"Send {time()}")
        client_socket.sendall(data)
    print(f"Array sent to {server_address}")


def main():
    # Define the server address and port
    server_address = ('localhost', 65432)

    # Create a NumPy array of dtype float32
    # Load the tokenizer and tokenize the input text
    from llm_falcon_model import load_tokenizer

    tokenizer = load_tokenizer()
    input_text = "Magnus Carlsen had won the World"
    input_ids = torch.tensor(tokenizer.encode(input_text, add_special_tokens=False).ids).unsqueeze(0).numpy()
    numpy_array = input_ids

    send_np_array_to_server(numpy_array, server_address)


if __name__ == '__main__':
    main()
