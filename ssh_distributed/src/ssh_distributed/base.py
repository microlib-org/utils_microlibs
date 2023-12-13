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
    base_dir = os.path.dirname(os.path.abspath(__file__))
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
    base_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(base_dir, 'upload_to_hosts.sh')

    args = [
        script_path, str(path.absolute().resolve()), *hosts
    ]
    subprocess.run(args)


def run_on_host(host, command):
    """
    Execute a command on a remote host using SSH.

    :param host: The hostname or IP address of the remote host.
    :param command: The command to be executed on the remote host.
    """
    ssh_command = ["ssh", host, command]
    try:
        subprocess.run(ssh_command)
    except subprocess.CalledProcessError as e:
        logging.error(f"Error occurred: {e.stderr}")


def download_from_hosts(
        source_path: Union[str, Path],
        out_path: Union[str, Path],
        hosts: List[str]
):
    logging.info("download_from_hosts.sh")
    source_path = Path(source_path)
    out_path = Path(out_path)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(base_dir, 'download_from_hosts.sh')

    args = [
        script_path, source_path, out_path, *hosts
    ]
    subprocess.run(args)


def delete_directory_from_hosts(
        path: Union[str, Path],
        hosts: List[str]
):
    logging.info("delete_directory_from_hosts.sh")
    path = Path(path)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(base_dir, 'delete_directory_from_hosts.sh')

    args = [
        script_path, path, *hosts
    ]
    subprocess.run(args)


if __name__ == "__main__":
    connect_tunnel(
        from_host="homebastion.local",
        to_host="home02.local",
        from_port=61002,
        to_port=61000,
        tmux_session_name="autossh_next"
    )
