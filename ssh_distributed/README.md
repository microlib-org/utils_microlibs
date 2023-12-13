# ssh_distributed

`ssh_distributed` is a very simple microlib for managing distributed computations using `ssh`.

Note: only works on Linux-based machines.

Install with:

```bash
pip install ssh_distributed
```

## Create autossh tunnel with port remapping

```python
import ssh_distributed

ssh_distributed.create_tunnel(
    from_host="home00.local",
    to_host="home01.local",
    from_port=61001,
    to_port=61000,
    tmux_session_name="autossh_next"
)
```

## Upload directory to hosts

```python
import ssh_distributed

ssh_distributed.upload_to_hosts(
    path="<PATH>",
    hosts=[
        "home00.local",
        "home01.local",
        "home02.local"
    ]
)
```