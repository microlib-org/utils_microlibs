# socket_rpc

`socket_rpc` is a very simple microlib for remote procedure calls (RPC) over sockets in Python. 

It exposes two functions: 
- `rpc` - acts as a server for a Python RPC
- `rpc_call` - allows you to call a function, registered on another host with the `rpc` decorator.

Install with:

```bash
pip install socket_rpc
```

## Quick server example

To expose a function over TCP, just decorate it with the `rpc` decorator:

```python
import logging
import sys

import numpy as np

from socket_rpc import rpc


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


@rpc(host='localhost', port=61000, buffer_size=10 * 1024 * 1024)
def callback(np_arr: np.ndarray):
    print(np_arr.shape)

```

## Quick call example

To call a function already exposed with the `rpc` decorator, just use the `rpc_call` function:

```python
import numpy as np
from socket_rpc import rpc_call

send_np_arr = rpc_call(host='localhost', port=61000)

send_np_arr(np.arange(1111))
```
