import logging
import subprocess
import os
from pathlib import Path
from typing import Union, List


def create_tunnel(
        from_host: str,
        to_host: str,
        from_port: int,
        to_port: int,
        tmux_session_name: str
):
    logging.info("Connect tunnel called. Make sure 'tmux' and 'autossh' are installed on all hosts.")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(base_dir, 'create_tunnel.sh')

    args = [
        script_path, from_host, to_host, str(from_port), str(to_port), tmux_session_name
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


def download_from_hosts(
        from_path: Union[str, Path],
        to_path: Union[str, Path],
        hosts: List[str]
):
    logging.info("download_from_hosts.sh")
    from_path = Path(from_path)
    to_path = Path(to_path)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(base_dir, 'download_from_hosts.sh')

    args = [
        script_path, from_path, to_path, *hosts
    ]
    subprocess.run(args)


def download_part_weights(
        from_host: str,
        to_host: str,
        from_path: Union[str, Path],
        to_path: Union[str, Path],
        spec: str
):
    logging.info("download_part_weights.sh")
    from_path = Path(from_path)
    to_path = Path(to_path)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(base_dir, 'download_part_weights.sh')

    args = [
        script_path, from_host, to_host, from_path, to_path, spec
    ]
    subprocess.run(args)


def kill_tmux_session_on_host(
        host: str,
        name: str
):
    logging.info("kill_tmux_session_on_host.sh")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(base_dir, 'kill_tmux_session_on_host.sh')

    args = [
        script_path, host, name
    ]
    subprocess.run(args)


def run_on_host(
        host: str,
        command: str,
        name: str
):
    """
    Execute a command on a remote host using SSH.

    :param host: The hostname or IP address of the remote host.
    :param command: The command to be executed on the remote host.
    :param name: The name of the tmux session
    """
    logging.info("run_on_host.sh")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(base_dir, 'run_on_host.sh')

    args = [
        script_path, host, command, name
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

