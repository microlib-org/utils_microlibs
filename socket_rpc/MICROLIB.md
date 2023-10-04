# socket_rpc

Here, you can find a full list of the things you can do with `socket_rpc`.

## Contents

Full API:

1. [Expose a function over TCP](#expose-a-function-over-tcp)
2. [Call a function over TCP](#call-a-function-over-tcp)

### Expose a function over TCP

To expose a function over TCP, just decorate it with the `rpc` decorator:

```python
import logging
import sys

import numpy as np

from socket_rpc import rpc


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

@rpc(host='localhost', port=61000, buffer_size=1 * 1024 * 1024)
def callback(np_arr: np.ndarray):
    print(np_arr.shape)

```

### Call a function over TCP

To call a function already exposed with the rpc decorator, just use the `rpc_call` function:

```python
import numpy as np
from socket_rpc import rpc_call

send_np_arr = rpc_call(host='localhost', port=61000)

send_np_arr(np.arange(1111))
```