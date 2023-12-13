import subprocess
import os


def call_connect_tunnel():
    # Determine the directory of base.py
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to the connect_tunnel.sh script
    script_path = os.path.join(base_dir, 'connect_tunnel.sh')

    # Call the script using subprocess
    subprocess.run([script_path, "homebastion.local", "home02.local", "61002", "61000", "autossh_next"])


# Call the function
if __name__ == "__main__":
    call_connect_tunnel()
