import logging
import subprocess
import os
from pathlib import Path
from typing import Union, List


def connect_tunnel(
        from_host: str,
        to_host: str,
        from_port: int,
        to_port: int,
        tmux_session_name: str
):
    logging.info("Connect tunnel called. Make sure 'tmux' and 'autossh' are installed on all hosts.")
    # Determine the directory of base.py
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to the connect_tunnel.sh script
    script_path = os.path.join(base_dir, 'connect_tunnel.sh')

    args = [
        script_path, from_host, to_host, str(from_port), str(to_port), tmux_session_name
    ]
    subprocess.run(args)


def upload_to_hosts(
        path: Union[str, Path],
        hosts: List[str]
):
    logging.info("upload_to_hosts.sh")
    path = Path(path)
    # Determine the directory of base.py
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to the connect_tunnel.sh script
    script_path = os.path.join(base_dir, 'upload_to_hosts.sh')

    args = [
        script_path, str(path.absolute().resolve()), *hosts
    ]
    subprocess.run(args)


# Call the function
if __name__ == "__main__":
    connect_tunnel(
        from_host="homebastion.local",
        to_host="home02.local",
        from_port=61002,
        to_port=61000,
        tmux_session_name="autossh_next"
    )
