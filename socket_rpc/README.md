# socket_rpc

`socket_rpc` is a very simple microlib for remote procedure calls (RPC) over sockets in Python. 

It exposes two functions: 
- `rpc` - acts as a server for a Python RPC
- `rpc_call` - allows you to call a function, registered on another host with the `rpc` decorator.

Install with:

```bash
pip install socket_rpc
```

It has no external dependencies and is less than 100 lines of code.

## Quick server example

To expose a function over TCP, just decorate it with the `rpc` decorator:

```python
import logging
import sys

import numpy as np

from socket_rpc import RPCServer


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

def callback0(np_arr: np.ndarray):
    print('0', np_arr.shape)
    

def callback1(np_arr: np.ndarray):
    print('1', np_arr.shape)

server = RPCServer(host='localhost', port=61000, buffer_size=1 * 1024 * 1024)
server.add_fn(callback0)
server.add_fn(callback1)
server.serve()

```

## Quick call example

To call a function already exposed with the `rpc` decorator, just use the `rpc_call` function:

```python
import numpy as np
from socket_rpc import RPCClient

client = RPCClient('127.0.0.1', 5555)
client.callback0(np.arange(100))
client.callback1(np.arange(10))
```
