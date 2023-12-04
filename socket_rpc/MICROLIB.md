# socket_rpc

Here, you can find a full list of the things you can do with `socket_rpc`.

## Contents

Full API:

1. [Expose functions over TCP](#expose-functions-over-tcp)
2. [Call a function over TCP](#call-a-function-over-tcp)

### Expose functions over TCP

To expose a function over TCP, just add it to an `RPCServer`:

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

### Call a function over TCP

To call a function already exposed with the `RPCServer`, just use the `RPCClient` object:

```python
import numpy as np
from socket_rpc import RPCClient

client = RPCClient('127.0.0.1', 5555)
client.callback0(np.arange(100))
client.callback1(np.arange(10))
```